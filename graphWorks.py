import pandas as pd
import matplotlib.pyplot as plt
import base64
import os

def gen_graph_html(csvfilename,columnx,columny):
    os.system("mkdir report")
    df = pd.read_csv(csvfilename)
    x = list(df[columnx])
    y = list(df[columny])

    plt.plot(x,y)
    plt.xlabel(columnx)
    plt.ylabel(columny)

    plt.savefig("report/"+csvfilename+".png",dpi=100)

    def get_base64_encoded_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    img = "report/"+csvfilename+".png"
    encoded = get_base64_encoded_image(img)
    st = '<img class="center" src=\'data:image/png;base64,{}\'>'.format(encoded)
    css = '''
    .center {
          display: block;
          margin-left: auto;
          margin-right: auto;
    }
    body {
        font-family : Calibri
    }
    table {
    border-collapse: collapse;
    }

    th, td {
    text-align: left;
    padding: 8px;
    }

    tr:nth-child(even){background-color: #E6E6FA}

    th {
    background-color: #D2D2D2;
    color: black;
    }'''

    body = f'''<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Aggregate Report</title>
                <style>
            {css}
            </style>
            
            </head>
            <body>
          <h2 align="center">Aggregate Report</h2>
          <table border="1" class="dataframe" align="center">
          <thead>
            <tr style="text-align: right;">
              <th></th>
              <th>Label</th>
              <th># Samples</th>
              <th>Average</th>
              <th>Median</th>
              <th>90% Line</th>
              <th>95% Line</th>
              <th>99% Line</th>
              <th>Min</th>
              <th>Max</th>
              <th>Error %</th>
              <th>Throughput</th>
              <th>Received KB/sec</th>
              <th>Std. Dev.</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th>0</th>
              <td>HTTP Request</td>
              <td>20</td>
              <td>651</td>
              <td>460</td>
              <td>1059</td>
              <td>1711</td>
              <td>2528</td>
              <td>369</td>
              <td>2528</td>
              <td>0.00%</td>
              <td>0.8</td>
              <td>3.7</td>
              <td>530.11</td>
            </tr>
            <tr>
              <th>1</th>
              <td>HTTP Request-0</td>
              <td>20</td>
              <td>493</td>
              <td>343</td>
              <td>947</td>
              <td>1294</td>
              <td>2107</td>
              <td>277</td>
              <td>2107</td>
              <td>0.00%</td>
              <td>0.8</td>
              <td>0.5</td>
              <td>444.46</td>
            </tr>
            <tr>
              <th>2</th>
              <td>HTTP Request-1</td>
              <td>20</td>
              <td>157</td>
              <td>117</td>
              <td>414</td>
              <td>416</td>
              <td>425</td>
              <td>86</td>
              <td>425</td>
              <td>0.00%</td>
              <td>0.8</td>
              <td>3.4</td>
              <td>110.27</td>
            </tr>
            <tr>
              <th>3</th>
              <td>TOTAL</td>
              <td>60</td>
              <td>434</td>
              <td>353</td>
              <td>804</td>
              <td>1294</td>
              <td>2107</td>
              <td>86</td>
              <td>2528</td>
              <td>0.00%</td>
              <td>2.3</td>
              <td>7.4</td>
              <td>453.97</td>
            </tr>
          </tbody>
        </table>
        <br>
        <br>
        <h2 align="center">Graph between {columnx} and {columny}</h2>
        {st}
        </body>
        </html>'''

    file = open(f"report/{csvfilename}.html", "w")
    file.write(body)
    file.close()
    print("Generated")


gen_graph_html("data.csv","Time","HitsPerSecond")
