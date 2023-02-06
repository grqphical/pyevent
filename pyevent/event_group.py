"""Script for handling event groups"""
from .events import Event
from .exceptions import *

class EventGroup:
    def __init__(self):
        self.linked_events:dict[str, Event] = {}
    
    def link_event(self, event:Event, name:str):
        """Links an event to the event group"""
        if name in self.linked_events.keys():
            raise EventAlreadyRegistered("Event already in Event Group")
        self.linked_events[name] = event
    
    def unlink_event(self, name:str):
        """Unlinks an event from the event group"""
        if name not in self.linked_events.keys():
            raise EventNotRegistered(f"No event with name '{name}' linked")
        del self.linked_events[name]
    
    def trigger_event(self, name:str, *args, **kwargs):
        """Triggers an event in the event group based on the name provided"""
        if name not in self.linked_events.keys():
            raise EventNotRegistered(f"No event with name '{name}' linked")
        
        self.linked_events[name].trigger(*args, **kwargs)
    
    def trigger_all(self, *args, **kwargs):
        """Triggers every event in the EventGroup"""
        for value in self.linked_events.values():
            value.trigger(args, kwargs)