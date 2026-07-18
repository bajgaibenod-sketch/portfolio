from flask import Blueprint, render_template
from .portfolio_data import portfolio

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html", portfolio=portfolio)