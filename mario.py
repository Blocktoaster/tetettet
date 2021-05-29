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
        
level = [
       "-------------------------------",
       "-  -             -----        -",
       "-      -   -      --          -",
       "-                 -   --      -",
       "-       -     --     ---      -",
       "-         -----       -       -",
       "--        -      -      --    -",
       "-                -    --      -",
       "-      -     --           --- -",
       "-      --- -           -      -",
       "-          --             -   -",
       "-      ---     ---            -",
       "-------------------------------",
       "-------------------------------",]


class block(sprite.Sprite):
    def __init__(self, player_x, player_y):
        super().__init__()
        self.image = Surface((32,32))
        self.image.fill((200,200,0))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def move(self):
        press = key.get_pressed()
        if press[K_LEFT]:
            self.rect.x +=10
        if press[K_RIGHT]:
            self.rect.x -=10     
    

igrok = GameSprite('cactus.png',320,300)
f1 = transform.scale(image.load("fon.png"),(700, 500))
f2 = transform.scale(image.load("fon.png"),(700, 500))
f3 = transform.scale(image.load("fon.png"),(700, 500))
f4 = transform.scale(image.load("fon.png"),(700, 500))
f5 = transform.scale(image.load("fon.png"),(700, 500))
width = 32
height = 32
colorp = "#FF6262"

x1 = 0
y1 = 0
steny=[]
x=y=0 
for row in level: 
        for col in row: 
            if col == "-":
                a = block(x,y)
                #pf = Surface((width,height))
                #pf.fill(Color(colorp)) 
                #window.blit(pf,(x,y))
                steny.append(a)
            x += width 
        y += height    
        x = 0 

while game:
    window.blit(f1,(x1-700,0))
    window.blit(f2,(x1,0))
    window.blit(f3,(x1+700,0))
    #window.blit(f4,(y1,0))
    #window.blit(f5,(y1+700,0))

    for i in steny:
        i.reset()
        i.move()
        
    for e in event.get():
        if e.type == QUIT:
            game = False
    press = key.get_pressed()
    if press[K_LEFT]:
        x1 +=10
    if press[K_RIGHT]:
        x1 -=10
    if press[K_UP] or sprite.collide_rect(i,igrok):
        y1 -=10
    else:
        y1+=10
    if x1>700:
        x1 = 0
    if x1<-700:
        x1 = 0
    if y1>320:
        y1 = 320
    igrok.reset()
    igrok.rect.y=y1
    display.update()
    clock.tick(60)

