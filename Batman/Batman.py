import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 600))

pygame.display.set_caption("Batman")

RunRight = [pygame.image.load('BMrun/run1.png'),pygame.image.load('BMrun/run2.png'),pygame.image.load('BMrun/run3.png'),pygame.image.load('BMrun/run4.png'),pygame.image.load('BMrun/run5.png'),
            pygame.image.load('BMrun/run6.png'),pygame.image.load('BMrun/run7.png'),pygame.image.load('BMrun/run8.png'),pygame.image.load('BMrun/run9.png'),pygame.image.load('BMrun/run10.png'),]
char = pygame.image.load('batman idle.png')


clock = pygame.time.Clock()

x = 500
y = 200
width = 64
height = 64
vel = 5
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount

    if walkCount + 1 >= 27:
        walkCount = 0

    if right:
        screen.blit(RunRight[walkCount // 3], (x, y))
        walkCount += 2
    else:
        screen.blit(char, (x, y))

    pygame.display.update()



# main loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    redrawGameWindow()

pygame.quit()