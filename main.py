import pygame as pg
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from sys import exit

def main():
    pg.init()
    print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()

    asteroids = pg.sprite.Group()
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                exit()

        screen.fill(color="black")

        for sprite in drawable:
            sprite.draw(screen)

        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
