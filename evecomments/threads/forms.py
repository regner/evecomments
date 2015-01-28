

from flask_wtf          import Form
from wtforms            import StringField
from wtforms.validators import DataRequired, InputRequired, Length


class EditThreadForm(Form):
    """ Form for editing existing threads. """

    title = StringField('Site Name', validators=[DataRequired(), InputRequired(), Length(min=3, max=50)])
    url   = StringField('Site Name', validators=[DataRequired(), InputRequired(), Length(min=3, max=512)])