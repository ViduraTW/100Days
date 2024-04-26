
import pygame as pg
from random import randrange

WINDOW = 1000
Tile_size = 50
Range = (Tile_size // 2, WINDOW - Tile_size // 2, Tile_size)
get_random_position = lambda: [randrange(*Range), randrange(*Range)]
snake = pg.rect.Rect([0, 0, Tile_size - 2, Tile_size - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
time, time_step = 0, 100
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()




while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_dir = (0, -Tile_size)
            if event.key == pg.K_DOWN:
                snake_dir = (0, Tile_size)
            if event.key == pg.K_LEFT:
                snake_dir = (-Tile_size, 0)
            if event.key == pg.K_RIGHT:
                snake_dir = (Tile_size, 0)



    screen.fill('black')


    #check borders

    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1

    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        length, snake_dir = 1, (0, 0)
        segments = [snake.copy()]





    #draw food

    pg.draw.rect(screen, 'cyan', food)

    #check food

    if snake.center == food.center:
        food.center = get_random_position()
        length += 1


    #food in tails
    food_in_tail = pg.Rect.collidelist(food, segments[:-1]) != -1
    if food_in_tail:
        food.center = get_random_position()



    #draw snake
    [pg.draw.rect(screen, 'dark green', segment) for segment in segments]

    #move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]


    pg.display.flip()
    clock.tick(60)











