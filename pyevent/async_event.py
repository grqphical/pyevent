"""Primary class for async events"""
from functools import wraps
from .exceptions import *
import asyncio

class AsyncEvent:
    """Primary Async Event Class"""
    def __init__(self):
        self._registered_coroutines:list = []
        self.loop = asyncio.get_event_loop()
    
    def register(self, func):
        """Registers a coroutine to the event"""
        @wraps(func)
        def wrapper():
            if func in self._registered_coroutines:
                raise FunctionAlreadyRegistered("Coroutine has already been added to event")
            self._registered_coroutines.append(func)
        return wrapper()
    
    def unregister(self, func):
        """Unregisters a coroutine to the event"""
        @wraps(func)
        def wrapper():
            try:
                self._registered_coroutines.remove(func)
            except ValueError:
                raise FunctionNotRegistered("Coroutine has not been registered to the event")
        return wrapper()
    
    def __iadd__(self, other):
        self.register(other)
        return self
    
    def __isub__(self, other):
        self.unregister(other)
        return self
    
    async def _trigger(self, *args, **kwargs):
        """Runs the event"""
        tasks = [asyncio.ensure_future(coro(*args, **kwargs)) for coro in self._registered_coroutines]

        if len(tasks) == 0:
            raise NoCoroutinesRegistered()
        await asyncio.wait(tasks)
    
    def trigger(self, *args, **kwargs):
        asyncio.run(self._trigger(*args, **kwargs))
        
    @property
    def registered_coroutines(self) -> list:
        """Returns the list of coroutines registered to this event"""
        return self._registered_coroutines