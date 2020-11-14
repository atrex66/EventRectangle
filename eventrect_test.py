from eventrect import *
import pygame

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

grid = (20, 20)
done = False
# make event container for the created rectangles used for multiple screens
ec = EventContainer('EventContainer1')
eclist = list()
font = pygame.font.SysFont(pygame.font.get_default_font(), 32)


def mouse_move(obj, event=None):
    for f in ec.ev_objects:
        if f.counter > 0:
            pygame.draw.rect(screen, colors[f.counter], f)
            f.counter -= 1


def mouse_enter(obj):
    a = font.render('Entering {0}'.format(obj.name), True, pygame.Color('yellow'))
    b = pygame.Surface(a.get_size())
    b.fill(pygame.Color('black'))
    screen.blit(b, (0, 40))
    screen.blit(a, (0, 40))
    obj.counter = 254
    pass


def mouse_leave(obj):
    a = font.render('Leaving {0}'.format(obj.name), True, pygame.Color('green'))
    b = pygame.Surface(a.get_size())
    b.fill(pygame.Color('black'))
    screen.blit(b, (0, 80))
    screen.blit(a, (0, 80))


def on_click(obj, mousepos=(0, 0)):
    a = font.render('Clicked {0}'.format(obj.name), True, pygame.Color('red'))
    b = pygame.Surface(a.get_size())
    b.fill(pygame.Color('black'))
    screen.blit(b, (0, 0))
    screen.blit(a, (0, 0))


colors = list()
for o in range(0, 255):
    colors.append((o, o, o, 255))

# make the screen full of rectangles
q = 0
for i in range(0, 800, grid[0]):
    for j in range(0, 600, grid[1]):
        r1 = EventRect('EventRect{0}'.format(q), i, j, grid[0], grid[1])
        r1.on_mouse_move = mouse_move
        r1.on_mouse_enter = mouse_enter
        r1.on_mouse_leave = mouse_leave
        r1.on_click = on_click
        ec.add(r1)
        q += 1

# eventcontainer for screen1
eclist.append(ec)

print("data generated")
while not done:
    events = pygame.event.get()
    for event in events:  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    #screen.fill(pygame.Color('black'))
    #for l in ec.ev_objects:
    #    pygame.draw.rect(screen, pygame.Color('green'), l, 1)

    # you can select the eventcontainer number to process
    eclist[0].process(events)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
