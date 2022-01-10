import shutil


def clean_data(fp):
    """
    Get all words of length 5 from the dictionary and convert to lowercase
    """

    def predicate(word) -> bool:
        return len(word) == 5 + 1 and all(char.isalpha() for char in word[:-1])

    with open(fp) as f:
        words = f.readlines()
    filter_words = [word.lower() for word in words if predicate(word)]
    with open('words-l5.txt', 'w') as f:
        f.writelines(filter_words)
    return True


def init_file():
    """
    There are 6 chances to guess, words-temp.txt holds the intermediate results.
    """
    shutil.copyfile('./words-l5.txt', './words-temp.txt')
    return True


def filter_word(response: dict, fp='./words-temp.txt'):
    """

    status = {
        "green": 0,
        "yellow": 1,
        "gray": -1
    }

    Args:
        fp: ./word-temp.txt
        response: {"w":0,"a":1,"t":-1,"e":1,"r":1}

    Returns:

    """

    for i, (k, v) in enumerate(response.items()):
        with open(fp) as f:
            words = f.readlines()
        if v == 0:
            words = filter(lambda x: x[i] == k, words)
        if v == 1:
            words = filter(lambda x: x[i] != k and k in x, words)
        if v == -1:
            words = filter(lambda x: k not in x, words)
        with open(fp, 'w') as f:
            f.writelines(list(words))
    return True


if __name__ == '__main__':
    clean_data('./words.txt')
    init_file()
    # guess 1
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
    # guess 2
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
    # guess 3
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
    # guess 4
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
    # guess 5
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
    # guess 6
    resp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
    filter_word(resp)
