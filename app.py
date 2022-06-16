from ast import Compare
from flask import Flask
import numpy as np
import pandas as pd
from flask import render_template
from PIL import Image
import base64
import io


def grab_image(path):
    im = Image.open(f"./figures/{path}")
    data = io.BytesIO()
    im.save(data, "JPEG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data

def grab_png(path):
    im = Image.open(f"./figures/{path}")
    data = io.BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())
    return encoded_img_data


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/IntroAndTheory")
def intro_and_theory():

    PMT_operation = grab_image("introandtheory/PMT_operation.jpg")
    quantum_eff = grab_png("introandtheory/quantum_eff.png")
    voltage_divider = grab_png("introandtheory/voltage_divider_circuit_sebastian.png")
    noisy_pmt = grab_png("introandtheory/noisy_pmt_signal.png")

    return render_template('introandtheory.html', fig1 = PMT_operation.decode('utf-8'), fig2 = quantum_eff.decode('utf-8'), fig3 = voltage_divider.decode('utf-8'), fig4 = noisy_pmt.decode('utf-8'))

@app.route("/Apparatus")
def apparatus():

    pmts = grab_image("apparatus/PMTs.jpg")
    ortec = grab_png("apparatus/ortec_preamp.png")
    amp = grab_image("apparatus/amplifier.jpg")
    pico = grab_image("apparatus/picoscope.jpg")
    pulse = grab_png("apparatus/pulse_gen.png")



    return render_template('apparatus.html', pmts=pmts.decode('utf-8'), ortec=ortec.decode('utf-8'), amp = amp.decode('utf-8'), pico=pico.decode('utf-8'), pulse=pulse.decode('utf-8'))

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



