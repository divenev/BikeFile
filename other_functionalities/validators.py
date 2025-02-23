from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinRequirementChars:
    min_string_length = 2
    validator_message = 'Below the minimum number of characters.'

    def __init__(self, min_string_length=None, validator_message=None):
        if self.min_string_length is not None:
            self.min_string_length = min_string_length
        if self.validator_message is not None:
            self.validator_message = validator_message

    def __call__(self, value):
        if len(value) < self.min_string_length:
            raise ValidationError(self.validator_message)
