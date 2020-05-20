import os
import pygame


class Sounds:
    """Manage the sounds"""
    path = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
    pygame.mixer.init()
    mario = pygame.mixer.Sound(f'{path}/sounds/Mario-jump-sound.wav')
    looser = pygame.mixer.Sound(f'{path}/sounds/Swanee-whistle-down.wav')
    winning = pygame.mixer.Sound(
        f'{path}/sounds/Winning-brass-fanfare-sound-effect.wav')


class Dice:
    """Manage the images of the dice"""
    path = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[:-1])
    image = [
        pygame.image.load(f'{path}/img/D1.png'),
        pygame.image.load(f'{path}/img/D2.png'),
        pygame.image.load(f'{path}/img/D3.png'),
        pygame.image.load(f'{path}/img/D4.png'),
        pygame.image.load(f'{path}/img/D5.png'),
        pygame.image.load(f'{path}/img/D6.png')]
