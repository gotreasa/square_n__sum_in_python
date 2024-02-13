import pytest
from modules import square_number_sum


def describe_square_sum():
    def should_error_when_input_not_array(capsys):
        """🧪 should error when the input is not an array"""
        with pytest.raises(ValueError, match="❗️ Input should be an array"):
            square_number_sum.square_sum("blah")
