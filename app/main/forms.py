from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators = [Required()])
    review = TextAreaField('Hostel review')
    submit = SubmitField('Submit')