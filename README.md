# Enumerable
Enumerable is a python library that re-implements a few core features of python's functional toolbox to be more flexible and support a more transactional way of solving problems.  By design, these tools support method chaining and lazy evaluation.

# Installation
Installation is simple via pip.

`pip install enumerable`
# Examples of use

A common thing we do in python, especially in the IT world is for data processing.  Let's say you want to load a log file and filter for specific events and strip off the line endings for further processing:

```python
import re
from enumerable import *
from operator import methodcaller

with open("log.txt", 'r') as log:
    def critical(log_line):
        return re.search("^CRITICAL:", log_line)

    results = filter(log, critical).map(methodcaller('strip'))

for line in results:
    <do something>
```

Map, Fold, and Reduce are currently provided and they are all lazy evaluated and support method chaining.

```python
>>> import operator
>>> from enumerable import *
>>>
>>> my_list = [1, 2, 3, 4, 5]
>>> # Notice that any additional arguments passed to map/filter/reduce
... # are then passed to the provided function.
... map(my_list, operator.pow, 2).to(tuple)
(1, 4, 9, 16, 25)
>>>
```
