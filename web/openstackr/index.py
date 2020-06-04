from flask import Blueprint, redirect, url_for

bp = Blueprint('index', __name__, url_prefix='')

@bp.route('/')
def index():
    return redirect(url_for('schedules.index'))

