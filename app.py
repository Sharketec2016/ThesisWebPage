from gettext import find
from zipfile import is_zipfile
from flask import Flask
import numpy as np
import pandas as pd
from flask import render_template
from PIL import Image
import base64
import io


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/IntroAndTheory")
def intro_and_theory():

    im = Image.open("./figures/introandtheory/PMT_operation.jpg")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())

    return render_template('introandtheory.html', fig1 = encoded_img_data.decode('utf-8'))

@app.route("/Apparatus")
def apparatus():
    return render_template('apparatus.html')

@app.route("/Procedure")
def procedure():
    return render_template('procedure.html')

@app.route("/DataAnalysis")
def data_analysis():
    return render_template('dataAnalysis.html')

@app.route("/Conclusions")
def conclusion():
    return render_template('conclusion.html')

@app.route("/Appendix")
def appendix():
    return render_template('appendix.html')

@app.route("/Citations")
def citations():
    return render_template('citations.html')

if __name__ == '__main__':

    app.run(debug=True, host="0.0.0.0", port=5000)



