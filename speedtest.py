#!/usr/bin/env python

# Imports
import time
import subprocess
import re
import gdata.spreadsheet.service
import config
from pysed import replace

# Google credentials
email = config.google['email']
password = config.google['password']
spreadsheet_key = config.google['spreadsheet_key']

# All spreadsheets have worksheets. I think worksheet #1 by default always
# has a value of 'od6'
worksheet_id = 'od6'

# Google Spreadsheet connection
spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Upload/Download bandwidth reporter'
spr_client.ProgrammaticLogin()

# Run speedtest and store output
speedtest_result=subprocess.check_output(["/usr/local/bin/speedtest-cli"], stderr=subprocess.STDOUT)

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

# Create dictionary to for the data
dict = {}
dict['date'] = time.strftime('%m/%d/%Y') + " " +  time.strftime('%H:%M:%S')
dict['ping'] = ping
dict['download'] = download
dict['upload'] = upload
print(dict)

# Insert row in spreadsheet
entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
# Check if added successfully
if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
  print("Insert row succeeded.")
else:
  print("Insert row failed.")
