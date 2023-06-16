# EventGroup

Class used for grouping events and async events

## Methods

#### ```EventGroup.link_event(event:Union[Event, AsyncEvent], name:str)```

Adds an event to the group

#### ```EventGroup.unlink_event(name:str)```

Removes an event from the group

#### ```Event.trigger_event(name:str, *args, **kwargs)```

Calls a specific event by it's name

#### ```Event.trigger_all(*args, **kwargs)```

Calls all linked events

## Properties

#### ```Event.linked_events```

Returns a list of all currently registered functions