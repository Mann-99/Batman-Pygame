import pygame
import random
from pygame import mixer

pygame.init()

# Sound
mixer.music.load("CPS2-Batman.wav")
mixer.music.play(-1)

screen = pygame.display.set_mode((1400, 600))
pygame.display.set_caption("Batman Game")

walkRight = [pygame.image.load('BMrun/run11.png'), pygame.image.load('BMrun/run12.png'),
             pygame.image.load('BMrun/run13.png'),
             pygame.image.load('BMrun/run14.png'), pygame.image.load('BMrun/run15.png'),
             pygame.image.load('BMrun/run16.png')]
walkLeft = [pygame.image.load('BMleft/run11.png'), pygame.image.load('BMleft/run12.png'),
            pygame.image.load('BMleft/run13.png'),
            pygame.image.load('BMleft/run14.png'), pygame.image.load('BMleft/run15.png'),
            pygame.image.load('BMleft/run16.png')]
batarang = [pygame.image.load('batarang/bat1.png'), pygame.image.load('batarang/bat2.png'),
            pygame.image.load('batarang/bat3.png'), pygame.image.load('batarang/bat4.png')]

bg = pygame.image.load('streets.png')
char = pygame.image.load('batman idle.png')

x = 250
y = 200
width = 40
height = 60
vel = 30

batarang = [pygame.image.load('batarang/bat1.png'), pygame.image.load('batarang/bat2.png'),
            pygame.image.load('batarang/bat3.png'), pygame.image.load('batarang/bat4.png')]
batarangX = 0
batarangY = 480
batarangX_change = 0
batarangY_change = 10
batarang_state = "ready"


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(screen, self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

clock = pygame.time.Clock()

left = False
right = False
walkCount = 0

sounds = [pygame.mixer.Sound('sounds/V00.wav'), pygame.mixer.Sound('sounds/V01.wav'),
          pygame.mixer.Sound('sounds/V02.wav')]


def playRandom():
    random.choice(sounds).play()


def ThrowBatarang(x, y):
    global batarang_state
    batarang_state = "throw"
    screen.blit(batarang, (x + 10, y + 0))


def redrawGameWindow():
    global walkCount

    screen.blit(bg, (0, 0))
    if walkCount + 1 >= 18:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount % 6], (x, y))
        walkCount -= 1
    elif right:
        screen.blit(walkRight[walkCount % 6], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
        walkCount = 0

    pygame.display.update()

# main loop
run = True
batbullet = []
while run:
    clock.tick(27)
    pygame.time.delay(50)

    screen.blit(pygame.transform.scale(bg, (1400, 480)), (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT]:
        x += vel
        left = False
        right = True


    else:
        left = False
        right = False
        walkCount = 0
    if keys[pygame.K_UP]:
        y -= 10
    if y <= 130:
        y = 130
    if keys[pygame.K_DOWN]:
        y += 10
    if y >= 220:
        y = 220

    if keys[pygame.K_a]:
        batarang_sound = mixer.Sound("49.wav")
        batarang_sound.play()

    if keys[pygame.K_s]:
        punch_sound = random.choice(sounds).play()
        punch_sound
    redrawGameWindow()

pygame.quit()
