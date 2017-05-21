# coding=utf-8

from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

from web_site.user import models, views
