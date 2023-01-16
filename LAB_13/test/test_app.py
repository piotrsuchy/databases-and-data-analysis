from app import hello, bubblesort
from app import extract_sentiment
from app import text_contain_word
import pytest

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want



testdata = [("I think today will be a great day", True), ("I do not think this will turn out well", False)]

@pytest.mark.parametrize("sample, expected", testdata)
def test_extract_sentiment(sample, expected):

    sentiment = extract_sentiment(sample)

    assert sentiment == expected



testdata = [
    ('There is a duck in this text', 'duck', True),
    ('There is nothing here', 'duck', False),
    ('There is nothing here', 'nothing', True)
    ]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output
    

testdata = [
    ([0, 2, 3, 1, 5, 6, 7, 4, 5, 3], sorted([0, 2, 3, 1, 5, 6, 7, 4, 5, 3])),
    ([-1, 2, -4, -3, 0, 0, -2, 3, 4], sorted([-1, 2, -4, -3, 0, 0, -2, 3, 4])),
    ([1], [1]),
    ([], [])
    ]

@pytest.mark.parametrize('sample, expected_output', testdata)
def test_bubblesort(sample, expected_output):
    
    assert bubblesort(sample) == expected_output