### Step 1: Turn on the Drive API

1. Use [this wizard](https://console.developers.google.com/start/api?id=drive) to create or select a project in the Google Developers Console and automatically turn on the API. Click the __Go to credentials__ button to continue.
2. At the top of the page, select the __OAuth consent screen__ tab. Select an __Email address__, enter a __Product name__ if not already set, and click the __Save__ button:  
  ![](http://up.frd.mn/cCML4.png)
3. Back on the __Credentials__ tab, click the __Add credentials__ button and select __OAuth 2.0 client ID__.
4. Select the application type __Other__, type in "Python Speedtest" as name and click the __Create__ button:  
  ![](http://up.frd.mn/BZu5V.png)
5. Click __OK__ to dismiss the resulting dialog.
6. Click the "__Download__" to the right of the client ID to download the JSON file that contains the secret key.
7. Move this file to your project directory and rename it `secret.json`.

### Step 2: Set up project and dependencies

1. Check the `README.md` and follow the installation instructions.
2. Make sure to install all "pip" dependencies.

### Step 3: Obtain OAuth tokens for client

1. Make sure you've installed the `secret.json` as described in step 1.
2. Run the script to establish OAuth authorization:  
  `$ ./speedtest.py`
3. Wait for the new browser window to open, make sure to log into your Google account and grant access to our `speedtest` script.
4. In case you run the "google-speedtest-chart" on a machine without GUI or browser support, run the following on a machine with GUI:  
  `$ ./speedtest.py --noauth_local_webserver`
5. ... and copy and paste the URL from the command line to your browser, perform the authorization to Google Drive and paste the access key back in your command line.
