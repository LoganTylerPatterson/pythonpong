from pygame.sprite import Sprite
import pygame


class Ball:

    def __init__(self, pong_game):
        super().__init__()
        self.screen = pong_game.screen
        self.settings = pong_game.settings
        self.screen_rect = pong_game.screen.get_rect()

        self.image = pygame.image.load("images/pong_ball.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        """Vertically ball can move in three directions, 0 is no slope, 1 is pos slope, -1 is neg slope """
        self.moving_up = 0
        """Horizontally ball can only move in two directions"""
        self.moving_right = False

    def update(self):
        """Move the ball"""
        self.move(self.moving_right, self.moving_up)
        self.rect.y = self.y
        self.rect.x = self.x

    """x is whether to move positiv right"""

    def move(self, xdir, ydir):
        if xdir:
            self.x += self.settings.ball_speed
        else:
            self.x -= self.settings.ball_speed
        if ydir == 1:
            self.y -= self.settings.ball_speed
        elif ydir == -1:
            self.y += self.settings.ball_speed
        else:
            self.y += 0

    """In order to know where to go, ball needs to know: if it hit a paddle low, high, or center, or if it hit the 
    wall """

    def check_collisions(self, paddle_rect, paddle2_rect):
        self.mid1 = ((paddle_rect.bottom - paddle_rect.top) / 2) + paddle_rect.top
        self.mid2 = ((paddle2_rect.bottom - paddle2_rect.top) / 2) + paddle2_rect.top
        if self.x == paddle_rect.right:
            if paddle_rect.top < self.y < self.mid1 - 10:
                self.moving_up = 1
                self.moving_right = True
            elif paddle_rect.bottom > self.y > self.mid1 + 10:
                self.moving_up = -1
                self.moving_right = True
            elif self.mid1 - 10 <= self.y <= self.mid1 + 10:
                self.moving_up = 0
                self.moving_right = True
        elif self.rect.right == paddle2_rect.left:
            if paddle2_rect.top < self.y < self.mid2 - 10:
                self.moving_up = 1
                self.moving_right = False
            elif paddle2_rect.bottom > self.y > self.mid2 + 10:
                self.moving_up = -1
                self.moving_right = False
            elif self.mid2 - 10 <= self.y <= self.mid2 + 10:
                self.moving_up = 0
                self.moving_right = False
        elif self.rect.top == self.screen_rect.top:
            self.moving_up = -1
        elif self.rect.bottom == self.screen_rect.bottom:
            self.moving_up = 1

    def check_gone(self):
        if self.x > self.screen_rect.right + 500:
            '''Update Score'''
            return 1
        elif self.x < self.screen_rect.left - 500:
            '''Update Score'''
            return 0

    def draw_from_center(self):
        self.moving_right =  not self.moving_right
        self.move(self.moving_right, self.moving_up)
        self.rect.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center
        self.x = self.rect.x
        self.y = self.rect.y

    def blit_ball(self):
        # Draw the ball to the screen
        self.screen.blit(self.image, self.rect)
