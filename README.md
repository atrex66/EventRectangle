# EventRectangle
Pygame rectangle extension class for mouse event handling

Extends pygame rectangle with mouse events, on_click, on_mouse_enter, on_mouse_leave, on_mouse_move
First need to create EventRectangle object
then add to an EventContainer and in the main loop call the EventContainer.process(events) for detecting wich
rectangle make the event, with multiple EventContainers you can handle multiple screen events and popup window
events. Handler call functions with the caller object (EventRectangle, mouse position) argument.

usage in eventrect_test.py
