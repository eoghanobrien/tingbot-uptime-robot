"""
The default view
"""
class ViewDefault(object):
    def __init__(self, screen):
        self.screen = screen
        self.bgcolor = (141,133,202)
        self.text_color = "white"
        self.align = "center"
        self.fonts = {"large": 24, "medium": 16, "small": 14}
        self.x = 160
        
    def render(self, image, text):
        self.screen.fill(color = self.bgcolor)
        self.screen.image(image, scale = "fit")
        self._render_desc_line(text)
        
    def _render_message_line(self, text):
        self.screen.text(
            text,
            color = self.text_color,
            align = self.align,
            xy = (self.x, 150),
            max_lines = 1,
            font_size = self.fonts["large"]
        )

    def _render_desc_line(self, text):
        self.screen.text(
            text,
            color = 'white',
            align = 'center',
            xy = (self.x, 200),
            max_lines = 1,
            font_size = self.fonts["medium"]
        )
    
    def _render_label_line(self, text):
        self.screen.text(
            text,
            color = self.text_color,
            align = self.align,
            xy = (self.x, 220),
            max_lines = 1,
            font_size = self.fonts["small"]
        )

"""
The Up view
"""
class ViewUp(ViewDefault):
    def __init__(self, screen, website):
        super(ViewUp, self).__init__(screen)
        self.screen = screen
        self.website = website
        self.bgcolor = (85,171,104)
        self.text_color = "white"
        self.align = "center"
        
    def render(self, image, text):
        self.screen.fill(color = self.bgcolor)
        self.screen.image(image, scale = "fit")
        self._render_message_line(text)
        self._render_desc_line(self.website.name)
        self._render_label_line(self.website.url)

"""
The Down view
"""    
class ViewDown(ViewDefault):
    def __init__(self, screen, website):
        super(ViewDown, self).__init__(screen)
        self.screen = screen
        self.website = website
        self.text_color = "white"
        self.bgcolor = (177,67,52)
        self.align = "center"
        
    def render(self, image, text):
        self.screen.fill(color = self.bgcolor)
        self.screen.image(image, scale = "fit")
        self._render_message_line(text)
        self._render_desc_line(self.website.name)
        self._render_label_line(self.website.url)
