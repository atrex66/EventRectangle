import pygame


class EventRect(pygame.Rect):
    name = 'Eventrect'
    pressed = 0
    hover = False
    on_click = None
    on_mouse_enter = None
    on_mouse_leave = None
    on_mouse_move = None
    enter = False
    counter = 0

    def __init__(self, name, x, y, w, h):
        self.name = name
        pygame.Rect.__init__(self, x, y, w, h)

    def set_on_click(self, f):
        self.on_click = f

    def set_on_enter(self, f):
        self.on_mouse_enter = f

    def set_on_leave(self,f):
        self.on_mouse_leave = f

    def set_on_move(self, f):
        self.on_mouse_move = f

    def set_events_target(self, oc, oe, ol, om):
        self.on_click = oc
        self.on_mouse_enter = oe
        self.on_mouse_leave = ol
        self.on_mouse_move = om


class EventContainer:
    objects = list()
    names = list()
    name = 'EventContainer'

    def __init__(self, n):
        self.name = n
        pass

    def add(self, obj):
        self.names.append(obj.name)
        self.objects.append(obj)

    def get_object_by(self, name=None, index=None):
        if name is not None:
            return self.objects[self.names.index(name)]
        if index is not None:
            return self.objects[index]
        return None

    def process(self, events):
        mp = pygame.mouse.get_pos()
        for k in events:
            for i in self.objects:
                if i.collidepoint(mp):
                    if not i.enter:
                        if i.on_mouse_enter is not None:
                            i.on_mouse_enter(i)
                            i.counter = 254
                    if k.type == pygame.MOUSEBUTTONDOWN and i.on_click is not None:
                        if k.button == 1:
                            i.pressed = 30
                            i.on_click(i)
                    if k.type == pygame.MOUSEMOTION and i.on_mouse_move is not None:
                        i.hover = 1
                        i.on_mouse_move(i)
                    i.enter = True
                else:
                    if i.enter and i.on_mouse_leave is not None:
                        i.on_mouse_leave(i)
                    i.enter = False
                if i.pressed > 0:
                    i.pressed -= 1

