import pygame as pg
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    pg.init()
    print(f"Starting Asteroids with pygame version: {pg.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    while True:
        log_state()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.fill(color="black")

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.draw(screen)

        pg.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
