import pygame, os


os.environ['SDL_VIDEO_CENTERED'] = '0'
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

window_size = (1250, 750)
#             width, length
pygame.init()
disp = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()
horiz_speed = 3  # px per frame, 90 px per second
vert_speed = 3
start_position = (525, 265)

def draw_logo(position):
    rekt = pygame.rect.Rect(position[0], position[1], 200, 120)
    pygame.draw.rect(disp, red, rekt)

def draw_background():
    disp.fill((255, 255, 255))

def collision_detection(pos):
    if pos == [0, 0] or pos == [1050, 630] or pos == [0, 630] or pos == [1050, 0]:
        return 3
    elif pos[0] == 0 or pos[0] == 1050:
        return 1
    elif pos[1] == 0 or pos[1] == 630:
        return 2
    else:
        return False

bonks = 0
position = [0, 35]
running = True
while running:
    draw_background()
    draw_logo(position)
    pygame.display.flip()
    position[0] += horiz_speed
    position[1] += vert_speed
    if position[0] > 1050:
        position[0] = 1050
    elif position[0] < 0:
        position[0] = 0
    if position[1] > 630:
        position[1] = 630
    elif position[1] < 0:
        position[1] = 0


    if collision_detection(position) == 3:
        print("Corner!")
        running = False
    elif collision_detection(position) == 1:
        horiz_speed *= -1
        bonks += 1
    elif collision_detection(position) == 2:
        vert_speed *= -1
        bonks += 1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
    clock.tick(240)
print("it took {} bounces to get a corner".format(bonks))
