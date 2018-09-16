# PyGramedia
[![Build Status](https://travis-ci.org/Keda87/PyGramedia.svg?branch=master)](https://travis-ci.org/Keda87/PyGramedia)

Unofficial API wrapper for [Gramedia](https://www.gramedia.com/), the biggest bookstore in Indonesia and based on coroutine python 3.

#### Requirement: 
- Python 3.6 and above.

#### Installation:
    pip install pygramedia

#### Usage:

```python
import asyncio
from pygramed import PyGramedia

obj = PyGramedia()

# Async mode based on coroutine.
coro = obj.product.retrieve()
coro = obj.product.retrieve(limit=5)
coro = obj.product.retrieve(limit=10, category='keluarga')

loop = asyncio.get_event_loop()
print(loop.run_until_complete(coro))

# Sync mode like general function.
print(obj.product.retrieve(limit=10, sync=True))
```
