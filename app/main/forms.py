from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class CommentsForm(FlaskForm):
    comment =TextAreaField('comment',validators=[(Required)])
    # <i class="fa fa-trash" aria-hidden="true"></i>
    submit = SelectField

class UpdateFrofile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.', validators=[(Required)])
    submit =SubmitField('Submit')

class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('1', 'Interview'), ('2', 'Pick Up Lines'), ('3', 'Promotion'),('4','Product')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

class UpvoteForm(FlaskForm):
    '''
    Class to create a wtf form for upvoting a pitch
    '''
    submit = SubmitField('Upvote')
