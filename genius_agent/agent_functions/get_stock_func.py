#!/usr/bin/env python
# coding: utf-8

import yfinance as yf


def exec_get_stock_price(symbol: str) -> float:
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price

