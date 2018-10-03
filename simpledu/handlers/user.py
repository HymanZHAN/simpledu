from flask import Blueprint, render_template
from simpledu.models import User

user = Blueprint('user', __name__, url_prefix='/user')

# @user.route('/')
# def user_index():
#     users = User.query.all()

@user.route('/<string:username>')
def user_detail(username):
    users = User.query.all()
    for user in users:
        if user.username == username:
            return render_template('user.html', user=user)
        else:
            return '404 Not Found'