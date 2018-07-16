#!/usr/bin/env python3

import datetime
import pygsheets
import speedtest
import argparse

# Set options
parser = argparse.ArgumentParser(
    description='Simple Python script to push speedtest results \
                (using speedtest-cli) to a Google Docs spreadsheet'
)
parser.add_argument(
    "-w, --workbookname", action="store", default="Speedtest", type=str,
    dest="workbookname",
    help='Sets the woorkbook name, default is "Speedtest"'
)
parser.add_argument(
    "-s, --sheetname", action="store", default="Sheet1", type=str,
    dest="sheetname",
    help='Sets the sheet name if "bymonth" not set, default is "sheet1"'
)
parser.add_argument(
    "-b, --bymonth", action="store_true", default=False,
    dest="bymonth",
    help='Creats a new sheet for each month named MMM YYYY (ex: Jun 2018)'
)

cliarg = parser.parse_args()

# Set constants
DATE = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
header = [['A1', 'B1', 'C1', 'D1'], ['Date', 'Download', 'Upload', 'Ping']]

if cliarg.bymonth:
    sheetname = datetime.datetime.now().strftime("%b %Y")

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
        speedtest = gc.open(cliarg.workbookname)
    except pygsheets.SpreadsheetNotFound:
        speedtest = gc.create(cliarg.workbookname)

    if cliarg.bymonth:
        try:
            sheet = speedtest.worksheet('title', sheetname)
        except pygsheets.WorksheetNotFound:
            sheet = speedtest.add_worksheet(sheetname)
    else:
        sheet = speedtest.sheet1

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
    download = round(spdtest.download() / 1000 / 1000, 2)
    upload = round(spdtest.upload() / 1000 / 1000, 2)
    ping = round(spdtest.results.ping)

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
