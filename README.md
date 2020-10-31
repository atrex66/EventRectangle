# EventRectangle
Pygame rectangle extension class for mouse event handling

usage:

# if all EventRectangles shares the same function, argument is the calling object
def my_event_function(obj):
  if obj.name == 'name':

evr = EventRect(name, x, y, width, height)  # pygame.Rect + mouse events (name for identification)
evr.on_click = my_onclick  # or None (default=None)
evr.on_mouse_move = my_mouse_move  # or None (default=None)
evr.on_mouse_enter = my_mouse_enter  # or None (default=None)
evr.on_mouse_leave = my_mouse_leave # or None (default=None
#or
evr.set_events_target(on_click, on_mouse_enter, on_mouse_leave, on_mouse_move)

ev = EventContainer('name')
ev.add(evr)

# in the main loop:

events = pygame.event.get()
ev.process(events)


usage in eventrect_test.py
