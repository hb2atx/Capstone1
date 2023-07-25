from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, EqualTo, InputRequired, ValidationError



class LoginForm(FlaskForm):

    username = StringField('Email', validators=[InputRequired(), Length(4, 20), Email()])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20)])
    submit = SubmitField('Log In')

    


class RegisterForm(FlaskForm):

        username = StringField("Username", validators=[InputRequired(), Length(min=4, max=20)])
        email = StringField("Email Address", validators=[InputRequired(), Length(4, 20), Email()])
        password = PasswordField("New Password", validators=[InputRequired(), Length(1, 32)])
        confirm = PasswordField('Verify Password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])
        submit = SubmitField('Register')

        # def validate_username(self, username):
        #       existing_user_username = User.query.filter_by(username=username.data).first()

        #       if existing_user_username:
        #             raise ValidationError("That username already exists. Please choose a different one")
              
    
                    

    

      
      
   









    