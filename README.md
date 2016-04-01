google-speedtest-chart
======================

Simple Python script to push speedtest results (using `speedtest-cli`) to a Google Docs spreadsheet. I use this to measure and track my upload and download bandwith:

![](http://up.frd.mn/xRiew.png)

You can find an interactive demo (actually productive) version of the chart here: https://docs.google.com/spreadsheets/d/1QvV6POBVBXuq5iXSOLNd5bwgd5To8FMuvsrSfvY7Nuk/pubchart?oid=1973311741&format=interactive

### Requirements

* Python 2.6
* [`speedtest-cli`](https://github.com/sivel/speedtest-cli)
* Google account

### Installation and usage

1. Clone and open repository:  
  `git clone https://github.com/frdmn/google-speedtest-chart.git && cd google-speedtest-chart`
1. Install dependencies:  
  `pip install gdata speedtest-cli google-api-python-client`
1. Copy default config and adjust it:  
  `cp default.config.json config.json`
1. Symlink it into your `$PATH`:  
  `ln -s speedtest.py /usr/local/bin/speedtest-to-google`
1. Create an OAuth token using the tutorial in the wiki:  
  :book: [docs/How-to-create-a-Google-OAuth-token.md](docs/How-to-create-a-Google-OAuth-token.md)
1. Create a spreadsheet dedicated to collect your speedtest results:  
  :book: [docs/Create-a-spreadsheet-to-collect-data.md](docs/Create-a-spreadsheet-to-collect-data.md) and make sure to adjust `spreadsheet_id` in the `config.json` file
1. Run the script:  
  `$ speedtest-to-google`

### License

[MIT](LICENSE)

### Version

1.3.0
