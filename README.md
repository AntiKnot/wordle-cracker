# wordle-crash
- [wordle: a daily world game](https://www.powerlanguage.co.uk/wordle/)
- wordle-crash: guess answer  


## usage
```python
status = {
    "green": 0,
    "yellow": 1,
    "gray": -1
}
```
Build function arguments from responses

```python
reqp = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
```

```shell script
python wordle.py
```

# example
```python
resp1 = {"y": 1, "o": -1, "u": 1, "n": -1, "g": -1}
resp2 = {"f": -1, "i": -1, "r": 1, "e": 1, "d": -1}
```
```txt
query
rebuy
rubye
ruely
ruyle
```

