google-speedtest-chart
======================

Simple Python script to push speedtest results (using `speedtest-cli`) to a Google Docs spreadsheet. I use this to measure and track my upload and download bandwith:

[![](http://up.frd.mn/hsoXvzqYw3.png)](https://docs.google.com/spreadsheets/d/e/2PACX-1vSJtguwlM6K4wJtwK842dpTRG46knn0M71A966VRE_9vIcP21s0XMrHXaOwekR2oznM9HE9K344NAsY/pubchart?oid=198771870&format=interactive)

You can find an interactive demo (~~actually productive~~) version of the chart by clicking the image above.

_Note_: If you rather like Grafana than writing to a Google spreadsheet, checkout my new project [`docker-speedtest`](https://github.com/frdmn/docker-speedtest).

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

1. Run the script with default settings (make sure you have a spreadsheet document called "Speedtest"):

    ```
    speedtest-to-google
    ```

    Alternatively you can use the `-w` switch to set a custom spreadsheet name:

    ```
    speedtest-to-google -w Speedtest-document
    ```

    Here are some other arguments that are available:

    ```
    usage: speedtest-charts.py [-h] [-w, --workbookname WORKBOOKNAME] [-b, --bymonth]

    Simple Python script to push speedtest results (using speedtest-cli) to a Google Docs spreadsheet

    optional arguments:
      -h, --help            show this help message and exit
      -w, --workbookname WORKBOOKNAME
                        Sets the woorkbook name, default is "Speedtest"
      -b, --bymonth         Creats a new sheet for each month named MMM YYYY (ex: Jun 2018)
      ```

### License

[MIT](LICENSE)

### Version

1.6.0
