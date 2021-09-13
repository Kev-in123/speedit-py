# speedit.py

This package allows you to test the speed of a function

## Installation

Stable version:

```
pip install speedit-py
```

Development version:

```
pip install git+https://github.com/Kev-in123/speedit-py
```

## Example Usage

```python
from speedit import speed

@speed
def hi_there():
  print("hi there")

hi_there()

@speed
def hello_there(msg):
  print(msg)

hello_there("hello there")
```