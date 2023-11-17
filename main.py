import math
import random
import random as rnd
from random import choice

import pygame
t=0
G=0.7
FPS = 30
POINTS = 0
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
class EnemyGun:
    def __init__(self, screen):
        self.screen = screen
        self.power = 3
        self.x = 40
        self.y = 500
        self.an = 1
        self.color = RED
        self.term = 1

    def moveVverh(self):
        self.y = self.y - 3

    def moveVniz(self):
        self.y = self.y + 3

    def fire2_end(self):
        global enemy_ball
        new_ball = EnemyBall(self.screen, self.x, self.y)
        new_ball.r += 5
        new_ball.vx = self.power * math.cos(self.an)
        new_ball.vy = - self.power * math.sin(self.an)

        enemy_ball.append(new_ball)
        self.power = choice(range(4, 10))

    def draw(self):
        power = self.power
        x = self.x + math.sin(self.an) + power * math.cos(self.an)
        y = self.y - math.cos(self.an) + power * math.sin(self.an)
        pygame.draw.line(surface=self.screen, color=self.color, start_pos=[self.x, self.y], end_pos=[x, y], width=10)
        pygame.draw.rect(
            self.screen,
            RED,
            (self.x - 20, self.y, 40, 30),
        )

    def enemy_targetting(self):
        if self.an >= math.pi / 2:
            self.term = -1
        if self.an <= -math.pi / 2:
            self.term = 1
        self.an += 0.1 * self.term
        n = choice(range(20))
        if n in [0, 19]:
            self.fire2_end()
class EnemyBall:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.color = GREY

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 0.1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x, self.y),
            self.r - 3
        )

    def enemy_hittest(self, obj):
        if self.x >= obj.x - 24 and self.x <= obj.x + 24 and self.y >= obj.y - 10 and self.y <= obj.y + 20:
            return True
        return False


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 2
        self.type_of_ball = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.type_of_ball == 0:
            self.x += self.vx
            v=self.vy
            self.vy -= 0.8
            self.y -=self.vy
            if self.x + self.r >= WIDTH + 2:
                self.vx *= -0.8
                self.x = WIDTH - self.r
            elif self.x - self.r <= 0:
                self.vx *= -0.8
                self.x = self.r + 1
            elif self.y + self.r >= HEIGHT + 2:
                self.vy *= -0.8
                self.live=self.live-1
                self.y -= self.r + 1
            elif self.y - self.r <= 0 + 5:
                self.vy *= -0.8
                if self.type_of_ball == 0:
                    self.y = self.r + 6
        else:
            self.x += self.vx
            self.y -= self.vy


    def draw(self):
        if(self.live>=0):
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r)


    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if  (self.r + obj.r) ** 2 > (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 :
            return True
        else:
            return False



# def snaip(gun1,gun2):
#         gun1.vy=1
#         gun1.vx=1

class Rect:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 2

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.x += self.vx
        v=self.vy
        self.vy -= 0.8
        self.y -=self.vy
        if self.x + self.r >= WIDTH + 2:
            self.vx *= -0.8
            self.x = WIDTH - self.r
        elif self.x - self.r <= 0:
            self.vx *= -0.8
            self.x = self.r + 1
        elif self.y + self.r >= HEIGHT + 2:
            self.vy *= -0.8
            self.y -= self.r + 1
            self.live-=1
        elif self.y - self.r <= 0 + 5:
            self.vy *= -0.8
            self.y = self.r + 6

    def draw(self):
        if (self.live >= 0):
            pygame.draw.rect(
                self.screen,
                self.color,
                (self.x, self.y,self.r+8,self.r+8),
                )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if  (self.r + obj.r) ** 2 > (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 :
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.y = 550
        self.x = 50
    def moveleft(self):
        self.x=self.x-6
    def moveright(self):
        self.x=self.x+6
    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen,self.x,self.y)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def fire2_rect(self, event):
            global rects, bullet
            bullet += 1
            new_rect = Rect(self.screen,self.x,self.y)
            new_rect.r += 5
            self.an = math.atan2((event.pos[1] - new_rect.y), (event.pos[0] - new_rect.x))
            new_rect.vx = self.f2_power * math.cos(self.an)
            new_rect.vy = - self.f2_power * math.sin(self.an)
            balls.append(new_rect)
            self.f2_on = 0
            self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if(event.pos[0]==20):
                self.an = math.atan((event.pos[1] - 450) / (event.pos[0] - 21))
            else:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        power = self.f2_power
        x = self.x + math.sin(self.an) + power * math.cos(self.an)
        y = self.y - math.cos(self.an) + power * math.sin(self.an)
        pygame.draw.line(surface=self.screen, color=self.color, start_pos=[self.x, self.y],end_pos=[x, y], width=10)
        pygame.draw.rect(
            self.screen,
            RED,
            (self.x-20, self.y, 40, 30),
        )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY



class Target:
    def __init__(self, color):
        self.r = rnd.randint(7, 35)
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.color = color
        self.vx = 2
        self.vy = 2
        self.live = 1
        self.points = 0
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def vzryv(self):
        for i in range (3):
            self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.r = rnd.randint(10, 20)
        color = self.color = RED
        self.live = 1
    def new_target2(self):
        """ Инициализация новой цели 2. """
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.r = rnd.randint(10, 20)
        self.color = BLUE
        self.live = 1
    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def move(self):
        ''' Движение мишени'''

        self.x += self.vx
        self.y += self.vy

        if self.x + self.r >= WIDTH - 2:
            self.vx *= -0.8
            self.x = WIDTH - self.r - 3


        elif self.x - self.r <= 0:

            self.vx *= -0.8
            self.x = self.r + 1
        elif self.y + self.r >= HEIGHT - 2:
            self.live -= 1

            self.vy *= -0.8
            self.y -= self.r + 1

        elif self.y - self.r <= 0 + 5:
            self.vy *= -0.8
            self.y = self.r + 6

    def speed(self):
        if self.points < 5:
            self.vx = 0
            self.vy = 0
        else:
            if (self.vx == 0):
                self.vx = 2 * (self.points - 1)
            if (self.vy == 0):
                self.vy = 2 * (self.points - 1)

    def draw(self):
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.r)

    def move2(self):
        self.x += self.vx
        self.y -=self.vy
        if self.x + self.r >= WIDTH + 2:
            self.vx *= -0.8
            self.x = WIDTH - self.r
        elif self.x - self.r <= 0:
            self.vx *= -0.8
            self.x = self.r + 1
        elif self.y + self.r >= HEIGHT + 2:
            self.vy *= -0.8
            self.y -= self.r + 1
        elif self.y - self.r <= 0 + 5:
            self.vy *= -0.8
            self.y = self.r + 6


