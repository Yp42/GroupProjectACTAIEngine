import main
import os

from flask import Flask

app = Flask(__name__)


@app.route("/stock=<stock>")
def get_response(stock):
    stock = str(stock)
    stock = stock.lower()

    try:
        reportExists = os.path.exists(f"../../reports/{stock}.md")
    except:
        print("No pre-existing report")

    if not reportExists:
        main.run(stock)
        os.rename("report.md", f"../../reports/{stock}.md")

    file = open(f"../../reports/{stock}.md")
    response = file.read()

    return {"input": stock, "response": response}


app.run()
