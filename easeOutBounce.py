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
TITLE = "Easing function easeOutBounce"
pygame.display.set_caption(TITLE)
FPS = 30

# MUSIC
# audio = pygame.mixer.music.load( MP3 PATH HERE )
# pygame.mixer.music.play(loops=-1)
# pygame.mixer.music.set_volume(0.1)

# OBJECTS
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, pos, radius):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2))
        # self.image = pygame.image.load("bigSlime.png")
        self.rect = self.image.get_rect(topleft=pos)
        pygame.draw.circle(self.image, color, [radius] * 2, radius, width=0)
        self.tween = tween.easeOutBounce
        self.animation_speed = 10
        self.counter = 0

    def animate(self):
        self.counter += self.animation_speed
        y = int(self.tween(self.counter / HEIGHT) * (HEIGHT - 200))

        if self.counter >= HEIGHT:
            self.counter = 0

        self.rect.y = y

    def update(self):
        self.animate()


ball = Ball("white", (WIDTH // 2 - 100, HEIGHT // 4), 100)
ball_group = pygame.sprite.Group()
ball_group.add(ball)


# ANIMATIONS
def draw():
    root.fill("black")

    ball_group.draw(root)
    ball_group.update()

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
