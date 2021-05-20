from pygame import*
from random import*
game= True
window = display.set_mode((700,500))
display.set_caption("tettet")

clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,66))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
igrok = GameSprite('goose.jpg',0,0)
f1 = transform.scale(image.load("fon.png"),(700, 500))
f2 = transform.scale(image.load("fon.png"),(700, 500))
f3 = transform.scale(image.load("fon.png"),(700, 500))

x1 = 0

while game:
    window.blit(f1,(x1-700,0))
    window.blit(f2,(x1,0))
    window.blit(f3,(x1+700,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    press = key.get_pressed()
    if press[K_LEFT]:
        x1 +=10
    if press[K_RIGHT]:
        x1 -=10
    if x1>700:
        x1 = 0
    if x1<-700:
        x1 = 0
    igrok.reset()
    display.update()
    clock.tick(60)