import pygame
import random

class Button:
    global mass
    def __init__(self, path, text, x, y):
        self.im = pygame.image.load(path)
        self.path = path
        self.text = text 
        self.x = x 
        self.y = y 
        ger1 = self.im.get_rect(
        bottomright=(x, y))
        screen.blit(self.im, ger1)

class Button1(Button):
    def izobr(self):
        self.im = pygame.image.load(self.path) 
        ger1 = self.im.get_rect(
        bottomright=(self.x, self.y))
        screen.blit(self.im, ger1)
    def delete(self):
        self.im = pygame.image.load("pr1.png")
        self.path = "pr1.png"
        ger1 = self.im.get_rect(
        bottomright=(self.x, self.y))
        screen.blit(self.im, ger1)
        
def igra(screen, s, n):
    global r, r1, r2, r3
    k = []
    k1 = []
    for i in range(37):
        k1.append(list(s[i]))
    for i in range(1, 36):
        for j in range(1, 36):
            x1 = []
            x1.append(s[i][j - 1])
            x1.append(s[i - 1][j])
            x1.append(s[i + 1][j])
            x1.append(s[i][j + 1])
            x1.append(s[i - 1][j + 1])
            x1.append(s[i + 1][j + 1])
            x1.append(s[i - 1][j - 1])
            x1.append(s[i + 1][j - 1])
            d = x1.count(n)
            d1 = x1.count(0)
            if (d1 == 5 or d1 == 6) and s[i][j] == n:
                k.append([i - 1, j - 1])
                k1[i][j] = n
            elif d >= 3 and s[i][j] != n:
                i1, j1 = i - 1, j - 1
                if s[i][j] == 1:
                    del r[r.index([i1, j1])]
                if s[i][j] == 2:
                    del r1[r1.index([i1, j1])]
                if s[i][j] == 3:
                    del r2[r2.index([i1, j1])]
                if s[i][j] == 4:
                    del r3[r3.index([i1, j1])]
                k.append([i - 1, j - 1])
                k1[i][j] = n
            elif s[i][j] == n:
                k1[i][j] = 0
    return k, k1

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.k = 1
        self.top = 10
        self.s2 = []
        for i in range(height):
            self.s2.append([])
            for j in range(width):
                self.s2[i].append([])
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        s = self.left
        s1 = self.top
        m = self.cell_size
        y = self.width
        y1 = self.height
        for i in range(y1):
            for j in range(y):
                pygame.draw.rect(screen, (255, 255, 255), (s, s1, m, m), 1)
                if self.k == 1:
                    self.s2[i][j] = [s, s1]
                s = s + m
            s = self.left
            s1 = s1 + m
        self.k = 0
        
    def click(self, screen, x):
        m = self.cell_size
        for i in range(self.height):
            for j in range(self.width):
                a = self.s2[i][j][0]
                a1 = self.s2[i][j][0] + m
                b = self.s2[i][j][1]
                b1 = self.s2[i][j][1] + m
                if x[0] > a and x[0] < a1 and x[1] > b and \
                   x[1] < b1:
                       return i, j

    
class Life(Board):
    def life(self, screen, r, r1, r2, r3):
        for i in range(len(r)):
            m = self.cell_size
            s = r[i][1] * m + 1
            s1 = r[i][0] * m + 1
            pygame.draw.rect(screen, (0, 255, 0), (s, s1, m - 2, m - 2))
        for i in range(len(r1)):
            m = self.cell_size
            s = r1[i][1] * m + 1
            s1 = r1[i][0] * m + 1
            pygame.draw.rect(screen, (0, 255, 255), (s, s1, m - 2, m - 2))
        for i in range(len(r2)):
            m = self.cell_size
            s = r2[i][1] * m + 1
            s1 = r2[i][0] * m + 1
            pygame.draw.rect(screen, (255, 255, 0), (s, s1, m - 2, m - 2))
        for i in range(len(r3)):
            m = self.cell_size
            s = r3[i][1] * m + 1
            s1 = r3[i][0] * m + 1
            pygame.draw.rect(screen, (255, 0, 0), (s, s1, m - 2, m - 2))

    def start(self, screen, s, n):
        k, k1 = igra(screen, s, n)
        return k, k1
    
