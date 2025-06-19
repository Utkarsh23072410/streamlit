import streamlit as st
import yfinance as yf
import datetime
ticker_symbol = st.text_input("Name of the stock", "AAPL")

start_date = st.date_input("Start date", datetime.date(2019, 1, 7))
end_date = st.date_input("End date", datetime.date(2023, 1, 7))
data =yf.download(ticker_symbol,start=start_date,end=end_date)


st.write(data) 
st.line_chart(data["Close"])