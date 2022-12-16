import pygame.font


class Button:
    """A class to manage buttons in the game."""
    def __init__(self, game_instance, message):
        """Initialize the button."""
        # Setup main surface
        self.screen = game_instance.screen
        self.screen_rectangle = self.screen.get_rect()

        # Setup button properties
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Rectangular container of button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rectangle.center

        # Add message onto button
        self._prepare_message(message)

    def _prepare_message(self, message):
        """Turns message into rendered image and centers onto the button."""
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rectangle = self.message_image.get_rect()
        self.message_image_rectangle.center = self.rect.center
