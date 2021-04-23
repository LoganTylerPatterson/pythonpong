import pygame


class Paddle:
    # Here we could pass parameters if we want to play against the computer or another person
    def __init__(self, pong_game, player):
        self.screen = pong_game.screen
        self.screen_rect = pong_game.screen.get_rect()
        self.settings = pong_game.settings

        # Load the paddle image and get the rectangle
        self.image = pygame.image.load('images/paddle.bmp')
        self.rect = self.image.get_rect()

        # We use 1 and 2 to determine whether to display the paddle on the right or the left side
        if player == 1:
            self.rect.midleft = self.screen_rect.midleft
            self.rect.left += 20
        elif player == 2:
            self.rect.midright = self.screen_rect.midright
            self.rect.right -= 20

        # Store the paddle's vertical position
        self.y = float(self.rect.y)

        self.moving_down = False
        self.moving_up = False

    def update_pos(self):
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.paddle_mov_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.paddle_mov_speed
        self.rect.y = self.y

    def blit_paddle(self):
        # Draw the paddle to the screen
        self.screen.blit(self.image, self.rect)
