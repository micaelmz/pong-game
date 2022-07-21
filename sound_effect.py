import pygame

pygame.init()
sound = pygame.mixer.music


def ball_bouncing():
    sound.load('sounds/bouncing.mp3')
    sound.set_volume(0.5)
    sound.play()


def game_over():
    sound.load('sounds/game_over.mp3')
    sound.set_volume(0.5)
    sound.play()
