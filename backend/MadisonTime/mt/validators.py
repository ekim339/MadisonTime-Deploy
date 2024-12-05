import string
from django.core.exceptions import ValidationError


def contains_special_character(value):
    for char in value:
        # string.punctuation: string of special characters
        # iterates over value and check if it is a special character
        if char in string.punctuation:
            return True
    return False



def contains_uppercase_letter(value):
    if any(char for char in value if char.isupper()): return True
    # for char in value:
    #     if char.isupper():
    #         return True
    return False



def contains_lowercase_letter(value):
    if any(char for char in value if char.islower()): return True
    # for char in value:
    #   if char.islower():
    #     return True
    return False



def contains_number(value):
    if any(char for char in value if char.isdigit()): return True
    # for char in value:
    #     if char.isdigit():
    #         return True
    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
                len(password) < 8 or
                not contains_uppercase_letter(password) or
                not contains_lowercase_letter(password) or
                not contains_number(password) or
                not contains_special_character(password)
        ):
            raise ValidationError("Password must be at least 8 chracters that are a combination of uppercase letter, lowercase letter, numbers and special characters.")

    def get_help_text(self):
        return "Enter at least 8 characters that are a combination of uppercase letter, lowercase letter, numbers and special characters."
        

def validate_no_special_characters(value):
    if contains_special_character(value):
        raise ValidationError("Cannot contain special characters.")
    
def validate_time_from(time_from):
    if time_from.hour < 6:
        raise ValidationError("Start time must be between 6:00AM-11:59PM.")

def validate_time_to(time_to):
    if 1 < time_to.hour and time_to.hour < 5:
        raise ValidationError("End time must be between 6:01AM-12:00AM.")
    else:
        if time_to.hour == 0 and time_to.minute != 0:
            raise ValidationError("End time must be between 6:01AM-12:00AM")
        elif time_to.hour == 6 and time_to.minute == 0:
            raise ValidationError("End time must be between 6:01AM-12:00AM")
        
