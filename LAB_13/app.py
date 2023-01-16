from textblob import TextBlob

def hello(name):
    return "Hello {}".format(name)


def extract_sentiment(text):
    text = TextBlob(text)
    if text.sentiment.polarity > 0:
        return True
    else:
        return False


def text_contain_word(word: str, text: str):
    return word in text


def bubblesort(list_of_numbers: list):
    n = len(list_of_numbers)
    if n == 0:
        return []
    for i in range(n):
        swap_occured = False
        for j in range(0, n-i-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                list_of_numbers[j], list_of_numbers[j+1] = list_of_numbers[j+1], list_of_numbers[j]
                swap_occured = True
        if not swap_occured:
            return list_of_numbers


    