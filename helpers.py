from flask import redirect, session
from functools import wraps


def check_password(password):
    """Check if string is eligible to be a password, return True or False"""

    # Set result to return
    result = False

    # Create a list of special symbols
    SYMBOLS = ["@", "#", "$", "%", "&","-", "_", "/"]

    # Check password length
    if not 8 <= len(password) <= 16:
        return result

    # Check if password has at least one of each uppercase or lowercase letter
    elif not any(char.isupper() for char  in password) and  not any(char.islower() for char in password):
        return result

    #Check is password has at least one special symbol
    elif not any(char in SYMBOLS for char in password):
        return result

    # Return True if password is eligible
    else:
        result = True
        return result


def login_required(f):
    """Decorate routes to require login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function