from flask import Blueprint

homeapi = Blueprint('homeapi', __name__)

@homeapi.route("/account")
def accountList():
    return "This is list of accounts"

