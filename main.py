from Geometry import Vector
from random import randint
from math import sqrt
import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60

class Particle:
    def __init__(self,x,y):
        self.pos = Vector(x,y)
        self.vel = Vector.Random2D()
        self.vel = randint(1,4)*self.vel 
        self.acc = Vector(0,0)
        self.mass = randint(1,6)
        self.r = sqrt(self.mass) * 20

    def applyForce(self,force : 'Vector' ):
        f = force * (1/self.mass)
        self.acc += f
    
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0,0)

def RenderLoop():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Physics Engine - Particle System")
    clock = pygame.time.Clock()

    particles = [Particle(randint(100, WIDTH-100), randint(100, HEIGHT-100)) for _ in range(15)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((20, 20, 30))

        for p in particles:
            p.update()
            # Edge wrapping
            if p.pos.x > WIDTH + p.r:
                p.pos.x = -p.r
            if p.pos.x < -p.r:
                p.pos.x = WIDTH + p.r
            if p.pos.y > HEIGHT + p.r:
                p.pos.y = -p.r
            if p.pos.y < -p.r:
                p.pos.y = HEIGHT + p.r
            
            pygame.draw.circle(screen, (255, 255, 255), (int(p.pos.x), int(p.pos.y)), int(p.r))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    RenderLoop()
