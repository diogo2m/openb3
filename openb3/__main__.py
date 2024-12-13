from openb3 import *
from time import sleep
import matplotlib.pyplot as plt
from multiprocessing import Process
from threading import Thread, Event
import json
import mysql.connector
import bcrypt

def sync_user():
    pass

def sync_portfolio():
    pass

def plot_price_over_time(y: list[float], collect_step: int = 1, filename: str = None, label: str = None, keep_open=False):
    x = [i*collect_step for i in range(len(y))]

    plt.plot(x, y, label=label, color="blue", linestyle="-", marker="o")

    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.title("Price Over Time")

    plt.legend()

    # plt.show()
    if filename:
        plt.savefig(f'outputs/{filename}.png')

    if not keep_open:
        plt.close()

def create_login(db: Database) -> int:
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    password = input("Password: ")
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    password = input("Retype password: ")
    if bcrypt.checkpw(password.encode(), hashed_password):
        UserDAO.add_user(db, name, email, hashed_password.decode(), phone)
        return UserDAO.get_user_by_email(db, email)["id"]
    else:
        print("Passwords do not match.")
        return None

def login(db: Database) -> int:
    email = input("Email: ")
    user = UserDAO.get_user_by_email(db, email)

    if not user:
        return None

    password = input("Password: ")
    hashed_password = user["password"].encode()

    if bcrypt.checkpw(password.encode(), hashed_password):
        return user["id"]
    else:
        return None

def create_portfolio(db: Database, user_id: int = None, name: str = None, stock_codes: list[str] = []):

    if not all([user_id, name, stock_codes]):
        name = input("Name: ")
        stock_codes = input("Stocks: ")
        stock_codes = stock_codes.replace(" ", "").split(",")

    PortfolioManager(user_id, name, stock_codes, db=db)

def create_trigger(db: Database, portfolio_id: int, stock_code: str = None, upper_limit: float = None, lower_limit: float = None, method: str = None):

    portfolio = PortfolioManager(db=db, portfolio_id=portfolio_id)

    if not all([stock_code, upper_limit, lower_limit, method]):
        stock_code = input("Stock: ")
        upper_limit = input("Upper Limit: ")
        lower_limit = input("Lower Limit: ")
        method = input("Method: ")

    portfolio.create_notification_trigger(stock_code=stock_code, lower_limit=lower_limit, upper_limit=upper_limit, method=method)

def menu():
    return NotImplemented

if __name__ == "__main__":

    db = Database("localhost", "root", "root", "OpenB3")

    user_id = 1

    if not user_id:
        if input("Do you want to create an account? (y/n): ") == 'y':
            user_id = create_login(db=db)
        else:
            user_id = login(db=db)

    if not user_id:
        print("Your login attempt failed, exiting.")
        exit(1)

    print(f"Welcome user {user_id}!")

    while input("Do you want to create a new portfolio? (y/n)") == 'y':
        create_portfolio()

        # create_portfolio(db, 1, "My Portfolio", ["PETR4", "ITUB4", "BBAS3"])
        # create_portfolio(db, 1, "Watching", ["PETR4", "WEGE3", "GGBR4"])
        # create_portfolio(db, 1, "Sister's Portfolio", ["VALE3", "ITSA4"])

    while input("Do you want to create a new trigger? (y/n)") == 'y':
        create_trigger()

        # create_trigger(db, 3, "VALE3", 57.00, 57.10, "push")

    print("Listing your portfolios: ")
    portfolio_managers = []
    portfolios = PortfolioDAO.get_portfolios_by_user_id(db, user_id)
    for portfolio in portfolios:
        new_portfolio = PortfolioManager(user_id=user_id, portfolio_id=portfolio["id"], db=db)
        portfolio_managers.append(new_portfolio)
        print(new_portfolio)

    print("Synchronizing your triggers: ")
    for trigger in NotificationTriggerDAO.get_notification_triggers_by_user(db, user_id):
        portfolio_managers[0].create_notification_trigger(notification_trigger_id = trigger["id"])

    print("Creating your data collector")
    my_collector = DataCollector(db=db, step_time=1)

    print("Populating data collector with all stocks in portfolios")
    stocks = set()
    for pm in portfolio_managers:
        for s in pm.stocks:
            stocks.add(s.code)

    for s in stocks:
        my_collector.add_stock(s)

    print("Trying to add BOAC34 to the data collector")
    my_collector.add_stock("BOAC34")

    stop_event = Event()
    print("Running deamon")
    
    thread = Thread(target=my_collector.daemon, args=(stop_event,), daemon=True)
    thread2 = Thread(target=portfolio_managers[0].daemon, args=(stop_event,), daemon=True)

    thread2.start()
    thread.start()

    sleep(10)

    print("Terminating process")
    stop_event.set()
    thread.join()
    thread2.join()

    over_times = []
    for stock_code in my_collector.watch_list:
        y = my_collector.watch_list[stock_code].pricing_history
        plot_price_over_time(y, filename=stock_code, label=stock_code)
        over_times.append(y)
    for y, stock_code in zip(over_times, my_collector.watch_list):
        plot_price_over_time(y, filename="summarized", label=stock_code, keep_open=True)
