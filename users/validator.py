import re

from .views import ValidationError

REGEX_EMAIL    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'

def email_validate(email):
    if not re.match(REGEX_EMAIL, email):
        raise ValidationError("INVALID_EMAIL")

def password_validate(password):
    if not re.match(REGEX_PASSWORD, password):
        raise ValidationError("INVALID_PASSWORD")

