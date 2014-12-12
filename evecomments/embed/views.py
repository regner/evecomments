

from flask import Blueprint, render_template

blueprint = Blueprint('embed', __name__, static_folder='../static')


@blueprint.route('/embed/<int:site_id>/embed', methods=('GET', ))
def embed(site_id):
    template_values = {
        'site_id'  : site_id,
    }

    return render_template('embed/embed.html')