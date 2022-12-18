import pygame.font


class Button:
    """A class to manage buttons in the game."""

    def __init__(self, game_instance, message, color):
        """Initialize the button."""
        # Setup main surface
        self.screen = game_instance.screen
        self.screen_rectangle = self.screen.get_rect()

        # Setup button properties
        self.width, self.height = 200, 50
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Rectangular container of button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        match self.button_color:
            case game_instance.settings.play_button_color:
                self.rect.center = self.screen_rectangle.center
            case game_instance.settings.easy_button_color:
                new_center = list(self.screen_rectangle.center)
                new_center[-1] -= 100
                self.rect.center = tuple(new_center)
            case game_instance.settings.normal_button_color:
                self.rect.center = self.screen_rectangle.center
            case game_instance.settings.hard_button_color:
                new_center = list(self.screen_rectangle.center)
                new_center[-1] += 100
                self.rect.center = tuple(new_center)

        # Add message onto button
        self._prepare_message(message)

    def _prepare_message(self, message):
        """Turns message into rendered image and centers onto the button."""
        self.message_image = self.font.render(message, True, self.text_color, self.button_color)
        self.message_image_rectangle = self.message_image.get_rect()
        self.message_image_rectangle.center = self.rect.center

    def draw_button(self):
        """Draws the button and then the message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rectangle)
