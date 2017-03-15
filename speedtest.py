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

def get_credentials():
    """Function to check for valid OAuth access tokens."""
    gc = pygsheets.authorize(outh_file="credentials.json")
    return gc

def submit_into_spreadsheet(download, upload, ping):
    """Function to submit speedtest result."""
    gc = get_credentials()

    speedtest = gc.open("Speedtest-2")
    sheet = speedtest.sheet1

    data = [DATE, download, upload, ping]

    sheet.append_row(values=data)

def main():
    # Check for proper credentials
    print("Checking OAuth validity...")
    credentials = get_credentials()

    # Run speedtest and store output
    print("Starting speed test...")
    speedtest_result = subprocess.check_output(["speedtest-cli"], stderr=subprocess.STDOUT)
    print("Starting speed finished!")

    # Find download bandwidth
    download = DOWNLOAD_RE.search(str(speedtest_result)).group(1)
    # Find upload bandwidth
    upload = UPLOAD_RE.search(str(speedtest_result)).group(1)
    # Find ping latency
    ping = PING_RE.search(str(speedtest_result)).group(1)

    # Write to spreadsheet
    print("Writing to spreadsheet...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")

if __name__ == "__main__":
    main()
