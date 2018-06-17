#!/usr/bin/env python3

import os
import datetime
import pygsheets
import speedtest

# Set options
bymonth = False

# Set constants
DATE = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
sheetname = datetime.datetime.now().strftime("%b %Y")
header = [['A1', 'B1', 'C1', 'D1'], ['Date', 'Download', 'Upload', 'Ping']]
workbookname = os.getenv('SPREADSHEET', 'Speedtest')

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

        headnew = str(sheet.cell('A1').value)
        headcur = str(header[1][0])

        if headnew != headcur:
            # create header row
            for index in range(len(header[0])):
                head = sheet.cell(header[0][index])
                head.value = header[1][index]
                head.update()

    data = [DATE, download, upload, ping]

    sheet.append_table(values=data)


def getresults():
    """Function to generate speedtest result."""
    spdtest = speedtest.Speedtest()
    spdtest.get_best_server()
<<<<<<< HEAD
    
    download = round(spdtest.download() / 1000 / 1000, 2)
    upload = round(spdtest.upload() / 1000 / 1000, 2)
    ping = round(spdtest.results.ping)

    print("Starting speed finished (Download: ", download, ", Upload: ", upload, ", Ping: ", ping, ")")
=======
    download = spdtest.download()
    upload = spdtest.upload()
    ping = spdtest.results.ping

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
    download, upload, ping = getresults()
    print("Starting speed finished!")
>>>>>>> Removed unused modules

    # Write to spreadsheet
    print("Writing to spreadsheet...")
    submit_into_spreadsheet(download, upload, ping)
    print("Successfuly written to spreadsheet!")


if __name__ == "__main__":
    main()