class EvilGun:
    def __init__(self, screen):
        self.screen = screen
        self.power = 3
        self.x = 0
        self.y = 0
        self.an = 1
        self.color = RED
        self.term = 1

    def fire2_end(self):
        global enemy_ball
        new_ball = EnemyBall(self.screen, self.x, self.y)
        new_ball.r += 5
        new_ball.vx = self.power * math.cos(self.an)
        new_ball.vy = - self.power * math.sin(self.an)

        enemy_ball.append(new_ball)
        self.power = choice(range(4, 10))

    def draw(self):
        angle = self.an
        dx = 30
        self.x = 20 + dx * math.cos(angle)
        self.y = 300 + dx * math.sin(angle)
        pygame.draw.line(self.screen, self.color, (20, 300), (self.x, self.y), width=5)

    def enemy_targetting(self):
        if self.an >= math.pi / 2:
            self.term = -1
        if self.an <= -math.pi / 2:
            self.term = 1
        self.an += 0.1 * self.term
        n = choice(range(20))
        if n in [0, 19]:
            self.fire2_end()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
enemy_ball = []
rects = []
count=0
count2=0
whose=0
shoot=0;
background = pygame.image.load('9225.jpg').convert()
background = pygame.transform.smoothscale(background, screen.get_size())
pygame.font.init()
my_font = pygame.font.SysFont('Lora', 20)
clock = pygame.time.Clock()
gun = Gun(screen)
gun2 = EnemyGun(screen)
target = Target(RED)
target2 = Target(BLUE)
finished = False
lives = 5

while not finished:
    # screen.fill(WHITE)
    screen.blit(background, (0, 0))
    gun.draw()
    gun2.draw()
    target.draw()
    target.speed()
    target2.draw()
    target2.speed()
    target.move2()
    target2.move2()
    gun2.draw()
    gun2.enemy_targetting()

    for i in enemy_ball:
        i.draw()
        i.move()

    # if(shoot==1):
    #     gun2.draw()
    for i in enemy_ball:
        i.draw()
    for b in balls:
        b.draw()
    for r in rects:
        r.draw()

    keys = pygame.key.get_pressed()
    text_surface = my_font.render(f'Осталось до смерти: {lives}', True, BLACK)
    screen.blit(text_surface, (10, 40))

    pygame.display.update()

    for i in enemy_ball:
        if i.enemy_hittest(gun):
            lives -= 1
            enemy_ball.remove(i)
        if lives <= 0:
            my_font = pygame.font.SysFont('Lora', 70)
            screen.fill(WHITE)
            text_surface = my_font.render(f'Game Over', True, BLACK)
            screen.blit(text_surface, (270, 250))
            pygame.display.update()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    if keys[pygame.K_a]:
        gun.moveleft()
    if keys[pygame.K_UP]:
        gun2.moveVverh()
    if keys[pygame.K_DOWN]:
        gun2.moveVniz()
    if keys[pygame.K_d]:
        gun.moveright()
    # if keys[pygame.K_SPACE]:
    #     gun2.snaip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            whose+=1
            if(whose%2==0):
                gun.fire2_end(event)
            else:
                gun.fire2_rect(event)

        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    if count==0:
        target.speed()
        count+=1
    if count2==0:
        target2.speed()
        count2+=1
    for b in balls:
        (b.move())
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target2()
    for r in rects:
        (r.move())
        if r.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if r.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            target2.new_target2()
    gun.power_up()

pygame.quit()


















































