pygame.init()
pygame.display.set_caption('Жизнь')
size = width, height = 940, 800
screen = pygame.display.set_mode(size)
board = Life(35, 35)
board.set_view(0, 0, 20)
k = 0
font = pygame.font.Font(None, 30)
font1 = pygame.font.Font(None, 60)
k1 = 0
clock = pygame.time.Clock()
s = [[0] * 37 for _ in range(37)]
running = True
r = []
dd = 0
hh = 0
fps = 500
t = 1
dd1 = []
t1 = 1
r1 = []
r2 = []
mass = []
r3 = []
pomoch = 0
koef = 0
ggg = 0
spisok = [1, 2, 3, 4]
pygame.display.flip()
vyhod = 0
colser = 0
ss = "Начните игру"
stav1 = 0
pobeda = 0
stav2 = 0
cpec = 0
ser = [1, 1, 1, -1, -1, -1]
i21 = Button1('pr2.png', '', 820, 680)
i22 = Button1('pr2.png', '', 860, 680)
i23 = Button1('pr2.png', '', 900, 680)
i11 = Button1('pr.png', '', 820, 150)
i12 = Button1('pr.png', '', 860, 150)
i13 = Button1('pr.png', '', 900, 150)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and k1 == 0:
            k = 1
            if (event.pos[0] < 900) and (event.pos[1] < 60) and (event.pos[0] + 171 > 900) and (event.pos[1] + 47 > 60) and ggg == 0 and pomoch != 1:
                ss = "Начните игру"
                pob = -1
                posx1 = random.randint(1, 31)
                posy1 = random.randint(1, 31)
                pov1 = random.randint(1, 2)
                posx2 = posx1
                posy2 = posy1
                while ((posx2 > posx1 - 4) and (posx2 < posx1 + 4)) or ((posy2 > posy1 - 4) and (posy2 < posy1 + 4)): 
                    posx2 = random.randint(1, 31)
                    posy2 = random.randint(1, 31)
                pov2 = random.randint(1, 2)
                posx3 = posx1
                posy3 = posy1
                while ((posx3 > posx1 - 4) and (posx3 < posx1 + 4)) or ((posy3 > posy1 - 4) and (posy3 < posy1 + 4)) or \
                      ((posx3 > posx2 - 4) and (posx3 < posx2 + 4)) or ((posy3 > posy2 - 4) and (posy3 < posy2 + 4)): 
                    posx3 = random.randint(1, 31)
                    posy3 = random.randint(1, 31)
                pov3 = random.randint(1, 2)
                posx4 = posx1
                posy4 = posy1
                while ((posx4 > posx1 - 4) and (posx4 < posx1 + 4)) or ((posy4 > posy1 - 4) and (posy4 < posy1 + 4)) or \
                      ((posx4 > posx2 - 4) and (posx4 < posx2 + 4)) or ((posy4 > posy2 - 4) and (posy4 < posy2 + 4)) or \
                      ((posx4 > posx3 - 4) and (posx4 < posx3 + 4)) or ((posy4 > posy3 - 4) and (posy4 < posy3 + 4)): 
                    posx4 = random.randint(1, 31)
                    posy4 = random.randint(1, 31)
                pov4 = random.randint(1, 2)
                aa = (posx1, posy1)
                r.append(list(aa))
                s[list(aa)[0]][list(aa)[1]] = 1
                if pov1 == 1:
                    for i in range(1, 4):
                        aa = (posx1 + i, posy1)
                        r.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 1
                else:
                    for i in range(1, 4):
                        aa = (posx1, posy1 + i)
                        r.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 1
                aa = (posx2, posy2)
                r1.append(list(aa))
                s[list(aa)[0]][list(aa)[1]] = 2
                if pov2 == 1:
                    for i in range(1, 4):
                        aa = (posx2 + i, posy2)
                        r1.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 2
                else:
                    for i in range(1, 4):
                        aa = (posx2, posy2 + i)
                        r1.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 2
                aa = (posx3, posy3)
                r2.append(list(aa))
                s[list(aa)[0]][list(aa)[1]] = 3
                if pov3 == 1:
                    for i in range(1, 4):
                        aa = (posx3 + i, posy3)
                        r2.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 3
                else:
                    for i in range(1, 4):
                        aa = (posx3, posy3 + i)
                        r2.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 3
                aa = (posx4, posy4)
                r3.append(list(aa))
                s[list(aa)[0]][list(aa)[1]] = 4
                if pov4 == 1:
                    for i in range(1, 4):
                        aa = (posx4 + i, posy4)
                        r3.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 4
                else:
                    for i in range(1, 4):
                        aa = (posx4, posy4 + i)
                        r3.append(list(aa))
                        s[list(aa)[0]][list(aa)[1]] = 4
                ggg = 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ggg == 1:
            if (event.pos[0] < 750) and (event.pos[1] < 250) and (event.pos[0] + 32 > 750) and (event.pos[1] + 32 > 250) and (stav1 == 0) and (pomoch != 1):
                stav1 = 1
                if ser.count(1) == 3:
                    i13 = Button1('pr.png', '', 820, 250)
                elif ser.count(1) == 2:
                    i12 = Button1('pr.png', '', 820, 250)
                elif ser.count(1) == 1:
                    i11 = Button1('pr.png', '', 820, 250)
                elif ser.count(1) == 4:
                    i23 = Button1('pr2.png', '', 820, 250)
                elif ser.count(1) == 5:
                    i22 = Button1('pr2.png', '', 820, 250)
            if (event.pos[0] < 750) and (event.pos[1] < 350) and (event.pos[0] + 32 > 750) and (event.pos[1] + 32 > 350) and (stav1 == 0) and (pomoch != 1):
                stav1 = 2
                if ser.count(1) == 3:
                    i13 = Button1('pr.png', '', 820, 350)
                elif ser.count(1) == 2:
                    i12 = Button1('pr.png', '', 820, 350)
                elif ser.count(1) == 1:
                    i11 = Button1('pr.png', '', 820, 350)
                elif ser.count(1) == 4:
                    i23 = Button1('pr2.png', '', 820, 350)
                elif ser.count(1) == 5:
                    i22 = Button1('pr2.png', '', 820, 350)
            if (event.pos[0] < 750) and (event.pos[1] < 450) and (event.pos[0] + 32 > 750) and (event.pos[1] + 32 > 450) and (stav1 == 0) and (pomoch != 1):
                stav1 = 3
                if ser.count(1) == 3:
                    i13 = Button1('pr.png', '', 820, 450)
                elif ser.count(1) == 2:
                    i12 = Button1('pr.png', '', 820, 450)
                elif ser.count(1) == 1:
                    i11 = Button1('pr.png', '', 820, 450)
                elif ser.count(1) == 4:
                    i23 = Button1('pr2.png', '', 820, 450)
                elif ser.count(1) == 5:
                    i22 = Button1('pr2.png', '', 820, 450)
            if (event.pos[0] < 750) and (event.pos[1] < 550) and (event.pos[0] + 32 > 750) and (event.pos[1] + 32 > 550) and (stav1 == 0) and (pomoch != 1):
                stav1 = 4
                if ser.count(1) == 3:
                    i13 = Button1('pr.png', '', 820, 550)
                elif ser.count(1) == 2:
                    i12 = Button1('pr.png', '', 820, 550)
                elif ser.count(1) == 1:
                    i11 = Button1('pr.png', '', 820, 550)
                elif ser.count(1) == 4:
                    i23 = Button1('pr2.png', '', 820, 550)
                elif ser.count(1) == 5:
                    i22 = Button1('pr2.png', '', 820, 550)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (event.pos[0] < 370) and (event.pos[1] < 760) and (event.pos[0] + 171 > 370) and (event.pos[1] + 47 > 760) and pomoch != 1:
                vyhod = 1
            if (event.pos[0] < 180) and (event.pos[1] < 760) and (event.pos[0] + 171 > 180) and (event.pos[1] + 47 > 760):
                pomoch = 1
            if (event.pos[0] < 900) and (event.pos[1] < 760) and (event.pos[0] + 171 > 900) and (event.pos[1] + 47 > 760) and pomoch == 1:
                pomoch = 0
            if (event.pos[0] < 900) and (event.pos[1] < 760) and (event.pos[0] + 171 > 900) and (event.pos[1] + 47 > 760) and pobeda != 0:
                cpec = 0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and k1 == 0 and k == 1:
            k1 += 1
        if event.type == pygame.KEYDOWN and k == 1 and k1 == 0:
            if event.key == pygame.K_SPACE and stav2 != 0:
                k1 += 1
                ss = "Идет игра..."
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4 and k1 == 1:
            koef += 50
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5 and k1 == 1:
            koef -= 50
    if pomoch != 1:
        screen.fill((10, 0, 0))
    if vyhod == 1:
        break
    if cpec == 0 and pobeda != 0:
        k1 = 0
        clock = pygame.time.Clock()
        s = [[0] * 37 for _ in range(37)]
        running = True
        r = []
        dd = 0
        hh = 0
        fps = 500
        t = 1
        dd1 = []
        t1 = 1
        r1 = []
        r2 = []
        mass = []
        r3 = []
        pomoch = 0
        koef = 0
        ggg = 0
        spisok = [1, 2, 3, 4]
        pygame.display.flip()
        vyhod = 0
        colser = 0
        ss = "Начните игру"
        stav1 = 0
        pobeda = 3
        stav2 = 0
        ser = [1, 1, 1, -1, -1, -1]
        i21 = Button1('pr2.png', '', 820, 680)
        i22 = Button1('pr2.png', '', 860, 680)
        i23 = Button1('pr2.png', '', 900, 680)
        i11 = Button1('pr.png', '', 820, 150)
        i12 = Button1('pr.png', '', 860, 150)
        i13 = Button1('pr.png', '', 900, 150)
        pobeda = 0
    if pobeda == 3 and cpec == 1:
        screen.fill((10, 0, 0))
        text = font1.render("Вы победили!", True, (255, 255, 255))
        screen.blit(text, [340, 380])
        i8 = Button('vyh.png', '', 900, 760)
        pygame.display.flip()
        continue
    if pobeda == 2 and cpec == 1:
        screen.fill((10, 0, 0))
        text = font1.render("Победа ИИ!", True, (255, 255, 255))
        screen.blit(text, [340, 380])
        i8 = Button('vyh.png', '', 900, 760)
        pygame.display.flip()
        continue
    if pomoch == 1:
        screen.fill((10, 0, 0))
        text = font.render("Правила игры", True, (255, 255, 255))
        text2 = font.render("Вы играете против ИИ. Сначала нажмите на кнопку random. Вам выпадет последователь-", True, (255, 255, 255))
        text3 = font.render("ность в которой вы должны будете выбрать цвет. За один цвет ставится одна жизнь.", True, (255, 255, 255))
        text4 = font.render("Нажмите на квадратик с цветом чтобы поставить (отменить нельзя) жизнь. После ход", True, (255, 255, 255))
        text5 = font.render("ИИ. Он ставит на любой другой цвет свою жизнь. Тот кто побеждает забирает жизни со-", True, (255, 255, 255))
        text6 = font.render("перника. Всего жизней три на каждого. Победит тот кто заберет все жизни себе.", True, (255, 255, 255))
        text7 = font.render("Если же никто из вас не победил, то жизни уходят обратно к вам. Мы уверяем вас в", True, (255, 255, 255))
        text8 = font.render("нашей честности, поэтому ИИ будет выбирать абсолютно рандомно, не зная до этого кто", True, (255, 255, 255))
        text9 = font.render("победит. Сердечки рядом с персонажем - это жизни. Нажмите на пробел чтобы начать", True, (255, 255, 255))
        text10 = font.render("Ваш персонаж - сверху, персонаж ИИ снизу. Желаем вам приятной игры!", True, (255, 255, 255))
        text11 = font.render("Просто стишок, для хорошего настроения ;)", True, (255, 255, 255))
        text12 = font.render("Если плох как математик,", True, (255, 255, 255))
        text13 = font.render("Это в общем не беда,", True, (255, 255, 255))
        text14 = font.render("Ведь хороший может физик", True, (255, 255, 255))
        text15 = font.render("Получиться из тебя!", True, (255, 255, 255))
        text16 = font.render("Если физик получился,", True, (255, 255, 255))
        text17 = font.render("Скажем прямо, неказист,", True, (255, 255, 255))
        text18 = font.render("Позже может получиться", True, (255, 255, 255))
        text19 = font.render("Очень классный программист!", True, (255, 255, 255))
        text20 = font.render("Программист хреновый вышел,", True, (255, 255, 255))
        text21 = font.render("Но остался шанс один,", True, (255, 255, 255))
        text22 = font.render("Что в конце концов отличный", True, (255, 255, 255))
        text23 = font.render("Из вас выйдет сисадмин!", True, (255, 255, 255))
        screen.blit(text, [10, 10])
        screen.blit(text2, [10, 40])
        screen.blit(text3, [10, 70])
        screen.blit(text4, [10, 100])
        screen.blit(text5, [10, 130])
        screen.blit(text6, [10, 160])
        screen.blit(text7, [10, 190])
        screen.blit(text8, [10, 220])
        screen.blit(text9, [10, 250])
        screen.blit(text10, [10, 280])
        screen.blit(text11, [10, 320])
        screen.blit(text12, [10, 350])
        screen.blit(text13, [10, 380])
        screen.blit(text14, [10, 410])
        screen.blit(text15, [10, 440])
        screen.blit(text16, [10, 480])
        screen.blit(text17, [10, 510])
        screen.blit(text18, [10, 540])
        screen.blit(text19, [10, 570])
        screen.blit(text20, [10, 610])
        screen.blit(text21, [10, 640])
        screen.blit(text22, [10, 670])
        screen.blit(text23, [10, 700])
        i8 = Button('vyh.png', '', 900, 760)
        pygame.display.flip()
        continue
    board.render(screen)
    Button('knop.png', '', 900, 60)
    i1 = Button('cv1.png', '', 750, 250)
    i2 = Button('cv2.png', '', 750, 350)
    i3 = Button('cv3.png', '', 750, 450)
    i4 = Button('cv4.png', '', 750, 550)
    Button('pom.png', '', 180, 760)
    Button('vyh.png', '', 370, 760)
    Button('12.png', '', 790, 200)
    i11.izobr()
    i12.izobr()
    i13.izobr()
    Button('mil.png', '', 770, 700)
    i21.izobr()
    i22.izobr()
    i23.izobr()
    if k == 1:
        board.life(screen, r, r1, r2, r3)
        if k1 == 1:
            random.shuffle(spisok)
            for i in spisok:
                if i == 1:
                    r, s = board.start(screen, s, 1)
                if i == 2:
                    r1, s = board.start(screen, s, 2)
                if i == 3:
                    r2, s = board.start(screen, s, 3)
                if i == 4:
                    r3, s = board.start(screen, s, 4)
            pygame.time.delay(fps + koef)
            if (r == []) and ('r' not in dd1):
                dd += 1
                dd1.append('r')
            if (r1 == []) and ('r1' not in dd1):
                dd += 1
                dd1.append('r1')
            if (r2 == []) and ('r2' not in dd1):
                dd += 1
                dd1.append('r2')
            if (r3 == []) and ('r3' not in dd1):
                dd += 1
                dd1.append('r3')
            if dd > 2:
                k1 = 3
        elif k1 == 2:
            k = 1
            koef = 0
            k1 = 0
            r1 = []
            dd = 0
            r = []
            k1 = 0
            ggg = 0
            r2 = []
            dd1 = []
            s = [[0] * 37 for _ in range(37)]
            r3 = []
            if pob == stav2:
                if ser.count(1) == 3:
                    ser[2] = -1
                    i23 = Button1('pr2.png', '', 900, 680)
                    i13 = Button1('pr.png', '', 900, 730)
                elif ser.count(1) == 2:
                    ser[1] = -1
                    i12 = Button1('pr.png', '', 860, 730)
                    i13 = Button1('pr.png', '', 900, 730)
                elif ser.count(1) == 1:
                    pobeda = 2
                    cpec = 1
                elif ser.count(1) == 4:
                    ser[3] = -1
                    i23 = Button1('pr2.png', '', 900, 680)
                    i22 = Button1('pr2.png', '', 860, 680)
                elif ser.count(1) == 5:
                    ser[4] = -1
                    i22 = Button1('pr2.png', '', 860, 680)
                    i21 = Button1('pr2.png', '', 820, 680)
            elif pob == stav1:
                if ser.count(1) == 3:
                    ser[3] = 1
                    i13 = Button1('pr.png', '', 900, 150)
                    i23 = Button1('pr2.png', '', 900, 200)
                elif ser.count(1) == 2:
                    ser[2] = 1
                    i12 = Button1('pr.png', '', 860, 150)
                    i13 = Button1('pr.png', '', 900, 150)
                elif ser.count(1) == 1:
                    ser[1] = 1
                    i11 = Button1('pr.png', '', 820, 150)
                    i12 = Button1('pr.png', '', 860, 150)
                elif ser.count(1) == 4:
                    ser[4] = 1
                    i23 = Button1('pr2.png', '', 900, 200)
                    i22 = Button1('pr2.png', '', 860, 200)
                elif ser.count(1) == 5:
                    pobeda = 3
                    cpec = 1
            else:
                if ser.count(1) == 3:
                    i13 = Button1('pr.png', '', 900, 150)
                    i23 = Button1('pr2.png', '', 900, 680)
                if ser.count(1) == 2:
                    i12 = Button1('pr.png', '', 860, 150)
                    i13 = Button1('pr.png', '', 900, 730)
                if ser.count(1) == 1:
                    i11 = Button1('pr.png', '', 820, 150)
                    i12 = Button1('pr.png', '', 860, 730)
                if ser.count(1) == 4:
                    i22 = Button1('pr2.png', '', 860, 680)
                    i23 = Button1('pr2.png', '', 900, 200)
                if ser.count(1) == 5:
                    i22 = Button1('pr2.png', '', 860, 200)
                    i21 = Button1('pr2.png', '', 820, 680)
            stav1 = 0
            stav2 = 0
        elif k1 == 3:
            if 'r' not in dd1:
                pob = 4
                ss = 'Победили зеленые'
            if 'r1' not in dd1:
                pob = 2
                ss = 'Победили голубые'
            if 'r2' not in dd1:
                pob = 3
                ss = 'Победили желтые'
            if 'r3' not in dd1:
                pob = 1
                ss = 'Победили красные'
            k1 = 2
        if stav1 != 0 and stav2 == 0:
            ran = [1, 2, 3, 4]
            del ran[ran.index(stav1)]
            random.shuffle(ran)
            stav2 = ran[0]
            if stav2 == 1:
                if ser.count(-1) == 3:
                    i23 = Button1('pr2.png', '', 820, 250)
                elif ser.count(-1) == 2:
                    i22 = Button1('pr2.png', '', 820, 250)
                elif ser.count(-1) == 1:
                    i21 = Button1('pr2.png', '', 820, 250)
                elif ser.count(-1) == 4:
                    i13 = Button1('pr.png', '', 820, 250)
                elif ser.count(-1) == 5:
                    i12 = Button1('pr.png', '', 820, 250)
            if stav2 == 2:
                if ser.count(-1) == 3:
                    i23 = Button1('pr2.png', '', 820, 350)
                elif ser.count(-1) == 2:
                    i22 = Button1('pr2.png', '', 820, 350)
                elif ser.count(-1) == 1:
                    i21 = Button1('pr2.png', '', 820, 350)
                elif ser.count(-1) == 4:
                    i13 = Button1('pr.png', '', 820, 350)
                elif ser.count(-1) == 5:
                    i12 = Button1('pr.png', '', 820, 350)
            if stav2 == 3:
                if ser.count(-1) == 3:
                    i23 = Button1('pr2.png', '', 820, 450)
                elif ser.count(-1) == 2:
                    i22 = Button1('pr2.png', '', 820, 450)
                elif ser.count(-1) == 1:
                    i21 = Button1('pr2.png', '', 820, 450)
                elif ser.count(-1) == 4:
                    i13 = Button1('pr.png', '', 820, 450)
                elif ser.count(-1) == 5:
                    i12 = Button1('pr.png', '', 820, 450)
            if stav2 == 4:
                if ser.count(-1) == 3:
                    i23 = Button1('pr2.png', '', 820, 550)
                elif ser.count(-1) == 2:
                    i22 = Button1('pr2.png', '', 820, 550)
                elif ser.count(-1) == 1:
                    i21 = Button1('pr2.png', '', 820, 550)
                elif ser.count(-1) == 4:
                    i13 = Button1('pr.png', '', 820, 550)
                elif ser.count(-1) == 5:
                    i12 = Button1('pr.png', '', 820, 550)
    text23 = font.render(ss, True, (255, 255, 255))
    screen.blit(text23, [600, 730])
    clock.tick(fps)
    pygame.display.flip()
