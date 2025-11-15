import numpy, sympy, flask
from flask import Flask, request, render_template, redirect, url_for
from sympy import Eq, symbols, simplify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def equation_web():
    if 'CD_Eq' in request.form:
        CD_Eq = request.form['CD_Eq']
        return redirect(url_for('CD_val'))

    return render_template('Main_Page.html')

@app.route('/CD_val', methods=['GET','POST'])
def CD_val():
    if request.method == 'POST':
        K_val = request.form('K')
        CDo_val = request.form('CDo')
        CL_val = request.form('CL')

        CD_val = CDo_val + K_val*(CL_val)**2

        outputValue = CD_val

        return render_template('results.html',solutions=outputValue)
    return render_template('CD_val.html')
