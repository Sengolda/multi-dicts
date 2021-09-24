# multi-dicts
A way for dict limits (in a list.)

## use now!
`git clone https://github.com/Sengolda/multi-dicts`

## Make sure the main.py is in the same directory
```py
from main import MultiDicts

m = MultiDicts(per_dict=3)
m.append({"m": 1, "e": 2, "a": 3})
m.sort_dicts() # Sort it.
print(m)
>>> [{"m": 1}, {"e": 2, "a": 3}]
```
