import tkinter as tk
from tkinter import messagebox
import pygame
import random
from Classes.Snake import Snake
from Classes.Cube import Cube

clock = pygame.time.Clock()
width = 500
height = 500
rows = 20
window = pygame.display.set_mode((width, height))


def draw_grid(surface):
    size_between = width // rows
    x = 0
    y = 0

    for i in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


def redraw_window(surface, snake, snack):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(surface)
    pygame.display.update()


def random_snack(snake):
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x, y), positions))) > 0:
            continue
        else:
            break
    return Cube(start=(x, y), rows=rows, height=height, width=width, color=(0, 255, 0))


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    root.destroy()


def main():
    snake = Snake(color=(255, 0, 0), position=(10, 10), rows=rows, height=height, width=width)
    snack = random_snack(snake)
    while True:
        pygame.time.delay(100)
        clock.tick(10)
        snake.move()
        if snake.body[0].position == snack.position:
            snake.add_cube()
            snack = random_snack(snake)
        # Check to see if the snake has collided with itself
        for x in range(len(snake.body)):
            if snake.body[x].position in list(map(lambda z: z.position, snake.body[x + 1:])):
                print('Score: ', len(snake.body))
                message_box('You Died!', 'You died! Your score was ' + str(len(snake.body)))
                snake.reset((10, 10))
                break
        redraw_window(window, snake, snack)


main()
