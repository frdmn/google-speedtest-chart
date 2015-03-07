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

### Lincense

[WTFPL](LICENSE)

### Version

1.0.0
