google-speedtest-chart
======================

Simple Python script to push speedtest results (using `speedtest-cli`) to a Google Docs spreadsheet. I use this to measure and track my upload and download bandwith:

![](http://up.frd.mn/v4TvJ.png)

You can find an interactive demo (actually productive) version of the chart here: https://docs.google.com/spreadsheets/d/1SX2Wl1IIHJpnt89UY9zBPRSzCLEApqmiZJ5x4m6t0Lk/pubchart?oid=1261155623&format=interactive

### Requirements

* Python 2.7
* [`speedtest-cli`](https://github.com/sivel/speedtest-cli)
* A Google account

### Installation

1. Clone repository:  
  `git clone https://github.com/frdmn/google-speedtest-chart.git /opt/google-speedtest-chart`
1. Install dependencies:  
  `pip install pysed gdata speedtest-cli`
1. Copy default config and adjust it:  
  `cp config.example.py config.py`  
  `vi config.py`
1. Symlink it into your `$PATH`:  
  `ln -s /opt/google-speedtest-chart/speedtest.py /usr/local/bin/speedtest-to-google`
1. Run it:  
  `speedtest-to-google`

### Detailed usage

1. Go to Google Docs dashboard and create a new Spreadsheet using the big green "+" button on the bottom right:  
  ![](http://up.frd.mn/lgMd7.png)
1. Use the first three columns and fill in "Date", "Download" and "Upload":  
  ![](http://up.frd.mn/yUfDx.jpg)
1. Copy the spreadsheet key from the URL into your `config.py`.  
1. Run the `speedtest-to-google` script to make sure it's working:  
  `/usr/local/bin/speedtest-to-google`
1. Yep, it works:  
  ![](http://up.frd.mn/pU7WH.jpg)
1. Setup a cronjob so the speedtest runs automatically:  
  `crontab -e`  

  and insert:
  
  `*/10 * * * * /usr/local/bin/speed-to-googledocs`

  Save and quit using Ctrl + X.
1. Now back in the spreadsheet, select the whole columns A - C by clicking on A, then with Shift + Click on B:  
  ![](http://up.frd.mn/Q1m56.png)
1. Click on "Insert" => "Chart" to create a chart.
1. In the "Start" tab type in, "Sheet1!A:C":  
  ![](http://up.frd.mn/g3qxS.png)
1. In the "Charts" tab select a proper line chart type:  
  ![](http://up.frd.mn/xHZU8.png)
1. Click on "Save" to insert the chart in your spreadsheet.
1. Now click on the little arrow in the right top corner of the chart and select "Publish chart":  
  ![](http://up.frd.mn/EnbmU.png)
1. Click on "Publish" to receive a URL that is publicly available.

### Lincense

[WTFPL](LICENSE)

### Version

1.0.0
