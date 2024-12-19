import pygame
import random

pygame.init()

w = 700
h = 500
screen = pygame.display.set_mode((w,h))

class Fish_food(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.x = random.randrange(0,w)
        self.rect.y = random.randrange(-300,-20)

    def update(self):
        self.rect.y += 1
        if self.rect.y > h:
            self.reset_pos()


    
class Fish(Fish_food):
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

food_list = pygame.sprite.Group()
all_list = pygame.sprite.Group()

for i in range(50):
    fish_food = Fish_food("green",  10, 10)
    fish_food.rect.x = random.randrange(w)
    fish_food.rect.y = random.randrange(h)

    food_list.add(fish_food)
    all_list.add(fish_food)

fish = Fish("red", 30,20)
all_list.add(fish)

run = False
clock = pygame.time.Clock()
score = 0
while not run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = True

    screen.fill("light blue")

    all_list.update()
    hit_list = pygame.sprite.spritecollide(fish, food_list, False)
    for i in hit_list:
        i.reset_pos()
        score = score +1
        print(score)
    all_list.draw(screen)
    

    clock.tick(20)
    pygame.display.update()

pygame.quit()


