import yfinance as yf
import PySimpleGUI as sg
investmentsFilePath = './myInvestments.txt'

# SET SOME LAYOUT VALUES
layout = []
sg.theme('dark')


with open(investmentsFilePath, 'r') as file:
    investments = []
    for line in file:
        [ticker, pricePayed, quantity] = line.split()
        investments.append({
            "ticker": ticker + ".SA",
            "payed": float(pricePayed),
            "quantity": float(quantity)
        })

totalPayedOnWallet = 0
currentPriceOnWallet = 0

option = input("1- Status\n2- Cotação atual")

if(option == '1'):
    for investment in investments:
        try:
            [tickerName, payedPerAction, quantity] = investment['ticker'], (investment['payed']), (investment['quantity'])
            ticker = yf.Ticker(tickerName)
            currentPricePerAction = ticker.info['previousClose']

            currentPrice = currentPricePerAction * quantity
            payed = payedPerAction * quantity

            totalPayedOnWallet += payedPerAction * quantity
            currentPriceOnWallet += currentPricePerAction * quantity

            percentualAppreciation = (currentPrice / payed - 1) * 100

            outputText = f'The share {tickerName} had an appreciation of {percentualAppreciation:.2f}%'
        except:
            outputText = f'The ticker {tickerName} is unable.'

        layout.append([sg.Text(outputText)])
        print(outputText)
    print(f'Sua carteira teve uma valorização de {(currentPriceOnWallet / totalPayedOnWallet - 1) * 100:.2f}%')

elif(option == '2'):
    for investment in investments:
        try:
            [tickerName, payedPerAction, quantity] = investment['ticker'], (investment['payed']), (investment['quantity'])
            ticker = yf.Ticker(tickerName)
            currentPricePerAction = ticker.info['previousClose']

            outputText = f'The share {tickerName} is listed at {currentPricePerAction:.2f}'
        except:
            outputText = f'The ticker {tickerName} is unable.'

        layout.append([sg.Text(outputText)])
        print(outputText)


# PRINTING THE LAYOUT
window = sg.Window('My Investments', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


