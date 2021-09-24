# multi-dicts
A way for dict limits (in a list.)

## use now!
`git clone https://github.com/Sengolda/multi-dicts`

## Make sure the main.py is in the same directory
```py
from main import MuliDicts 

m = MuliDicts(per_dict=2)
m.append({"a": 1, "e": 2})
m.sort_dicts() # Sort it.
print(m)
>>> [{"a": 1}, {"e": 2}]
```
