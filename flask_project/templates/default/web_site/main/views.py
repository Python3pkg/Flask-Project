# coding=utf-8

from flask import render_template
from flask.ext.login import login_required
from . import main_blueprint as bp


@bp.route('/')
@login_required
def index():
    return render_template('index.html')
