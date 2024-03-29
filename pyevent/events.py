"""Script that hold the main event class"""
from functools import wraps
from .exceptions import *

class Event:
    """Primary Event Class"""
    def __init__(self):
        self._registered_functions:list[function] = []
    
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
    
    def __iadd__(self, other):
        self.register(other)
        return self
    
    def __isub__(self, other):
        self.unregister(other)
        return self
    
    def trigger(self, *args, **kwargs):
        """Calls all registered functions"""
        if len(self._registered_functions) == 0:
            raise NoFunctionsRegistered()
        
        for func in self._registered_functions:
            func(*args, **kwargs)
        
    @property
    def registered_functions(self) -> list:
        """Returns the list of functions registered to this event"""
        return self._registered_functions