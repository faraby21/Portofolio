import pygame
import time
pygame.init()
back = (170,200,3)
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x = 0, y = 0, width = 10, height = 10 , color = None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color,self.rect)
    def outline(self, frame_color,thickness):
        pygame.draw.rect(mw,frame_color,self.rect,thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True,text_color)
    def draw(self,shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image,(self.rect.x + shift_x,self.rect.y + shift_y))

Red = (255,0,0)
Green =(0,255,51)
Yellow = (255,255,0)
Dark_Blue = (0,0,255)
cards = []
num_cards = 4
x = 40

for i in range(num_cards):
    new_card = Label(x,170,70,100,Yellow)
    new_card.outline(Dark_Blue,10)
    new_card.set_text('Click',26)
    cards.append(new_card)
    x = x + 90



time_text = Label(0,0,50,50,back)
time_text.set_text('Time:',40,Dark_Blue)
time_text.draw(20,20)

timer = Label(50,55,50,40,back)
timer.set_text('0',40,Dark_Blue)
timer.draw(0,0)

score_text = Label(380,0,50,50,back)
score_text.set_text('Count:',45,Dark_Blue)
score_text.draw(20,20)

score = Label(430,55,50,40,back)
score.set_text('0',40,Dark_Blue)
score.draw(0,0)

start_time = time.time()
cur_time = start_time
points = 0
wait = 0
from random import randint
while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color((255,255,0))
            if (i + 1) == click:
                cards[i].draw(10,40)
            else:
                cards[i].fill()

    else:
        wait -= 1

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i + 1 == click:
                        cards[i].color(Green)
                        points += 1
                    else:
                        cards[i].color(Red)
                        points -= 1
                    cards[i].fill()
                    score.set_text(str(points),40,Dark_Blue)
                    score.draw(0,0)
    new_time = time.time()

    if int(new_time) - int(cur_time) == 1:
        timer.set_text(str(int(new_time - start_time)),40,Dark_Blue)
        timer.draw(0,0)
        cur_time = new_time
        
    if new_time - start_time >= 11:
        win = Label(0,0,500,500,Green)
        win.set_text("Time's up!!!",60,Dark_Blue)
        win.draw(140,180)
        break

    if points >= 5:
        win = Label(0,0,500,500,Green)
        win.set_text('You win!!!',60,Dark_Blue)
        win.draw(140,180)
        resul_time = Label(90,230,250,250,Green)
        resul_time.set_text(
            'Completion time: ' + str(int(new_time - start_time)) + 'sec',40,Dark_Blue
        )
        break

    pygame.display.update()
    clock.tick(40)


pygame.display.update()