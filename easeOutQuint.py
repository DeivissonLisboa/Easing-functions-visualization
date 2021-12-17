import pygame
import pytweening as tween

# GLOBALS


# COLORS


# SCREEN SETUP
pygame.init()
WIDTH, HEIGHT = 800, 800
root = pygame.display.set_mode((WIDTH, HEIGHT))
# icon = pygame.image.load( ICON PATH HERE )
# pygame.display.set_icon(icon)
TITLE = "Easing functions easeOutQuint"
pygame.display.set_caption(TITLE)
FPS = 30

# MUSIC
# audio = pygame.mixer.music.load( MP3 PATH HERE )
# pygame.mixer.music.play(loops=-1)
# pygame.mixer.music.set_volume(0.1)

# OBJECTS
class Circle(pygame.sprite.Sprite):
    def __init__(self, surface, pos, size):
        super().__init__()
        self.surface = surface
        self.size = size
        self.r = size // 200
        self.range = 100
        self.circle_sprites = [self.createCircle(i) for i in range(5, self.range)]
        self.current_sprite = 0
        self.image = self.circle_sprites[self.current_sprite]
        self.rect = self.image.get_rect(center=pos)
        self.ani_speed = 0.5
        self.tween = tween.easeOutQuint  # https://easings.net/
        self.dir = -1

    def createCircle(self, scale):
        surface = pygame.Surface((self.size, self.size))
        pygame.draw.circle(
            surface,
            "white",
            (self.size // 2, self.size // 2),
            (self.r * scale),
            width=0,
        )
        return surface

    def update(self):
        self.current_sprite += self.ani_speed * self.dir
        current = int(self.tween(abs(self.current_sprite / self.range)) * self.range)

        if current >= len(self.circle_sprites) - 1:
            self.dir *= -1

        self.image = self.circle_sprites[current]


group = pygame.sprite.Group()
circle = Circle(root, (WIDTH // 2, HEIGHT // 2), 600)
group.add(circle)


# ANIMATIONS
def draw():
    root.fill("black")

    group.draw(root)
    group.update()

    pygame.display.update()


# MAIN LOOP
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()


if __name__ == "__main__":
    main()
    pygame.quit()
