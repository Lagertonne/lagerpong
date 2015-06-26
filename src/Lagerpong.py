'''
Created on 26.06.2015

@author: lagertonne
'''

import sys
import pygame
from pygame.locals import *


def main():
    pygame.init()
    
    paddleWidth = 15
    gapPaddle = 15
    
    size = width, height = 640, 480
    speed = [1, 2]
    black = 0, 0, 0
    red = 255, 1, 1
    green = 0, 255, 0
    white = 255, 255, 255
    paddleSpeed = 3
    

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(size)

    leftPaddle = pygame.Rect( (15, 0) , (paddleWidth, 35))
    rightPaddle = pygame.Rect( (size[0]-paddleWidth-gapPaddle, 0) , (paddleWidth, 35) )
    
    ball = pygame.Rect( (size[0] / 2, size[1] / 2) , (10, 10) )
        
      
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed()
    
        screen.fill(black)
        
        if keys[K_DOWN]:
            if( (leftPaddle.top + leftPaddle.height) != size[1]):
                leftPaddle = leftPaddle.move(0, paddleSpeed)
                print("DOWN pressed")
        if keys[K_UP]:
            if( leftPaddle.top != 0):
                leftPaddle = leftPaddle.move(0, -paddleSpeed)
                print("UP pressed")
        
        if keys[K_s]:
            if( (rightPaddle.top + rightPaddle.height) != size[1]):
                rightPaddle = rightPaddle.move(0,paddleSpeed)
                print("W pressed")
        if keys[K_w]:
            if (rightPaddle.top != 0):
                rightPaddle = rightPaddle.move(0, -paddleSpeed)
                print("S pressed")
                
        if( ball.top <= 0):
            speed[1] = -speed[1]
        if( ball.bottom >= size[1] ):
            speed[1] = -speed[1]
        if( ball.left <= leftPaddle.right and ball.top >= leftPaddle.top and ball.bottom <= leftPaddle.bottom):
            speed[0] = -speed[0]
            print("Collision LEFT!")
        if( ball.right >= rightPaddle.left and ball.top >= rightPaddle.top and ball.bottom <= rightPaddle.bottom):
            speed[0] = -speed[0]
            print("Collision RIGHT!")
            
        ball = ball.move(speed[0], speed[1])        
                
                
        pygame.draw.rect(screen, red, (leftPaddle.left, leftPaddle.top, leftPaddle.width, leftPaddle.height), 0)
        pygame.draw.rect(screen, green, (rightPaddle.left, rightPaddle.top, rightPaddle.width, rightPaddle.height), 0)
        pygame.draw.rect(screen, white, (ball.left, ball.top, ball.width, ball.height), 0)
        
        clock.tick(80)
        
        pygame.display.flip()
if __name__ == '__main__':
    main()
