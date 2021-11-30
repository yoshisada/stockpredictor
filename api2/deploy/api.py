import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from fbprophet import Prophet
from flask import Flask
from flask import request
import yfinance as yf

app = Flask(__name__)


@app.route('/result', methods = ['POST'])
def result():
    data = request.json
    print(data["data"])
    ticker = yf.Ticker(data["data"])
    print(ticker)
    data_ticker = ticker.history(period="60mo")
    data_ticker.reset_index(inplace=True)
    print(data_ticker, data_ticker.info())
    #print(data2.index)
    newDF = pd.DataFrame(data_ticker, columns = ["Date", "Close"])
    prophet_df = newDF.rename(columns={"Date":'ds', "Close":'y'})

    prophet_data = Prophet()
    prophet_data.fit(prophet_df)

    future = prophet_data.make_future_dataframe(periods = 360)
    forecast = prophet_data.predict(future)

    #fig = prophet_data.plot(forecast, xlabel='ds', ylabel='yhat')
    print(forecast.info())
    t1 = go.Scatter(x=prophet_df["ds"][-360:], y=prophet_df["y"][-360:], name = "Actual Price")
    t2 = go.Line(x=forecast["ds"][-720:], y=forecast["yhat"][-720:], name = "Predicted Price")


    t3 = go.Scatter(x=forecast["ds"][-720:], y=forecast["yhat_lower"][-720:] + ((forecast["trend_lower"][-720:]-forecast["trend"][-720:])),
    mode='lines', line_color='grey', name = "Pred Price Lower")
    t4 = go.Line(x=forecast["ds"][-720:], y=forecast["yhat_upper"][-720:] + ((forecast["trend_upper"][-720:]-forecast["trend"][-720:])), fill='tonexty',
    mode='lines', line_color='grey', name = "Pred Price Upper")


    # print(forecast["trend"], forecast["trend_lower"]-forecast["trend"])
    # print(forecast["yhat_upper"] + (forecast["trend_lower"]-forecast["trend"]))
    fig = make_subplots()
    
    fig.add_trace(t2)
    fig.add_trace(t3)
    fig.add_trace(t4)
    fig.add_trace(t1)
    fig.update_layout(title_text="1 Year Price History for "+data["data"]+" and 1 Year Predicted Data", xaxis_title="Date",
    yaxis_title="Price USD")
    fig.write_image("../../public/5yrForecast.png")
    fig.write_html("../../public/5yrForecast.html")
    #fig.show()
    fig = px.line(forecast, x='ds', y=forecast.columns)
    fig = prophet_data.plot(forecast)
    fig.show()

    print(prophet_df)
    t1 = go.Line(x=data_ticker["Date"], y=data_ticker["Close"])
    fig = make_subplots()
    fig.add_trace(t1)
    fig.update_layout(title_text="5 Year Price History for "+data["data"], xaxis_title="Date",
    yaxis_title="Price USD")
    fig.write_image("../../public/5yr.png")
    fig.write_html("../../public/5yr.html")
    #fig.show()
    return data

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

