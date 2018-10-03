from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, Email, EqualTo, DataRequired, URL, NumberRange
from simpledu.models import User, db, Course


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(3, 24, message='Username should be 3 ~ 24 characters long.')])
    email = StringField('Email', validators=[
        DataRequired(), Email(message='Please enter a valid email address.')])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(6, 24, message='Password should be 6 ~ 24 characters long.')])
    repeat_password = PasswordField('Repeat Password', validators=[
        DataRequired(), Length(6, 24), EqualTo('password', message='The two passwords don\'t match.')])
    submit = SubmitField('Submit')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already exists.')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already exists.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(6, 24)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('Email not registered.')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Wrong password.')


class CourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired(), Length(5, 64)])
    description = TextAreaField('Course Description', validators=[DataRequired(), Length(20, 512)])
    image_url = StringField('Thumbnail URL', validators=[DataRequired(), URL()])
    author_id = IntegerField('Author ID', validators=[DataRequired(), NumberRange(min=1, message='Invalid User ID')])
    submit = SubmitField('Submit')

    def validate_author_id(self, field):
        if not User.query.get(self.author_id.data):
            raise ValidationError('User does not exist')

    def create_course(self):
        course=Course()
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course

    def update_course(self, course):
        self.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return course
