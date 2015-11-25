#!/usr/bin/env python

from __future__ import print_function
import os
import json
import subprocess
import re
import time

import gdata
import gdata.spreadsheets.client
import gdata.spreadsheets.data
import gdata.gauth

import oauth2client
import oauth2client.client
import oauth2client.tools
import oauth2client.file

# Set constants
SCOPES = "https://spreadsheets.google.com/feeds/"
APPLICATION_NAME = "google-speedtest-chart"

DOWNLOAD_RE = re.compile(r"Download: ([\d.]+) .bit")
UPLOAD_RE = re.compile(r"Upload: ([\d.]+) .bit")
PING_RE = re.compile(r"([\d.]+) ms")

# Parse possible args (--noauth_local_webserver)
try:
    import argparse
    flags = argparse.ArgumentParser(
        parents=[oauth2client.tools.argparser]).parse_args()
except ImportError:
    flags = None

# Load config file
with open("config.json", "r") as configfile:
    config = json.load(configfile)

# Function to check for valid OAuth access tokens
def get_credentials():
    home_dir = os.path.expanduser("~")
    credential_dir = os.path.join(home_dir, ".credentials")
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, "drive-python-quickstart.json")

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print("--------")
        flow = oauth2client.client.flow_from_clientsecrets(
            config["client_secret_file"], SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = oauth2client.tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = oauth2client.tools.run(flow, store)
        print("Storing credentials to " + credential_path)
        print("--------")
    return credentials

# Function to submit speedtest result
def submit_into_spreadsheet(ping, download, upload):
    credentials = get_credentials()

    # create the spreadsheet client and authenticate
    spr_client = gdata.spreadsheets.client.SpreadsheetsClient()
    auth2token = gdata.gauth.OAuth2TokenFromCredentials(credentials)
    spr_client = auth2token.authorize(spr_client)

    # Prepare dictionary
    data = {
        "date": time.strftime("%m/%d/%Y %H:%M:%S"),
        "ping": ping,
        "download": download,
        "upload": upload,
    }
    print(data)

    entry = gdata.spreadsheets.data.ListEntry()
    entry.from_dict(data)

    # add the ListEntry you just made
    spr_client.add_list_entry(entry, config["spreadsheet_id"], config["worksheet_id"])

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
    download = DOWNLOAD_RE.search(speedtest_result).group(1)
    # Find upload bandwidth
    upload = UPLOAD_RE.search(speedtest_result).group(1)
    # Find ping latency
    ping = PING_RE.search(speedtest_result).group(1)

    # Write to spreadsheet
    print("Writing to spreadsheet ...")
    submit_into_spreadsheet(ping, download, upload)
    print("Successfuly written to spreadsheet!")

if __name__ == "__main__":
    main()
