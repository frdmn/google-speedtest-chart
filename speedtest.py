#!/usr/bin/env python

import os
import subprocess
import re
import datetime
import pygsheets

# Set constants
SCOPE = ["https://spreadsheets.google.com/feeds/"]
DOWNLOAD_RE = re.compile(r"Download: ([\d.]+) .bit")
UPLOAD_RE = re.compile(r"Upload: ([\d.]+) .bit")
PING_RE = re.compile(r"([\d.]+) ms")
DATE = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")

# Function to check for valid OAuth access tokens
def get_credentials():
    gc = pygsheets.authorize(service_file="credentials.json")
    return gc

# Function to submit speedtest result
def submit_into_spreadsheet(download, upload, ping):
    gc = get_credentials()

    speedtest = gc.open("Speedtest")
    sheet = speedtest.sheet1

    data = [DATE, download, upload, ping]
    print(data)

    sheet.append_row(values=data)

# Main function to run speedtest
def main():
    # Check for proper credentials
    print("Checking OAuth validity ... ")

    credentials = get_credentials()

    # Run speedtest and store output
    print("Starting speed test ... ")
    speedtest_result = subprocess.check_output(["speedtest-cli"], stderr=subprocess.STDOUT)
    print("Starting speed finished!")

    # Find download bandwidth
    download = DOWNLOAD_RE.search(str(speedtest_result)).group(1)
    # Find upload bandwidth
    upload = UPLOAD_RE.search(str(speedtest_result)).group(1)
    # Find ping latency
    ping = PING_RE.search(str(speedtest_result)).group(1)

    # Write to spreadsheet
    print("Writing to spreadsheet ...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")

if __name__ == "__main__":
    main()
