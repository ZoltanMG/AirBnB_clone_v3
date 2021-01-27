#!/usr/bin/python3

from api.v1.views import app_views


@app_views.route("/status", methods=["GET"])
def index():
    """
    return the status of the api
    """
    return {
        "status": "OK"
    }
