from flask import abort
from flask_login import current_user
from functools import wraps
from simpledu.models import User


def role_required(role):
    '''
    Decorator that ensures that a function can only be accessed by certain role.
    Example:
        @role_required(User.ADMIN)
        def admin():
            pass
    '''

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Invoke 404 when level of user authentication is not met.
            if not current_user.is_authenticated or current_user.role < role:
                abort(404)
            return func(*args, **kwargs)
        return wrapper
    return decorator


staff_required = role_required(User.ROLE_STAFF)
admin_required = role_required(User.ROLE_ADMIN)
