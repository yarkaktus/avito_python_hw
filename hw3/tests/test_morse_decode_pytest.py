import pytest

from hw3.morse import decode


@pytest.mark.parametrize(
    "morse_code, decoded_text",
    [("... --- ...", "SOS"), (".- .- .- .-", "AAAA"), (".... . .-.. .--.", "HELP"), ],
)
def test_decode_simple_cases(morse_code: str, decoded_text: str):
    assert decode(morse_code) == decoded_text


@pytest.mark.parametrize("morse_code", ["=", "Ь", "Â", ])
def test_exception(morse_code: str):
    with pytest.raises(KeyError):
        decode(morse_code)


def test_empty_string():
    assert decode("") == ""


@pytest.mark.parametrize(
    "morse_code, decoded_text",
    [(".....", "5"), (".---- ----- ----- -----", "1000"), ("----. ----.", "99"), ],
)
def test_numbers_cases(morse_code: str, decoded_text: str):
    assert decode(morse_code) == decoded_text
