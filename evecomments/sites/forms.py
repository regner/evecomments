

from flask_wtf import Form
from wtforms   import StringField
from wtforms.validators import DataRequired, InputRequired, Length


class AddSiteForm(Form):
    """ Form for adding new sites to the comments system. """

    name = StringField('Site Name', validators=[DataRequired(), InputRequired(), Length(min=3, max=50)])