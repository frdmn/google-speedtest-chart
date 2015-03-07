#!/usr/bin/python

import time
import subprocess
import re
import gdata.spreadsheet.service
from pysed import replace

email = 'your.address@gmail.com'
password = '12345abcde'

# You can find the key in the spreadsheet URL:
# https://docs.google.com/spreadsheets/d/XXX
# => XXX is the key, copy and paste below
spreadsheet_key = 'XXX'

# All spreadsheets have worksheets. I think worksheet #1 by default always
# has a value of 'od6'
worksheet_id = 'od6'

spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Upload/Download bandwidth reporter'
spr_client.ProgrammaticLogin()

speedtest_result=subprocess.check_output(["/usr/local/bin/speedtest-cli"], stderr=subprocess.STDOUT)

download = re.findall(r'Download: [0-9\.]* .bit', speedtest_result, re.MULTILINE)[0]
download = replace(download, "Download: ", "")
download = replace(download, ".bit", "")

upload = re.findall(r'Upload: [0-9\.]* .bit', speedtest_result, re.MULTILINE)[0]
upload = replace(upload, "Upload: ", "")
upload = replace(upload, ".bit", "")

# Prepare the dictionary to write
dict = {}
dict['date'] = time.strftime('%m/%d/%Y') + " " +  time.strftime('%H:%M:%S')
dict['upload'] = upload
dict['download'] = download
print(dict)

entry = spr_client.InsertRow(dict, spreadsheet_key, worksheet_id)
if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
  print("Insert row succeeded.")
else:
  print("Insert row failed.")
