import pandas as pd
import matplotlib.pyplot as plt
import base64
import os


def gen_graph_html(csvfile, columnx, columny):
    df = pd.read_csv(csvfile)
    x = list(df[columnx])
    y = list(df[columny])

    plt.plot(x, y)
    plt.xlabel(columnx)
    plt.ylabel(columny)
    os.system("mkdir report")
    plt.savefig("report/" + csvfile + ".png", dpi=100)

    def get_base64_encoded_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    img = "report/" + csvfile + ".png"
    encoded = get_base64_encoded_image(img)
    st = '<img class="center" src=\'data:image/png;base64,{}\'>'.format(encoded)
    css = '''
    .center {
          display: block;
          margin-left: auto;
          margin-right: auto;
    }
   '''

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
        <h2 align="center">Graph between {columnx} and {columny}</h2>
        {st}
        </body>
        </html>'''

    file = open(f"report/{csvfile}.html", "w")
    file.write(body)
    file.close()
    print("Generated")


# REPLACE WITH YOUR FILENAME AND COLUMN NAMES
gen_graph_html("data.csv", "x", "y")
