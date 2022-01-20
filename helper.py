from typing import List

from pypinyin import lazy_pinyin
from pypinyin import pinyin


class ChengYu:
    def __init__(self, chengyu, pinyin, code):
        self.chengyu = chengyu
        self.pinyin = pinyin
        self.code = code

    def to_string(self):
        res = " ".join([self.chengyu, self.pinyin, self.code])
        res += "\n"
        return res


def word2pinyin(word):
    # pinyin("拼音") -> [["pin"],["yin"]]
    lst_py = [l for l in lazy_pinyin(word)]
    str_py = ",".join(lst_py)
    lst_code = [len(item) for item in lst_py]
    str_code = "".join([str(item) for item in lst_code])
    cy = ChengYu(chengyu=word, pinyin=str_py, code=str_code)
    return cy


def words2pinyin(words: List[str]) -> List[ChengYu]:
    res = [word2pinyin(word.strip("\n")) for word in words]
    return res
