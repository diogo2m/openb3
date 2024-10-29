[![License](https://img.shields.io/github/license/diogo2m/openb3.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/workflow/status/diogo2m/openb3/CI)](https://github.com/diogo2m/openb3/actions)  
[![Issues](https://img.shields.io/github/issues/diogo2m/openb3)](https://github.com/diogo2m/openb3/issues)

<style>
    *{
        font-family: 'Open Sans', sans-serif;
        color: #1f1f1f;
    }

    td{
        text-align: center;
    }

    table{
        align-content: center;
        width: 100%;
        height: 240px;
        margin: auto;
        padding: auto;
    }

    .logo-text{
        font-family: 'Open Sans', sans-serif;
        color: #000000;
        font-weight: bold;
        font-size: 30px;
    }

    .list{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        list-style-type: none;
        width: 520px;
        background-color: #f1f5f1;
        margin: 20px;
        padding: 20px;
    }

    .list-item{
        margin: 0px;
    }
</style>

<center>    
  <img src="./img/OpenB3_Logo.svg" alt="OpenB3" width="170">
  <p class="logo-text">build your future.</p>
  <ul class="list">
    <li style="margin: 0px"> <a href="#introduction">Introduction</a></li>
    <li style="margin: 0px"> <a href="#software-architecture">Software Architecture</a></li>
    <li style="margin: 0px"> <a href="#planning">Planning</a></li>
    <li style="margin: 0px"> <a href="#getting-started">Getting Started</a></li>
  </ul>
</center>

Welcome to the **OpenB3**, an open-source initiative to assist Brazilian investors in collecting, managing, and analyzing stock market data with ease. This tool provides various utilities such as notifications for stock price movements, stock filtering based on key parameters, and helpful calculations for stock analysis.

---

## 🚀 Features

### 1. **Real-Time Notifications**
   - Receive alerts when stock prices move beyond user-defined limits or based on the stock's beta index.
   - Stay informed about significant market fluctuations to help make timely investment decisions.

### 2. **Stock Filtering**
   - Filter stocks based on essential metrics such as:
     - P/E (Price-to-Earnings) Ratio
     - P/BV (Price-to-Book Value)
     - Dividend Yield
     - ROE (Return on Equity)
   - Quickly find stocks that meet your investment strategy criteria.

### 3. **Stock Analysis Calculations**
   - Perform various calculations to assist in stock analysis, including:
     - Moving averages (e.g., Simple Moving Average, Exponential Moving Average)
     - Volatility
     - Beta index
     - Support and resistance levels
     - Risk assessment tools such as Sharpe and Sortino ratios

---

## 📊 Use Cases

- **Active traders**: Get notified when stock prices move beyond critical thresholds.
- **Long-term investors**: Analyze stock fundamentals using metrics such as P/E ratio, P/BV, and others.
- **Risk-averse investors**: Use beta index and volatility metrics to assess the risk level of a stock.
- **Analysts**: Perform in-depth analysis using moving averages, price patterns, and volatility calculations.

---

## 🔧 Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/diogo2m/openb3.git
cd openb3
pip install -r requirements.txt
```

You can also install using Docker:

```bash
docker build -t stock-analysis .
docker run -p 8080:8080 stock-analysis
```

---

## 📈 Getting Started

1. **Set up your API keys**  
   Obtain access to stock market data by registering for an API key from providers like Alpha Vantage, Yahoo Finance, or B3.

2. **Configure the alert thresholds**  
   Define the limits for stock prices or beta index values to receive timely notifications. Example configuration:

```yaml
# config.yaml
alerts:
  stock_price:
    PETR4:
      lower_limit: 25.00
      upper_limit: 30.00
  beta:
    PETR4: 1.2
```

3. **Run the stock analysis**  
   Once configured, start the tool to track stock prices and perform calculations:

```bash
python main.py
```

---

## 📊 Examples

### Stock Filtering by P/E Ratio

```bash
python data_collector.py --filter pe_ratio<=15 sector="Energy"
python data_collector.py --list sector
```

### Calculating Moving Average

```bash
python calculate_ma.py --ticker PETR4 --days 30
```

---

## 🛠️ Contributing

We welcome contributions from the community! Please follow these steps to get involved:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.

For more details, check out our [Contributing Guidelines](CONTRIBUTING.md).

---

## 📝 License

This project is licensed under the GNU Affero General Public License (AGPL) v3.0 - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For any questions, feel free to reach out via:

- Email: diogomonteiro.aluno@unipampa.edu.br
- GitHub Issues: [Submit an issue](https://github.com/diogo2m/openb3/issues) 

---

## 🙌 Acknowledgments

We'd like to thank the following:

- [Alpha Vantage](https://www.alphavantage.co) for providing financial data.
- The open-source community for inspiring this project.

---

### Future Work

- **Machine Learning**: Implement models to predict stock trends.
- **Portfolio Analysis**: Assist users in managing their portfolios more effectively.
- **Brazilian Market Optimization**: Focus on real-time data from the B3 (Brazil Stock Exchange).
