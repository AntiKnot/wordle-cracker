from typing import List


def load_words(fp) -> List[str]:
    with open(fp) as f:
        words: List[str] = f.readlines()
    return [w.rstrip('\n') for w in words]


def save_words(fp, words) -> bool:
    with open(fp, 'w') as f:
        f.writelines([f"{w}\n" for w in words])
    return True


if __name__ == '__main__':
    import os

    if not os.path.exists('./tmp'):
        os.mkdir('./tmp')
    if os.path.exists('./tmp/test_tmp.txt'):
        os.remove('./tmp/test_tmp.txt')
    assert save_words(fp='./tmp/test_tmp.txt', words=['foo', 'bar']) is True
    assert load_words(fp='./tmp/test_tmp.txt') == ['foo', 'bar']
