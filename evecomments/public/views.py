

from flask import Blueprint, render_template

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/')
def home():
    return render_template('public/home.html')

@blueprint.route('/demo')
def demo():
    return render_template('public/demo.html')