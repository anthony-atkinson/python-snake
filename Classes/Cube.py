import pygame


class Cube(object):
    def __init__(self, rows, height, width, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.rows = rows
        self.height = height
        self.width = width
        self.position = start
        self.dirnx = dirnx
        self.dirny = dirny
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny)

    def draw(self, surface, eyes=False):
        distance = self.width // self.rows
        i = self.position[0]
        j = self.position[1]

        # Draw the cube in; modify the position such that it draws inside the grid square
        pygame.draw.rect(surface, self.color, (i * distance + 1, j * distance + 1, distance - 2, distance - 2))
        # Draw the eyes if requested
        if eyes:
            center = distance // 2
            radius = 3
            left_eye = (i * distance + center - radius, j * distance + 8)
            right_eye = (i * distance + distance - radius * 2, j * distance + 8)
            pygame.draw.circle(surface, (0, 0, 0), left_eye, radius)
            pygame.draw.circle(surface, (0, 0, 0), right_eye, radius)
