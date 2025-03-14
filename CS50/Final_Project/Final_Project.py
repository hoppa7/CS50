import pygame, random, math
pygame.init()

#Colors
white = (255,255,255)
#Screen
screen_width = 600
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))
#Circle params
velocity = 10
circle_pos = screen_width // 2, screen_height // 2
radius = 15
#Rect1 params
x1 = 0
y1 = 150
width = 10
height = 150
#Rect2 params
x2 = screen_width - width
y2 = 150

pygame.display.set_caption("Pong Project")

class Circle:
    def __init__(self):
        self.y = screen_height // 2
        self.x = screen_width // 2
        self.speed = 10
        self.speed_limit = 12
        self.set_random_direction()

    def enforce_speed_limit(self):
        speed = (self.dx ** 2 + self.dy ** 2) ** 0.5
        if speed > self.speed_limit:
            scale = self.speed_limit / speed
            self.dx *= scale
            self.dy *= scale

    def set_random_direction(self):
        angle = random.uniform(0, math.pi)
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def draw(self):
        pygame.draw.circle(screen, white, (self.x, self.y), radius)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if not 0 < self.x < screen_width:
            self.dx = -self.dx
        if not 0 < self.y < screen_height:
            self.dy = -self.dy

        if self.y - radius < 0 or self.y + 15 > screen_height:
            self.dy *= -1

    def reset_circle(self):
        self.y = screen_height // 2
        self.x = screen_width // 2
        self.speed = 15
        self.set_random_direction()

run = True

circle = Circle()
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    circle.move()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y2 > velocity - 1:
        y2 -= velocity
    if keys[pygame.K_DOWN] and y2 < 450 - height:
        y2 += velocity

    if keys[pygame.K_w] and y1 > velocity - 1:
        y1 -= velocity
    if keys[pygame.K_s] and y1 < 450 - height:
        y1 += velocity

    if (circle.x - radius < x1 + width and
    y1 < circle.y < y1 + height):
        if circle.dx < 0:  
            circle.dx *= -1.2
            circle.enforce_speed_limit()
            circle.dy *= 1



    if (circle.x + radius > x2 and
        y2 < circle.y < y2 + height):
        if circle.dx > 0:  
            circle.dx *= -1.2
            circle.enforce_speed_limit()
            circle.dy *= 1

    if circle.x - radius < 0 or circle.x + radius > screen_width:
        circle.reset_circle()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, white, (x1, y1, width, height))
    pygame.draw.rect(screen, white, (x2, y2, width, height))
    circle.draw()
    pygame.display.update()

pygame.quit()

