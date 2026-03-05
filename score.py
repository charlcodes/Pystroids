import pygame

class Score:
    def __init__(
        self,
        font_name="Arial",
        font_size=24,
        bold=True,                          #to do place all in constants
        padding=8,
        margin=10,
        bg_color=(0, 0, 0),
        border_color=(255, 215, 0),
        text_color=(255, 255, 255),
        border_width=2,
        border_radius=6
    ):
        self.font = pygame.font.SysFont(font_name, font_size, bold=bold)
        self.padding = padding
        self.margin = margin
        self.bg_color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.border_width = border_width
        self.border_radius = border_radius
        self.score = 0

    def set_score(self, value):
        self.score = value

    def add(self, amount=1):
        self.score += amount

    def reset(self):
        self.score = 0

    def draw(self, surface):
        formated_score = str(self.score).zfill(8)
        label = self.font.render(f"*{formated_score}*", True, self.text_color, self.bg_color)
        box_w = label.get_width() + self.padding * 2
        box_h = label.get_height() + self.padding * 2

        box_rect = pygame.Rect(self.margin, self.margin, box_w, box_h)
        pygame.draw.rect(surface, self.bg_color, box_rect, border_radius=self.border_radius)
        pygame.draw.rect(surface, self.border_color, box_rect, self.border_width, border_radius=self.border_radius)

        surface.blit(label, (self.margin + self.padding, self.margin + self.padding))

    