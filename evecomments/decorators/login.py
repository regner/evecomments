

from functools import wraps

from flask           import current_app, request
from flask.ext.login import current_user


def login_required_for_post(func):
    """ Almost identical to the default Flask-Login login_required decorator
    except that it only checks the authentication if the request is a POST request.
    """

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if current_app.login_manager._login_disabled:
            return func(*args, **kwargs)

        elif request.method == 'POST' and not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()

        return func(*args, **kwargs)
    return decorated_view