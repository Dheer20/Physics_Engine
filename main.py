from Geometry import *
from random import randint
import math as m
import pygame

WIDTH,HEIGHT = 1200,800
FPS = 60


class Particle:
    def __init__(self,x,y):
        self.pos = Vector(x,y)
        self.vel = randint(1,4) * Vector.Random2D()
        self.acc = Vector(0,0)
        self.mass = randint(1,6)
        self.r = m.sqrt(self.mass) * 20

    def apply_force(self,force : 'Vector'):
        f = force * (1/self.mass)
        self.acc += f

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc = Vector(0,0)

def EdgeWrap(p : 'Particle'):
    if p.pos.x > WIDTH + p.r:
        p.pos.x = -p.r
    if p.pos.x < -p.r:
        p.pos.x = WIDTH + p.r
    if p.pos.y > HEIGHT + p.r:
        p.pos.y = -p.r
    if p.pos.y < -p.r:
        p.pos.y = HEIGHT + p.r

def EdgeBounce(p : 'Particle'):
    if p.pos.x > WIDTH-p.r :
        p.pos.x = WIDTH-p.r
        p.vel.x *= -1
    if p.pos.x < p.r:
        p.pos.x = p.r
        p.vel.x *= -1
    if p.pos.y > HEIGHT-p.r:
        p.pos.y = HEIGHT-p.r
        p.vel.y *= -1
    if p.pos.y < p.r:
        p.pos.y = p.r
        p.vel.y *= -1
    
def RenderLoop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Physics Engine - Particle System")
    clock = pygame.time.Clock()

    edge_behaviour = True

    particles = [Particle(randint(50,WIDTH-50),randint(50,HEIGHT-50)) for _ in range(30)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    edge_behaviour = not edge_behaviour

        screen.fill((20,20,30))

        for p in particles:

            p.update()
            if edge_behaviour:
                EdgeBounce(p)
            else:
                EdgeWrap(p)
            
            pygame.draw.circle(screen,(244,244,244),(int(p.pos.x),int(p.pos.y)),int(p.r))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    RenderLoop()


