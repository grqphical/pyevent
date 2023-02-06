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
from pyevent.events import Event
import asyncio

event = Event()

# Note all functions added must be coroutines
@event.register
async def test(args, kwargs):
    print(kwargs["message"])
    await asyncio.sleep(1)

# This call the event and runs all coroutines attached to it
# You can pass positional args and keyword arguments to events as well
event.trigger(message="Hello World")
```

## Using Event Groups

If you have many events you want to organize into a single variable you can use event groups
```python
from pyevent.events import Event
from pyevent.event_group import EventGroup
import asyncio

# Create the event and event group
event = Event()
event_group = EventGroup()

# Note all functions added must be coroutines
@event.register
async def test(args, kwargs):
    print("Hello World")
    await asyncio.sleep(1)

# This adds the event to the event group under the name Test
event_group.link_event(event, "Test")

# This will call a specific event
event_group.trigger_event("Test")

# This will call every linked event
event_group.trigger_all()
```