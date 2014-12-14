

from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired, Length, InputRequired


class AddCommentForm(Form):
    """ Form for adding comments. """
    message = TextAreaField('Message', validators=[DataRequired(), InputRequired(), Length(min=5, max=512)])