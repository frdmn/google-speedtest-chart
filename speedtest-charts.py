#!/usr/bin/env python3

import os
import subprocess
import re
import datetime
import pygsheets
import speedtest

# Set constants
DATE = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

def get_credentials():
    """Function to check for valid OAuth access tokens."""
    gc = pygsheets.authorize(outh_file="credentials.json")
    return gc

def submit_into_spreadsheet(download, upload, ping):
    """Function to submit speedtest result."""
    gc = get_credentials()

    speedtest = gc.open(os.getenv('SPREADSHEET', 'Speedtest'))
    sheet = speedtest.sheet1

    data = [DATE, download, upload, ping]

    sheet.append_table(values=data)

def main():
    # Check for proper credentials
    print("Checking OAuth validity...")
    credentials = get_credentials()

    # Run speedtest and store output
    print("Starting speed test...")
    spdtest = speedtest.Speedtest()
    spdtest.get_best_server()
    download = spdtest.download()
    upload = spdtest.upload()
    ping = spdtest.results.ping
    print("Starting speed finished!")

    # Write to spreadsheet
    print("Writing to spreadsheet...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")

if __name__ == "__main__":
    main()
