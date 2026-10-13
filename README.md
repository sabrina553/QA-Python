# QA-Python

Exercises from the Python module of the QA Software Development Bootcamp, kept as they were written while learning.

## Contents

| Path | What it is |
| --- | --- |
| `practise/1.py` to `11.py` | Course exercises: input and output, conditionals, loops, functions, classes, abstract base classes, file I/O |
| `practise/dice/` | Splitting code across modules (`import dice`) |
| `practise/pytesting/` | First unit tests with `pytest` and `pytest-cov` |
| `ISBN.py` | Calculates the 13th (check) digit of an ISBN-13 |
| `NumtoWord.py` | Turns a number string into words, e.g. `1024` → "One Thousand, Twenty Four" |
| `debug.py` | A deliberately broken script for practising with `pdb`; it is meant to fail |
| `beepboop.py` | Prints a dot per million up to an input number |
| `word conjugation/splitter.py` | An unfinished experiment with a dictionary word list |

## Running it

```bash
python3 ISBN.py                  # prints 7, the check digit for 978-0-306-40615-?
cd practise/pytesting && python3 -m pytest count_test.py --cov
```

`splitter.py` expects `words_alpha.txt` from [dwyl/english-words](https://github.com/dwyl/english-words) next to it. The list used to be committed (about 20 MB) and is now left out; download it if you want to run the script.

## What I learnt

- Testing early: `pytest` with coverage made it obvious which branches of a function I had never run.
- `NumtoWord.py` was my first real fight with string slicing, and with a global variable shared between functions, which is why it is hard to follow.
- Classes and inheritance, including abstract methods with `abc`.

## What I would do better

- `NumtoWord.py` works, but prints stray double spaces ("Twenty "), and the expected outputs in its comments are out of date. I would rewrite it to return a string instead of printing, drop the global, and turn those examples into tests.
- Use `with open(...)` everywhere so files are always closed.
- Name files after what they do instead of `1.py` to `11.py`.
- Do not commit generated files (`__pycache__`, `.coverage`) or large third-party data; a `.gitignore` now covers these.
