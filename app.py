from flask import Flask
import numpy as np
import pandas as pd
from flask import render_template



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/IntroAndTheory")
def intro_and_theory():
    return render_template('introandtheory.html')

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


if __name__ == '__main__':
    app.run(debug=True, port=80)
