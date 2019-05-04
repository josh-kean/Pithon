import pygame
from letters import numSelect
from settings import GameSettings, KeyBoard
import random
import time
pygame.init()

# RGB Colors
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
grey = (160, 160, 160)

display_width, display_height = 1000, 1000

#create main game frame
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PITHON')
clock = pygame.time.Clock()
crashed = False

#set count to 0
#this count controls the score display and the snake body
count = 0

def randomRange(axis, values):
    if axis == 'x':
        return random.randrange(values[0], values[1], values[2])
    if axis == 'y':
        return random.randrange(values[0], values[1], values[2])
def numDisplay(number, x, y):
    gameDisplay.blit(number, (x, y))

#add code to score that makes a box around text
def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " +str(count), True, black)
    gameDisplay.blit(text, [display_width/2,25])

def pithon(mode):
    difficulty = mode
#sets image width
    number_width = 50
#initial number starting position
    image_x, image_y = display_width/2, display_height/2
    pi_string = ["images/three.png","images/one.png","images/four.png"]
    snake_position = [[image_x, image_y], [image_x, image_y], [image_x+number_width, image_y]]
    x_change = -50
    y_change = 0
#determines starting position in array to pull from letters
#count starts at 2 so the first 3 digits of pi are displayed on screen (remember index
#starts at 0!!!)
    count = 2
    rcount = random.randrange(1,9)
    while rcount == count+1:
        rcount = random.randrange(1,9)

#determines starting food position
    randRangeList = [number_width*3, display_height-100, number_width]
    food_x, food_y = randomRange('x', randRangeList), randomRange('y', randRangeList)
    rfood_x, rfood_y = randomRange('x', randRangeList), randomRange('y', randRangeList)
    crashed = False

    event = pygame.event.poll()
    while not crashed:
#allows the user to quit the game
# events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#makes the frame background white
        gameDisplay.fill(grey)

#sets initial game score
        score(count-2)

#creates next snake body part on screen
        food = numSelect()
        numDisplay(pygame.image.load(food.piDigit(count+1)), food_x, food_y)

#creates fake food on screen if hard mode enabled
        if difficulty == 'hard':
            rfood = numSelect()
            numDisplay(pygame.image.load(rfood.piDigit(rcount)), rfood_x, rfood_y)

#generates snake body
        [numDisplay(pygame.image.load(pi_string[x]), snake_position[x][0], snake_position[x][1]) for x in range(1,len(pi_string))]

#creates user controls

        change = KeyBoard(event, x_change, y_change, number_width)
        x_change = change[0]
        y_change = change[1]

        snake_position[0][0] += x_change
        snake_position[0][1] += y_change

#for loop to shift everything up one
        for x in reversed(range(1,len(pi_string))):
            snake_position[x][0] = snake_position[x-1][0]
            snake_position[x][1] = snake_position[x-1][1]

#if statement to detect food collision
        if food_x == snake_position[0][0] and food_y == snake_position[0][1]:
            count +=1
            rcount = random.randrange(1,9)
            while rcount == count+1:
                rcount = random.randrange(1,9)
            #removes food from screen
            food_x, food_y = -100, -100
            pi_string.append(food.piDigit(count))
            snake_position.append([food_x,food_y])
            food_x = random.randrange(number_width*2,display_width-number_width*2,number_width)
            food_y = random.randrange(number_width*2,display_height-number_width*2,number_width)
            if difficulty == 'hard':
                rfood_x = random.randrange(number_width,display_width-number_width,number_width)
                rfood_y = random.randrange(number_width,display_height-number_width,number_width)
            while [food_x,food_y] in snake_position:
                food_x = random.randrange(number_width*2,display_width-number_width*2, number_width)
                food_y = random.randrange(number_width*2,display_height-number_width*2, number_width)
                if difficulty == 'hard':
                    rfood_x = random.randrange(number_width,display_width-number_width,number_width)
                    rfood_y = random.randrange(number_width,display_height-number_width,number_width)


#draws snake head
        numDisplay(pygame.image.load(pi_string[0]), snake_position[0][0], snake_position[0][1])

#ends game if snake hits edge

        if snake_position[0][0] > display_width-number_width or snake_position[0][0] < 0+number_width or snake_position[0][1] > display_height-number_width or snake_position[0][1] < 0+number_width:
            time.sleep(2)
            crashed = True
            # return crashed

        if snake_position[0] in snake_position[2:]:
            time.sleep(2)
            crashed = True
            # return crashed
        if difficulty == 'hard':
            if snake_position[0][0] == rfood_x and snake_position[0][1] == rfood_y:
                time.sleep(2)
                crashed = True
                # return crashed

#these two statements need to be at the end of the pithon definition

        # pygame.event.clear()
        pygame.display.update()
        clock.tick(7)

def start_screen():
#allows the user to quit the game
    while True:
        for action in pygame.event.get():
            crashed = False
            if action.type == pygame.QUIT:
                pygame.quit()
                quit()
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_w:
                    while crashed == False:
                        crashed = pithon(False)
                        # break
                if action.key == pygame.K_s:
                    while crashed == False:
                        crashed = pithon('hard')
                        # break
# creates white start screen

# my goal for the start page is to have an image of a snake, and to
# display overall high score.

        gameDisplay.fill(red)

        font = pygame.font.SysFont(None, 30)
        text = font.render("Press s for hard mode", True, black)
        gameDisplay.blit(text, [display_width/2,display_height/2])
        other_text = font.render("Press w for easy mode", True, black)
        gameDisplay.blit(other_text, [display_width/2, display_height/2-50])

        # pygame.event.clear()
        pygame.display.update()

start_screen()
#specific method to quit pygame
pygame.quit()
quit()
