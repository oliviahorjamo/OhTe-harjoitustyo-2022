import pygame

class GeneralUIDrawing:
    """Kaikille näkymille yhteisten objektien piirtämisestä vastaava luokka.
    """
    def __init__(self, display):
        """Luokan konstruktori, joka luo uuden GeneralUIDrawing -luokan olion.

        Args:
            display: Näkymän luokalle parametrina antama näyttö, jolle luokan
            piirtofunktiot piirtävät.
        """
        pygame.font.init()
        self._blue = (206, 243, 245)
        self._black = (0,0,0)
        self._button_outline_width = 2
        self._field_outline_width = 2
        self._text_x_scaling_factor = 10
        self._descritpion_y_scaling_factor = 30
        self._display = display

    def draw_button(self, button, mouse_over_button = False):
        """Piirtää erilaisia painikkeita.

        Args:
            button: Piirrettävä painike Sprite -oliona.
            mouse_over_button: Boolean -arvo, joka kertoo, onko käyttäjän
            hiiri kyseisen painikkeen kohdalla.
        """
        if mouse_over_button:
            pygame.draw.rect(self._display, self._blue, button)
        pygame.draw.rect(self._display, self._black, button, self._button_outline_width)
        self._display.blit(button.text,
                          (button.rect.x + self._text_x_scaling_factor, button.rect.y))

    def draw_text_field(self, field, description, text, field_clicked = False):
        """Piirtää erilaisia tekstikenttiä.

        Args:
            field: Piirrettävä tekstikenttä Sprite -oliona.
            description: Piirrettävän tekstikentän kuvaus str -muodossa.
            text: Tekstikenttään kirjoitettu teksti str -muodossa.
            field_clicked: Boolean -arvo, joka kertoo, onko tekstikenttää klikattu.
        """
        if field_clicked:
            pygame.draw.rect(self._display, self._blue, field)
        pygame.draw.rect(self._display, self._black, field.rect, self._field_outline_width)
        description_surface = field.font.render(
            description, 1, self._black
        )
        self._display.blit(
            description_surface, (field.rect.x, field.rect.y - self._descritpion_y_scaling_factor)
        )
        text_surface = field.font.render(text, 1, self._black)
        self._display.blit(
            text_surface, (field.rect.x + self._text_x_scaling_factor, field.rect.y)
        )