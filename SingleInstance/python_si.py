class Event:
    class __Event:
        def __init__(self):
            self.val = None
            self.listeners = {}
        def dispatch(self, event):
            print("dispatching event - {}".format(event))
            if event in self.listeners:
                for listener in self.listeners[event]:
                    listener()
        def observe(self, event, listener):
            # print("observing event - {}, listener {}".format(event, listener))
            if event not in self.listeners:
                self.listeners[event] = []
            self.listeners[event].append(listener)
            

    _shared = None
    def __new__(cls):
        if not Event._shared:
            Event._shared = Event.__Event()
        return Event._shared
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name, val):
        return setattr(self.instance, name, val)

class CloseDoorButton:
    def __init__(self):
        self.event = Event()

    def on_press(self):
        self.event.dispatch("close_door")

class DoorControl:
    def __init__(self):
        self.event = Event()
        self.event.observe("close_door", self._on_receive_close_door)

    def _on_receive_close_door(self):
        print("Door Control - closing door")

class PassengerAnnouncement:
    def __init__(self):
        self.event = Event()
        self.event.observe("close_door", self._on_receive_close_door)

    def _on_receive_close_door(self):
        print("PA System - announce door is closing")

closeDoor = CloseDoorButton()
doorControl = DoorControl()
pa = PassengerAnnouncement()

closeDoor.on_press()

