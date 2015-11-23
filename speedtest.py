#!/usr/bin/env python

from __future__ import print_function
import httplib2
import os
import gdata
import yaml
import subprocess
import re
import time
from pysed import replace

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

# Parse possible args (--noauth_local_webserver)
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# Load config file
with open("config.yml", 'r') as ymlfile:
    config = yaml.load(ymlfile)

# Set constants
SCOPES = 'https://spreadsheets.google.com/feeds/'
CLIENT_SECRET_FILE = config['google']['client_secret_file']
APPLICATION_NAME = 'google-speedtest-chart'

# Function to check for valid OAuth access tokens
def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'drive-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print('--------')
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
        print('--------')
    return credentials

# Function to submit speedtest result
def submit_into_spreadsheet(ping, download, upload):
    credentials = get_credentials()

    # Use it within gdata
    import gdata.spreadsheets.client
    import gdata.spreadsheets.client
    import gdata.spreadsheets.data
    import gdata.gauth

    # create the spreadsheet client and authenticate
    spr_client = gdata.spreadsheets.client.SpreadsheetsClient()
    auth2token = gdata.gauth.OAuth2TokenFromCredentials(credentials)
    spr_client = auth2token.authorize(spr_client)

    # Prepare dictionary
    dict = {}
    dict['date'] = time.strftime('%m/%d/%Y') + " " +  time.strftime('%H:%M:%S')
    dict['ping'] = ping
    dict['download'] = download
    dict['upload'] = upload
    print(dict)

    entry = gdata.spreadsheets.data.ListEntry()
    entry.from_dict(dict)

    # add the ListEntry you just made
    spr_client.add_list_entry(entry, config['google']['spreadsheet_id'], config['google']['worksheet_id'])

# Main function to run speedtest
def main():
    # Check for proper credentials
    print("Checking OAuth validity ... ")

    credentials = get_credentials()

    # Run speedtest and store output
    print("Starting speed test ... ")
    speedtest_result=subprocess.check_output(["/usr/local/bin/speedtest-cli"], stderr=subprocess.STDOUT)
    print("Starting speed finished!")

    # Find download bandwidth and substitute unimportant bits
    download = re.findall(r'Download: [0-9\.]* .bit', speedtest_result, re.MULTILINE)[0]
    download = replace(download, "Download: ", "")
    download = replace(download, ".bit", "")

    # Find upload bandwidth and substitute unimportant bits
    upload = re.findall(r'Upload: [0-9\.]* .bit', speedtest_result, re.MULTILINE)[0]
    upload = replace(upload, "Upload: ", "")
    upload = replace(upload, ".bit", "")

    # Find ping latency and substitute unimportant bits
    ping = re.findall(r'[0-9\.]* ms', speedtest_result, re.MULTILINE)[0]
    ping = replace(ping, " ms", "")

    # Write to spreadsheet
    print("Writing to spreadsheet ...")
    submit_into_spreadsheet(ping, download, upload)
    print("Successfuly written to spreadsheet!")

if __name__ == '__main__':
    main()
