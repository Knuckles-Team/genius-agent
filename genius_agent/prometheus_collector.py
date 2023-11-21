#!/usr/bin/env python
# coding: utf-8

from prometheus_client import start_http_server

def start_prometheus_server(port):
    start_http_server(port)

if __name__ == "__main__":
    start_prometheus_server(8999)  # Adjust the port as needed
