class Wall:
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, screenScroll):
        self.rect.x += screenScroll[0]
        self.rect.y += screenScroll[1]

    def render(self, surface):
        surface.blit(self.image, self.rect)
