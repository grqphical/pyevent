# PyEvent

![Maintainer](https://img.shields.io/badge/maintainer-grqphical07-blue)
[![GitHub license](https://badgen.net/github/license/grqphical07/pyevent)](https://github.com/grqphical07/pyevent/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/grqphical07/pyevent.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/grqphical07/pyevent/stargazers/)

A simple, asynchronous event system made for Python 3

## Installation

1. Download the source code
2. Run ```pip install .``` to install it as a package

## Basic Usage
```python
from pyevent import Event

event = Event()


@event.register
def test(args, kwargs):
    print(kwargs["message"])

# This call the event and runs all functions attached to it
# You can pass positional args and keyword arguments to events as well
event.trigger(message="Hello World")
```

**You also can use += and -= to add/remove events**
```python
from pyevent import Event

event = Event()


def test(args, kwargs):
    print(kwargs["message"])

event += test

# This call the event and runs all functions attached to it
# You can pass positional args and keyword arguments to events as well
event.trigger(message="Hello World")
```
## Async events

PyEvent also works with coroutines. Use the [```AsyncEvent```](/async_event/) class for this functionality
```python
from pyevent import AsyncEvent

event = AsyncEvent()

async def test():
    print("Hello world!")
    await asyncio.sleep(1)

event += test

event.trigger()

```

## Using Event Groups

If you have many events you want to organize into a single variable you can use [```EventGroups```](/event_group/)
```python
from pyevent import Event
from pyevent import EventGroup

# Create the event and event group
event = Event()
event_group = EventGroup()

# Note all functions added must be coroutines
@event.register
def test(*args, **kwargs):
    print("Hello World")

# This adds the event to the event group under the name Test
event_group.link_event(event, "Test")

# This will call a specific event
event_group.trigger_event("Test")

# This will call every linked event
event_group.trigger_all()
```