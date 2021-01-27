#!/usr/bin/python3

"""
importamos el objeto Blueprint
"""
from flask import Blueprint

# creamos el objeto blueprint == app_views
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


from api.v1.views.cities import *
from api.v1.views.index import *
