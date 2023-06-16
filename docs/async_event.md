# AsyncEvent

Class used for asynchronous events

## Methods

#### ```AsyncEvent.register()```

Decorator used to add a coroutine to the event

#### ```AsyncEvent.unregister()```

Decorator used to remove a coroutine from the event

#### ```AsyncEvent.trigger(*args, **kwargs)```

Calls all coroutines registered in the current event

## Properties

#### ```AsyncEvent.registered_coroutines```

Returns a list of all currently registered coroutines