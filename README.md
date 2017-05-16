google-speedtest-chart
======================

Simple Python script to push speedtest results (using `speedtest-cli`) to a Google Docs spreadsheet. I use this to measure and track my upload and download bandwith:

[![](http://up.frd.mn/xRiew.png)](https://docs.google.com/spreadsheets/d/1QvV6POBVBXuq5iXSOLNd5bwgd5To8FMuvsrSfvY7Nuk/pubchart?oid=1973311741&format=interactive)

You can find an interactive demo (~~actually productive~~) version of the chart by clicking the image above.

### Requirements

* Google account
* Python 3.X
* [`speedtest-cli`](https://github.com/sivel/speedtest-cli)
* [`pygsheets`](https://github.com/nithinmurali/pygsheets)

### Installation and usage

1. Clone and open repository:

    ```
    git clone https://github.com/frdmn/google-speedtest-chart.git
    cd google-speedtest-chart
    ```

1. Install dependencies:

    ```
    pip install -r requirements.txt
    ```


1. Symlink it into your `$PATH`:

    ```
    ln -s speedtest-charts.py /usr/local/bin/speedtest-to-google
    ```

1. Authorization
    
    1. :book: [Authorize pygsheets](https://pygsheets.readthedocs.io/en/latest/authorizing.html#authorizing-pygsheets)
    1. :book: [Create an OAuth token](https://pygsheets.readthedocs.io/en/latest/authorizing.html#oauth-credentials), download the credential file and and store it as `credentials.json`

1. Create a spreadsheet dedicated to collect your speedtest results:  

    :book: [docs/Create-a-spreadsheet-to-collect-data.md](docs/Create-a-spreadsheet-to-collect-data.md)

1. Run the script, you can pass a custom spreadsheet name by setting `SPREADSHEET` environment variable:

    ```
    SPREADSHEET="Speedtest-document" speedtest-to-google
    ```

### License

[MIT](LICENSE)

### Version

1.4.0
