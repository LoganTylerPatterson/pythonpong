# Smarter peoples imports
import sys
import pygame

# My imports
from paddle import Paddle
from settings import Settings
from ball import Ball


class Pong:

    def __init__(self):
        # Start up pygame
        pygame.init()
        self.settings = Settings()

        # Get a display object with height and width from settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # Set the background color to black
        self.bg_color = (0, 0, 0)
        pygame.display.set_caption("Pong")

        # Initialize the firstpaddle
        self.paddle1 = Paddle(self, 1)
        self.paddle2 = Paddle(self, 2)

        # Initialize the ball
        self.ball = Ball(self)

    def run_game(self):

        while True:
            self.check_for_events()
            self.paddle2.update_pos()
            self.paddle1.update_pos()
            if self.ball.check_gone() == 1:
                self.ball.draw_from_center()
            elif self.ball.check_gone() == 0:
                self.ball.draw_from_center()
            self.ball.update()
            self.ball.check_collisions(self.paddle1.rect, self.paddle2.rect)

            self.draw_screen()

    def check_for_events(self):
        # Listening for keyboard and click actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.paddle2.moving_down = True
                elif event.key == pygame.K_UP:
                    self.paddle2.moving_up = True
                elif event.key == pygame.K_z:
                    self.paddle1.moving_down = True
                elif event.key == pygame.K_a:
                    self.paddle1.moving_up = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.paddle2.moving_down = False
                elif event.key == pygame.K_UP:
                    self.paddle2.moving_up = False
                elif event.key == pygame.K_z:
                    self.paddle1.moving_down = False
                elif event.key == pygame.K_a:
                    self.paddle1.moving_up = False

    def draw_screen(self):
        # Update the images and flip the screen
        self.screen.fill(self.settings.bg_color)
        self.paddle1.blit_paddle()
        self.paddle2.blit_paddle()
        self.ball.blit_ball()

        # Draw the display to the screen
        pygame.display.flip()


if __name__ == '__main__':
    pong = Pong()
    pong.run_game()
