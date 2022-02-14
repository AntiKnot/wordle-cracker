import shutil
from typing import List

from helper import ChengYu
from helper import words2pinyin
from utils import load_words


def init_data(
        fp_src="chengyu-l4.txt",
        fp_dst="chengyu-pinyin-l4.txt"
) -> List[ChengYu]:
    with open(fp_src) as f:
        words = f.readlines()
    lst_chengyu = words2pinyin(words)
    with open(fp_dst, 'w') as f:
        f.writelines([cy.to_string() for cy in lst_chengyu])
    return lst_chengyu


def init_file():
    shutil.copyfile('./chengyu-pinyin-l4.txt', './chengyu-pinyin-temp.txt')
    return True


def load_chengyu_pinyin(fp="chengyu-pinyin-temp.txt"):
    words: List[str] = load_words(fp)
    lst_cy = []
    for word in words:
        word, pinyin, code = word.split(" ")
        cy = ChengYu(word, pinyin, code)
        lst_cy.append(cy)
    return lst_cy


def save_chengyu_pinyin(lst_cy, fp="chengyu-pinyin-temp.txt"):
    with open(fp, 'w') as f:
        f.writelines([cy.to_string() for cy in lst_cy])


def filter_chengyu_pinyin(response: List[tuple], fp="chengyu-pinyin-temp.txt"):
    words = load_chengyu_pinyin(fp)
    for i, (k, v) in enumerate(response):
        if v == 0:
            res = []
            for word in words:
                assert isinstance(word, ChengYu)
                py = word.pinyin
                py = py.replace(',', '')
                print(py)
                if py[i] == k:
                    res.append(word)
            words = res
        if v == 1:
            res = []
            for word in words:
                assert isinstance(word, ChengYu)
                py = word.pinyin
                py = py.replace(',', '')
                if py[i] != k:
                    res.append(word)
            words = res
        if v == -1:
            res = []
            for word in words:
                assert isinstance(word, ChengYu)
                py = word.pinyin
                py = py.replace(',', '')
                if k not in py:
                    res.append(word)
            words = res
        save_chengyu_pinyin(words)
    return True


def struct_filter(fmt, lst_cy) -> List[ChengYu]:
    def predicate(cy: ChengYu):
        return cy.code == fmt

    return list(filter(predicate, lst_cy))


def filter_word(response: dict, fp='./words-temp.txt'):
    """

    status = {
        "green": 0,
        "yellow": 1,
        "gray": -1
    }

    Args:
        fp: ./chengyu-temp.txt
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
            f.writelines(sorted(list(words), key=lambda x: -len(set(x))))
    return True


if __name__ == '__main__':
    # init_data()
    init_file()
    lst_cy = load_chengyu_pinyin()
    lst_cy = struct_filter("3323", lst_cy)
    save_chengyu_pinyin(lst_cy)
    filter_chengyu_pinyin(
        [
            ("y", -1), ("o", -1), ("u", -1),
            ("s", -1), ("h", 1), ("i", 1),
            ("y", -1), ("i", -1),
            ("l", -1), ("a", 1), ("i", 0)
        ])
