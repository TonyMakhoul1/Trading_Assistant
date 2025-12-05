import streamlit as st
from main import run

st.set_page_config(page_title="AI Stock Analyst & Trader", layout="centered")

st.title("📈 AI Stock Market Analyst & Trader")
st.write("Enter a stock symbol and let the AI agents analyze and give a trading decision.")

symbol = st.text_input("Enter Stock Symbol (like: AAPL, TSLA, MSFT):").upper()

if st.button("Analyze"):
    if not symbol:
        st.error("Please enter a stock symbol.")
    else:
        st.write("Running analysis... please wait.")

        result = run(symbol)

        st.success("Analysis Completed!")

        raw = result.raw
        tasks = result.tasks_output

        task1 = tasks[0].raw if len(tasks) > 0 else "No task 1 output."

        task2 = tasks[1].raw if len(tasks) > 1 else "No task 2 output."

        st.subheader("📊 Market Analysis")
        st.write(task1)

        st.markdown("---")

        st.subheader("📈 Strategic Trading Decision")
        st.write(task2)

        st.markdown("---")

        st.subheader("🧠 Full Raw Output")
        st.text(raw)
