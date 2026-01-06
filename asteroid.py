from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen,color="white",center=(self.position),radius=self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_degree = random.uniform(20, 50)
        vel_one = self.velocity.rotate(random_degree)
        vel_two = self.velocity.rotate(-random_degree)
        vel_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, vel_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, vel_radius)
        asteroid_one.velocity = vel_one * 1.2
        asteroid_two.velocity = vel_two * 1.2