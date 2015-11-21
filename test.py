from __future__ import print_function
import httplib2
import os
import gdata
import yaml

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
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# Main function
def main():
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

    #create a ListEntry. the first item of the list corresponds to the first 'header' row
    entry = gdata.spreadsheets.data.ListEntry()
    entry.set_value('ham', 'gary')
    entry.set_value('crab', 'sack')

    # add the ListEntry you just made
    spr_client.add_list_entry(entry, config['google']['spreadsheet_id'], config['google']['worksheet_id'])

if __name__ == '__main__':
    main()
