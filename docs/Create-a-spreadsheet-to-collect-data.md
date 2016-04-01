### Detailed usage

1. Go to the Google Docs dashboard and create a new Spreadsheet using the big green "+" button on the right bottom:  
  ![](http://up.frd.mn/lgMd7.png)
1. Fill in the first four columns `Date`, `Download`, `Upload` and `Ping`:  
  ![](http://up.frd.mn/qS5LU.jpg)
1. Copy the spreadsheet key from the URL into your `config.json`.  
1. Run the `speedtest-to-google` script to make sure it's working:  
  `/usr/local/bin/speedtest-to-google`
1. Yep, it works:  
  ![](http://up.frd.mn/lDStQ.jpg)
1. Setup a cronjob so the speedtest runs automatically:  
  `crontab -e`  

  and insert:

  `*/10 * * * * PATH=$PATH:/usr/local/bin /usr/local/bin/speedtest-to-google`

  Save and quit using Ctrl + X.
1. Now back in the spreadsheet, select the whole columns A - D by clicking on A, then with Shift + Click on D:  
  ![](http://up.frd.mn/7fusF.jpg)
1. Click on "Insert" => "Chart" to create a chart.
1. In the "Start" tab type in, `Sheet1!A:D`:  
  ![](http://up.frd.mn/t8ig1.jpg)
1. In the "Charts" tab select a appropriate line chart type, "line chart" for example:  
  ![](http://up.frd.mn/xHZU8.png)
1. Click on the "Customise" tab for the final adjustments.
1. At the very top, check "Compare mode" in the features:  
  ![](http://up.frd.mn/blDkc.jpg)
1. Scroll down to the "Series" group and select "Ping" in the drop down menu, then set it to "Left axis":  
  ![](http://up.frd.mn/AQbyj.jpg)
1. Finally, click on "Insert" to transfer the chart in your spreadsheet.
1. Now click on the little arrow in the top right corner of the chart and select "Publish chart":  
  ![](http://up.frd.mn/pnOc7.jpg)
1. Hit "Publish" to receive an URL which is publicly available.
