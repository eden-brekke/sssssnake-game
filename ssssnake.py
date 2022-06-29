import pygame
import time
import random

window_x_axis = 1000
window_y_axis = 500

dark_blue = pygame.Color(0, 0, 102)
hot_pink = pygame.Color(255, 0, 102)
apple_green = pygame.Color(0, 255, 0)
white = pygame.Color(255, 255, 255)
yellow = pygame.Color(255, 255, 0)

pygame.init()

pygame.display.set_caption("Welcome to Eden's Sssssnake game")
game_window = pygame.display.set_mode((window_x_axis, window_y_axis))

fames_per_second_controller = pygame.time.Clock()