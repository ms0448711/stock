import twstock
import mplfinance as mpf
import pandas as pd


def show_stock():
    stock = twstock.Stock("2330")
    data=stock.fetch_from(year=2023, month=3)

    