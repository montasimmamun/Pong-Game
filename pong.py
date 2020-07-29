import pygame
import random
import sys

#  sound
pygame.mixer.init()

#   initialize pygame
pygame.init()


# Colors
white = (255, 255, 255)
red = (255,0,77)
black = (0, 0, 0)
gameName = (255, 0, 77)
enterToPlay = (0,181,184)
quitGame = (254, 225, 26)
gameOver = (255, 0, 77)
enterToContinue = (90, 39, 193)
qToQuit = (39, 159, 0)
#   window size
screen_width = 500
screen_height = 500

#   bar size
bar_width = 100
bar_height = 15

sx = 200
sy = 450

bx = int(screen_width / 2)
by = int(screen_height / 2)

#   ball radius
ball_radius = 15

#   bar speed
speed = 0

bxspeed = 1
byspeed = -2
event_delayer = 3   #   make event delay

#   result
result = ""

#   set display
screen = pygame.display.set_mode([screen_width, screen_height])

#   background image
backgroundImage = pygame.image.load("images/gameImage.png")
backgroundImage = pygame.transform.scale(backgroundImage, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Pong Game")    #   set game name to Snake Game
pygame.display.update()

#   game icon
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#   game font
font = pygame.font.SysFont(None, 30)

#   snake fps
fps = 60
clock = pygame.time.Clock()

#   display score to screen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, [x,y])

#   display color black
screen.fill((0, 0, 0))

#   display ball
pygame.draw.circle(screen, (255, 255, 0), (bx, by), ball_radius, 0)
#   display bar
pygame.draw.rect(screen, (255, 40, 0), (sx, sy, bar_width, bar_height), 0)
#   update display
pygame.display.flip()


def sblock():
    global speed
    if sx <= 0 or sx >= screen_width - bar_width:
        speed = 0

#   ball movement
def ball_movement():
    global bx, by
    bx += bxspeed
    by += byspeed

#   reset ball
def reset():
    global byspeed, bxspeed, event_delayer, bx, by, sx, sy, speed
    sx = 200
    sy = 450

    bx = int(screen_width / 2)
    by = int(screen_height / 2)

    speed = 0

    bxspeed = random.randint(-2, 2)

    if bxspeed == 0:
        bxspeed = 1

    byspeed = random.randint(-2, 2)

    if byspeed == 0:
        byspeed = 2

    #   old bar and ball disappear
    screen.fill((0, 0, 0))
    #   display new ball
    pygame.draw.circle(screen, (255, 255, 0), (bx, by), ball_radius, 0)
    #   display new bar
    pygame.draw.rect(screen, (255, 40, 0), (sx, sy, bar_width, bar_height), 0)
    #   update new screen
    pygame.display.flip()
    #   wait 10 sec
    pygame.time.wait(1000)


def ballblock():
    global byspeed, bxspeed, event_delayer
    if by - ball_radius <= 0:
        byspeed *= -1
    if bx - ball_radius <= 0:
        bxspeed *= -1
    if bx + ball_radius >= screen_width:
        bxspeed *= -1
    if by >= 435 and by <= 440:
        if bx >= sx - 15 and bx <= sx + bar_width + 15:
            byspeed *= -1
        else:
            event_delayer -= 1
            reset()


def movement():
    global sx
    sx += speed


#   welcome screen
def welcome():
    #   play welcome music
    pygame.mixer.music.load('sounds/game.mp3')
    pygame.mixer.music.play()

    #   game control variable
    exit_game = False
    while not exit_game:
        global result

        #   welcome image
        welcomeImage = pygame.image.load("images/welcomeImage.png")
        welcomeImage = pygame.transform.scale(welcomeImage, (screen_width, screen_height)).convert_alpha()

        screen.blit(welcomeImage, (0, 0))
        text_screen("Pong Game By Montasim", gameName, 130, 10)
        text_screen(f"{result}", gameName, 230, 50)
        text_screen("Press Enter To Play", enterToPlay, 165, 342)
        text_screen("Press Q to Quit", quitGame, 180, 376)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Game()

                if event.key == pygame.K_q:
                    quit()

        pygame.display.update()
        clock.tick(60)

def GameOver():

    #   set display
    screen = pygame.display.set_mode([screen_width, screen_height])

    #   text_screen("Score: " + str(score) + ", High Score: " + str(hiScore), scoreHighScore, 170, 150)
    text_screen("Game Over!", gameOver, 240, 175)
    text_screen("Press Enter To Continue", enterToContinue, 180, 200)
    text_screen("Press Q To Quit", qToQuit, 225, 225)

    #   update display
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                Game()

            if event.key == pygame.K_q:
                quit()

        #   print(event)  #   prints all event in the game


def Game():
    while event_delayer > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    global speed
                    speed = -2
                if event.key == pygame.K_RIGHT:
                    speed = 2

        #   redraw every event of entire surface
        screen.fill((0, 0, 0))
        movement()
        sblock()
        pygame.draw.rect(screen, (255, 40, 0), (sx, sy, bar_width, bar_height), 0)
        ball_movement()
        ballblock()
        pygame.draw.circle(screen, (255, 255, 0), (bx, by), ball_radius, 0)
        pygame.display.flip()
        pygame.time.wait(5)

    #   print("Lost")

welcome()