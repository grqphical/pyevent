"""Script that hold the main event class"""
from functools import wraps
from .exceptions import *
import asyncio

class Event:
    """Primary Event Class"""
    def __init__(self):
        self._registered_functions:list[function] = []
        self.loop = asyncio.get_event_loop()
    
    def register(self, func):
        """Registers a function to the event"""
        @wraps(func)
        def wrapper():
            if func in self._registered_functions:
                raise FunctionAlreadyRegistered("Function has already been added to event")
            self._registered_functions.append(func)
        return wrapper()
    
    def unregister(self, func):
        """Unregisters a function to the event"""
        @wraps(func)
        def wrapper():
            try:
                self._registered_functions.remove(func)
            except ValueError:
                raise FunctionNotRegistered("Function has not been registered to the event")
        return wrapper()
    
    async def _trigger(self, args, kwargs):
        """Runs the event"""
        tasks = [asyncio.ensure_future(coro(args, kwargs)) for coro in self._registered_functions]
        await asyncio.wait(tasks)
    
    def trigger(self, *args, **kwargs):
        asyncio.run(self._trigger(args, kwargs))
        
    @property
    def registered_functions(self) -> list:
        """Returns the list of functions registered to this event"""
        return self._registered_functions