from forex_python.converter import CurrencyRates, CurrencyCodes
from flask import Flask, request, render_template, jsonify, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from decimal import Decimal, ROUND_HALF_UP
app = Flask(__name__)


app.config['SECRET_KEY'] = 'key'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/form')
def render_form():

    return render_template("form.html")


@app.route("/convert")
def convert_currency():
    """Check if word is in dictionary."""
    c = CurrencyRates()
    ccodes = CurrencyCodes()

    cfrom = request.args["currency-from"].upper()
    cto = request.args["currency-to"].upper()
    camnt = request.args["currency-amnt"]
    csymbolfrom = ccodes.get_symbol(cfrom)
    csymbolto = ccodes.get_symbol(cto)


    if not camnt.isnumeric():
        flash(f'Not a Valid Amount', 'danger')
        return redirect(f"/form")

    try:
        conversion = c.convert(cfrom, cto, Decimal(camnt))
    except:
        flash(f'Not a Valid Country Code', 'danger')
        return redirect(f"/form")

    result = conversion.quantize(Decimal(".01"), rounding=ROUND_HALF_UP)

    return render_template('form.html', camnt=camnt, result=result, csymbolfrom=csymbolfrom, csymbolto=csymbolto)
