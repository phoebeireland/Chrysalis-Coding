from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=15)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=12)])
    password_confirm = PasswordField('Confirm Password', validators=[
        DataRequired(), EqualTo('password', message='Passwords must be the same.')
    ])
    submit = SubmitField('Register')


class CreatePost(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    inspirational_quote = StringField('Inspirational Quote')
    submit = SubmitField('Post')


class EditPost(FlaskForm):
    title = StringField('Title')
    content = TextAreaField('Content')
    inspirational_quote = StringField('Inspirational Quote')
    submit = SubmitField('Update')


class DeletePost(FlaskForm):
    username = StringField('username')
    submit = SubmitField('Delete')