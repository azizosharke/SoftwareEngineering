from flask import Blueprint, render_template

login_bp = Blueprint("login", __name__, url_prefix="/")

@login_bp.route("/")
def login():
    error=""
    return render_template("login.html",error=error)