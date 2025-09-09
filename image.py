import pygame
import sys
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake on Screen")

BLACK=(0,0,0)
GREEN=(0, 255, 0)

snake_pos=[100, 50]
snake_body=[[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
speed = 15

clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and snake_direction !='DOWN':
                snake_direction='UP'
            if event.key==pygame.K_DOWN and snake_direction !='UP':
                snake_direction='DOWN'
            if event.key==pygame.K_LEFT and snake_direction !='RIGHT':
                snake_direction='LEFT'
            if event.key==pygame.K_RIGHT and snake_direction !='LEFT':
                snake_direction='RIGHT'
    if snake_direction=='UP':
        snake_pos[1]-=10
    if snake_direction=='DOWN':
        snake_pos[1]+=10
    if snake_direction=='LEFT':
        snake_pos[0]-=10
    if snake_direction=='RIGHT':
        snake_pos[0]+=10

    snake_body.insert(0,list(snake_pos))
    snake_body.pop()
    for pos in snake_body:
        pygame.draw.rect(screen,GREEN,pygame.Rect(pos[0],pos[1],10,10))
    pygame.display.update()
    clock.tick(speed)
