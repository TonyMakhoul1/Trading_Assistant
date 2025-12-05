# 🚀 Multi-Agent AI Stock Trading Assistant 📈

A smart AI-powered Stock Trading Assistant that helps users make informed trading decisions by providing:
* 📊 Market analysis and trends
* 💹 Buy/Sell/Hold recommendations
* 🧠 Clear explanations for each decision

Built using CrewAI multi-agent architecture, Streamlit UI, and live stock data via yfinance.

## 🚀 Project Overview

This project simulates a real-world AI trading assistant using two specialized AI agents, each responsible for a specific task:

| Agent | Role |
|-------|------|
| 📊 Market Analysis Agent | Fetches live stock data and extracts insights |
| 💹 Trading Recommendation Agent | Generates Buy/Sell/Hold recommendations with explanations |

All agents collaborate using CrewAI to generate a complete trading recommendation from a single stock symbol input.

## 🧱 Tech Stack

* **Python 3.10+**
* **CrewAI** – Multi-agent orchestration
* **Streamlit** – Web UI
* **yfinance** – Real-time stock market data

## 📂 Project Structure

```
crew_ai_multi_agents/
│
├── app.py                  # Streamlit web interface
├── main.py                 # Main execution entry point
├── crew.py                 # CrewAI agent orchestration
├── requirements.txt        # Project dependencies
├── .gitignore
│
├── tools/
│   └── stock_research_tool.py   # Live stock data extraction using yfinance
│
├── agents/
│   ├── analyst_agent.py         # Market Analysis Agent
│   └── trader_agent.py          # Trading Recommendation Agent
│
└── tasks/
    ├── analyse_task.py          # Market analysis task
    └── trade_task.py            # Trading decision task
```

## 🖥️ How It Works

1. User enters a stock symbol (e.g., `AAPL`, `TSLA`) in the Streamlit UI.
2. Input is passed to the CrewAI system.
3. **Market Analysis Agent** fetches live data using yfinance and extracts key indicators:
   * Current price
   * Daily change
   * Trading volume
   * Market trends
4. **Trading Recommendation Agent** processes the analysis and generates a Buy/Sell/Hold recommendation with a clear explanation.
5. Results are displayed in the Streamlit dashboard.


## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

## ✅ Features

* ✅ Real-time stock data fetching using yfinance
* ✅ Multi-Agent AI system (CrewAI)
* ✅ Clear Buy/Sell/Hold recommendations
* ✅ Explanations for each recommendation
* ✅ Simple Streamlit UI
* ✅ Modular and scalable architecture

## 🎯 Use Case

This project demonstrates:
* Multi-agent orchestration in AI
* Real-world financial data integration
* AI reasoning for decision-making
* End-to-end product-ready AI system


## 📌 Future Enhancements

* ✅ Integrate more market indicators and technical analysis
* ✅ Add user portfolio tracking
* ✅ Implement alert notifications (email/WhatsApp)
* ✅ Advanced AI reasoning for risk assessment
* ✅ Deploy web app publicly

## 👨‍💻 Author

**Tony Makhoul**  
Computer Engineer | AI Engineer | ML/DL Engineer
 - Lebanese International University

---
