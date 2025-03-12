import pygame
from constants import *
from player import*
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize pygame modules
    pygame.init()

    # Set game logic parameters
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Initialize game objeccts
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Shot.containers =(shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    # Game Loop:
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            # Enable quit button
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split()
                    shot.kill()
                



        for asteroid in asteroids:
            if asteroid.collide(player):
                running = False
                print("Game Over!!")
        # Draw game objects
        screen.fill("black") # Black background
        for obj in drawable:
            obj.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Limit framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()