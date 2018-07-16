#!/usr/bin/env python3

import os
import datetime
import pygsheets
import speedtest

# Set options
bymonth = True

# Set constants
DATE = datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S")
sheetname = datetime.datetime.now().strftime("%b test1 %Y")
header = [['Date'], ['Download'], ['Upload'], ['Ping']]
workbookname = os.getenv('SPREADSHEET', 'Speedtest-test3')

# set variable scope
download = ''
upload = ''
ping = ''


def get_credentials():
    """Function to check for valid OAuth access tokens."""
    gc = pygsheets.authorize(outh_file="credentials.json")
    return gc


def submit_into_spreadsheet(download, upload, ping):
    """Function to submit speedtest result."""
    gc = get_credentials()

    try:
        speedtest = gc.open(workbookname)
    except pygsheets.SpreadsheetNotFound:
        speedtest = gc.create(workbookname)

    if not bymonth:
        sheet = speedtest.sheet1
    else:
        try:
            sheet = speedtest.worksheet('title', sheetname)
        except pygsheets.WorksheetNotFound:
            sheet = speedtest.add_worksheet(sheetname)

        head1 = sheet.cell('A1').value
        print(head1)
        if head1 != header[1]:
            sheet.update_cells('A1:D1', header)
            headrange = sheet.range('A1:D1')
            headrange.set_text_format('bold', 'true')

    data = [DATE, download, upload, ping]

    sheet.append_table(values=data)


def getresults():
    spdtest = speedtest.Speedtest()
    spdtest.get_best_server()
    download = round(spdtest.download() / (2 ** 20), 2)
    upload = round(spdtest.upload() / (2 ** 20), 2)
    ping = round(spdtest.results.Ping)

    return(download, upload, ping)


def getresults_test():
    download = '200'
    upload = '300'
    ping = '20'

    return(download, upload, ping)


def main():
    # Check for proper credentials
    print("Checking OAuth validity...")
    try:
        get_credentials()
    except pygsheets.AuthenticationError:
        print("Authentication Failed")
        raise

    # Run speedtest and store output
    print("Starting speed test...")
#    getresults()
    getresults_test()
    print(
        "Starting speed finished (Download: ", download,
        ", Upload: ", upload,
        ", Ping: ", ping, ")")

    # Write to spreadsheet
    print("Writing to spreadsheet...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")


if __name__ == "__main__":
    main()
