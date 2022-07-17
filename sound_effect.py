import pygame

pygame.init()
sound = pygame.mixer.music


def ball_bouncing():
    sound.load('bouncing.mp3')
    pygame.mixer.music.set_volume(0.5)
    sound.play()


def game_over():
    sound.load('game_over.mp3')
    sound.play()