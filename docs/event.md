# Event

Class used for synchronous events

## Methods

#### ```Event.register()```

Decorator used to add a function to the event

#### ```Event.unregister()```

Decorator used to remove a function from the event

#### ```Event.trigger(*args, **kwargs)```

Calls all functions registered in the current event

## Properties

#### ```Event.registered_functions```

Returns a list of all currently registered functions