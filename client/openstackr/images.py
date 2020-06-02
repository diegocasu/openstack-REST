from flask import Blueprint, render_template
from openstackr.util import get_resource

bp = Blueprint('images', __name__, url_prefix='/images')


@bp.route('/')
def index():
    images = get_resource('images')
    return render_template('images/index.html', images=images)
