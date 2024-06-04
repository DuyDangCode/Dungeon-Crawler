from buttons.imageButton import ButtonImage
from config import gameConstant
import pygame
from pygame import mixer
import sys
from tile.screenFade import ScreenFade
from tile.world import World
from utils.imageUtils import scaleImage

# pathWeaponsImage = "assets/images/weapons/"

pygame.init()
mixer.init()
pathAudio = "assets/audio/"

mixer.music.load(pathAudio + "music.wav")
mixer.music.set_volume(0.5)
mixer.music.play(-1, 0.5, 5000)

arrowHitSound = mixer.Sound(pathAudio + "arrow_hit.wav")
arrowShotSound = mixer.Sound(pathAudio + "arrow_shot.mp3")
coinSound = mixer.Sound(pathAudio + "coin.wav")
healSound = mixer.Sound(pathAudio + "heal.wav")
arrowShotSound.set_volume(0.3)
arrowHitSound.set_volume(0.3)
coinSound.set_volume(0.3)
healSound.set_volume(0.3)
sounds = {}
sounds["arrow_hit"] = arrowHitSound
sounds["arrow_shot"] = arrowShotSound
sounds["coin"] = coinSound
sounds["heal"] = healSound

clock = pygame.time.Clock()
atariFont = pygame.font.Font(gameConstant.FONT_PATH_ATARI, gameConstant.FONT_SIZE)


pygame.display.set_caption(gameConstant.GAME_NAME)
screen = pygame.display.set_mode(
    (gameConstant.SCREEN_WIDTH, gameConstant.SCREEN_HEIGHT)
)


def drawGrid(screen):
    for i in range(30):
        pygame.draw.line(
            screen,
            gameConstant.WHITE,
            (i * gameConstant.TILE_SIZE, 0),
            (i * gameConstant.TILE_SIZE, gameConstant.SCREEN_HEIGHT),
        )
        pygame.draw.line(
            screen,
            gameConstant.WHITE,
            (0, i * gameConstant.TILE_SIZE),
            (gameConstant.SCREEN_WIDTH, i * gameConstant.TILE_SIZE),
        )


world = World(atariFont, sounds)
butonImage = ButtonImage()
screenFade = ScreenFade()
introFade = True
gameOver = False
screenScroll = [0, 0]
gameStart = False
gamePause = False
win = False


def menuWin():
    global win
    global world
    tempSurface = pygame.Surface(
        (gameConstant.SCREEN_WIDTH, gameConstant.SCREEN_HEIGHT)
    )
    tempSurface.set_alpha(128)
    tempSurface.fill(gameConstant.MAROON)
    screen.blit(tempSurface, (0, 0))
    textImage = atariFont.render("You win", True, gameConstant.WHITE)
    screen.blit(textImage, (50, 50))
    restartButton = screen.blit(butonImage.imagesList["button_restart"], (50, 150))
    existButton = screen.blit(
        butonImage.imagesList["button_exit"],
        (50, 180 + butonImage.imagesList["button_restart"].get_height()),
    )

    posMouse = pygame.mouse.get_pos()
    if restartButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            world.win = False
            win = False
    if existButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def menuStart():
    global gameStart
    tempSurface = pygame.Surface(
        (gameConstant.SCREEN_WIDTH, gameConstant.SCREEN_HEIGHT)
    )
    tempSurface.set_alpha(128)
    tempSurface.fill(gameConstant.MAROON)
    screen.blit(tempSurface, (0, 0))
    startButton = screen.blit(butonImage.imagesList["button_start"], (50, 50))
    existButton = screen.blit(
        butonImage.imagesList["button_exit"],
        (50, 80 + butonImage.imagesList["button_start"].get_height()),
    )
    screen.blit(
        scaleImage(pygame.image.load("assets/images/characters/elf/idle/1.png"), 20),
        (gameConstant.SCREEN_WIDTH / 2, 0),
    )
    posMouse = pygame.mouse.get_pos()
    if startButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            gameStart = True
    if existButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def menuPause():
    global gamePause
    tempSurface = pygame.Surface(
        (gameConstant.SCREEN_WIDTH, gameConstant.SCREEN_HEIGHT)
    )
    tempSurface.set_alpha(128)
    tempSurface.fill(gameConstant.MAROON)
    screen.blit(tempSurface, (0, 0))
    screen.blit(
        pygame.transform.flip(
            scaleImage(
                pygame.image.load("assets/images/characters/elf/idle/1.png"), 20
            ),
            True,
            False,
        ),
        (gameConstant.SCREEN_WIDTH / 2, 0),
    )
    resumeButton = screen.blit(butonImage.imagesList["button_resume"], (50, 50))
    existButton = screen.blit(
        butonImage.imagesList["button_exit"],
        (50, 80 + butonImage.imagesList["button_resume"].get_height()),
    )
    posMouse = pygame.mouse.get_pos()
    if resumeButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            gamePause = False
    if existButton.collidepoint(posMouse):
        if pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def main():
    moving_up, moving_down, moving_right, moving_left = (
        False,
        False,
        False,
        False,
    )
    while True:
        clock.tick(gameConstant.FPS)
        screen.fill(gameConstant.BACKGROUND)
        global gameStart
        global gamePause
        global win
        if win:
            menuWin()
        elif not gameStart:
            menuStart()
        else:
            if gamePause:
                menuPause()
            else:
                global screenScroll
                global introFade
                global gameOver

                dx, dy = 0, 0
                if moving_up:
                    dy += -gameConstant.SPEED
                if moving_down:
                    dy += gameConstant.SPEED
                if moving_left:
                    dx += -gameConstant.SPEED
                if moving_right:
                    dx += gameConstant.SPEED

                introFade = world.update(dx, dy) or introFade
                world.render(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_a:
                            moving_left = True
                        if event.key == pygame.K_w:
                            moving_up = True
                        if event.key == pygame.K_d:
                            moving_right = True
                        if event.key == pygame.K_s:
                            moving_down = True
                        if event.key == pygame.K_ESCAPE:
                            gamePause = True
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_a:
                            moving_left = False
                        if event.key == pygame.K_w:
                            moving_up = False
                        if event.key == pygame.K_d:
                            moving_right = False
                        if event.key == pygame.K_s:
                            moving_down = False

                gameOver = world.gameOver
                if introFade:
                    introFade = screenFade.fade(screen, 0)
                if gameOver:
                    screenFade.fade(screen, 1)

                    buttonRestartImage = butonImage.imagesList["button_restart"]
                    buttonRestartRect = buttonRestartImage.get_rect()
                    buttonRestartRect.center = (
                        gameConstant.SCREEN_WIDTH / 2,
                        gameConstant.SCREEN_HEIGHT / 2,
                    )
                    posMouse = pygame.mouse.get_pos()
                    screen.blit(buttonRestartImage, buttonRestartRect)
                    if buttonRestartRect.collidepoint(posMouse):
                        if pygame.mouse.get_pressed()[0]:
                            gameOver = False
                            introFade = True
                            world.gameOver = False
                            world.resetLevel(world.level)
                if world.win:
                    win = True
        pygame.display.update()


main()
