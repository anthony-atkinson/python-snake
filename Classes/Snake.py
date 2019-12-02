import pygame
from Classes.Cube import Cube


class Snake(object):
    body = []
    turns = {}

    def __init__(self, rows, height, width, color, position):
        self.color = color
        self.rows = rows
        self.height = height
        self.width = width
        self.head = Cube(start=(10, 10), rows=rows, height=height, width=width)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.add_head_pos_to_turns()
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.add_head_pos_to_turns()
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.add_head_pos_to_turns()
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.add_head_pos_to_turns()
        for body_index, cube in enumerate(self.body):
            # Copy cube's position array
            p = cube.position[:]
            if p in self.turns:
                # Retrieve turn at body_index
                turn = self.turns[p]
                # Move the cube to the turns specified position
                cube.move(turn[0], turn[1])
                if body_index == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                # Move the cube to the right side if it's hit the edge of the left
                if cube.dirnx == -1 and cube.position[0] <= 0:
                    cube.position = (cube.rows - 1, cube.position[1])
                # Move the cube to the left side if it's hit the edge of the right
                elif cube.dirnx == 1 and cube.position[0] >= cube.rows - 1:
                    cube.position = (0, cube.position[1])
                # Move the cube to the top side if it's hit the edge of the bottom
                elif cube.dirny == 1 and cube.position[1] >= cube.rows - 1:
                    cube.position = (cube.position[0], 0)
                # Move the cube to the bottom side if it's hit the edge of the top
                elif cube.dirny == -1 and cube.position[1] <= 0:
                    cube.position = (cube.position[0], cube.rows - 1)
                # Just move the cube along. Nothing to see here
                else:
                    cube.move(cube.dirnx, cube.dirny)

    def add_head_pos_to_turns(self):
        self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

    def reset(self, pos):
        self.head = Cube(start=pos, rows=self.rows, height=self.height, width=self.width)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx, self.dirny = 0, 1

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        def create_cube(x, y):
            return Cube(start=(x, y), rows=self.rows, height=self.height, width=self.width)

        if dx == 1 and dy == 0:
            self.body.append(create_cube(tail.position[0] - 1, tail.position[1]))
        elif dx == -1 and dy == 0:
            self.body.append(create_cube(tail.position[0] + 1, tail.position[1]))
        elif dx == 0 and dy == 1:
            self.body.append(create_cube(tail.position[0], tail.position[1] - 1))
        elif dx == 0 and dy == -1:
            self.body.append(create_cube(tail.position[0], tail.position[1] + 1))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, cube in enumerate(self.body):
            if i == 0:
                cube.draw(surface, True)
            else:
                cube.draw(surface)
