import pygame
import time
import random

snake_speed = 15

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

frames_per_second_controller = pygame.time.Clock()

snake_pos = [100, 50]

snake_body = [[100,50], [90, 50], [80, 50], [70, 50]]

apple_pos = [random.randrange(1, (window_x_axis//10))*10, random.randrange(1, (window_y_axis//10))*10]

apple_spawn = True

direction = 'RIGHT'
change_direction = direction

score = 0

def show_score(choice, color, font, size):
  score_font = pygame.font.SysFont(font, size)
  score_surface = score_font.render('Current Score : ' + str(score) + ' Keep Going!', True , color)
  score_rectangle = score_surface.get_rect()
  game_window.blit(score_surface, score_rectangle)
  
  
def game_over():
  my_font = pygame.font.SysFont('times new roman', 50)
  game_over_surface = my_font.render("You scored : " + str(score) + ' Nice Job!', True , yellow)
  game_over_rectangle = game_over_surface.get_rect()
  game_over_rectangle.midtop = (window_x_axis/2, window_y_axis/4)
  game_window.blit(game_over_surface, game_over_rectangle)
  pygame.display.flip()
  time.sleep(4)
  pygame.quit()
  quit()
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'

    if change_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == apple_pos[0] and snake_pos[1] == apple_pos[1]:
        score += 10
        apple_spawn = False
    else:
        snake_body.pop()
        
    if not apple_spawn:
        apple_pos = [random.randrange(1, (window_x_axis//10)) * 10,
                          random.randrange(1, (window_y_axis//10)) * 10]
        
    apple_spawn = True
    game_window.fill(dark_blue)

    for pos in snake_body:
        pygame.draw.rect(game_window, hot_pink, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, apple_green, pygame.Rect(apple_pos[0], apple_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > window_x_axis-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_y_axis-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    frames_per_second_controller.tick(snake_speed)