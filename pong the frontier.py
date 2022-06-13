from ast import Pass
from pickle import FALSE
from re import L
from tkinter.tix import TEXT
import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pong")


FPS = 60 #Frames per second

WHITE = (255, 255, 255, 255)#Color variables
BLACK = (0, 0, 0)
RED = (255, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100 #Paddle size

BALL_RADIUS = 5 #ball size

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

WINNING_SCORE = 5 

#GAME OBJECTS
class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x=  x
        self.y = self.original_y=y
        self.width = width
        self.height = height

    #Draws paddle object on screen
    def draw(self, win):
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))

    #Paddle movement up/down
    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y


def draw(win, paddles, ball, left_score, right_score): 
    win.fill(BLACK) #window display color

    left_score_text = SCORE_FONT.render(f"{left_score}", 1 , WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", 1 , WHITE)
    win.blit(left_score_text,(WIDTH//4 - left_score_text.get_width()//2 , 20 ))
    win.blit(right_score_text,(WIDTH*(3/4) - right_score_text.get_width()//2 , 20 ))

    #Draws paddles
    for paddle in paddles:
        paddle.draw(win)

    #dotted middle line
    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 5, HEIGHT//20))

    #draws the ball
    ball.draw(win)

    pygame.display.update()


def handle_paddle_movement(keys, left_paddle, right_paddle):#Paddle keyboard movements
#left paddle moves with W and S keys
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

#right paddle moves with arrow keys
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN]and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)

#collisons 
def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel*= -1
    
#collision redirection 
    if ball.x_vel < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height/2
                difference_in_y = middle_y - ball.y
                reduction_factor =  (left_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height/2
                difference_in_y = middle_y - ball.y
                reduction_factor =  (right_paddle.height / 2) / ball.MAX_VEL
                y_vel = difference_in_y / reduction_factor
                ball.y_vel = y_vel * -1

class Ball:
    MAX_VEL = 8
    COLOR = RED 

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), (self.radius))

    def move(self): #ball movement
         self.x += self.x_vel
         self.y += self.y_vel
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0 
        self.x_vel *= -1


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Configures left paddle position on screen
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT) #Configures right paddle position on screen
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x <0:
            right_score += 1
            ball.reset()
        elif ball.x >WIDTH:
            left_score+= 1
            ball.reset()
        
        WON = False
        if left_score >= WINNING_SCORE:
            WON = True
            win_text = "left player won"
        elif right_score >= WINNING_SCORE:
            WON = True
            win_text = "right player won"

        if WON:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0
    pygame.quit()

if __name__ == '__main__':
    main()