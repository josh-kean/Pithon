import pygame
from letters import numSelect
import random

pygame.init()

# RGB Colors
black = (0,0,0)
white = (255,255,255)

display_width, display_height = 1000, 500

#create main game frame 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PITHON')
clock = pygame.time.Clock()
crashed = False

#set count to 0
count = 0



def numDisplay(number, x, y):
    gameDisplay.blit(number, (x, y))

def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " +str(count), True, black)
    gameDisplay.blit(text, [display_width/2,25])
    
# ~ def message_display(text):
    # ~ largeText = pygame.font.Font('freesansbold.ttf',115)
    # ~ TextSurf, TextRect = text_objects(text, largeText)
    # ~ TextRect.center = (display_width/2, display_height/2)
    # ~ gameDisplay.blit(TextSurf, TextRect)

    # ~ pygame.display.update()

    # ~ time.sleep(2)
    # ~ game_loop()
    
# ~ def crash():
    # ~ message_display("You Crashed")  


def pithon():
#sets image width
    number_width = 50
#initial number starting position
    image_x, image_y = display_width/2, display_height/2
    pi_string = ["images/three.png","images/one.png","images/four.png"]
    snake_position = [[image_x, image_y], [image_x, image_y], [image_x+number_width, image_y]]
#    x_position = [image_x, image_x, image_x+number_width]
#    y_position = [image_y, image_y, image_y]
    x_change, y_change = -50, 0
#determines starting position in array to pull from letters
    count = 2

#determines starting food position
    food_x, food_y = random.randrange(number_width,display_width-number_width,number_width), random.randrange(number_width,display_height-number_width,number_width)
    crashed = False


    while not crashed:
#allows the user to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


#makes the frame background white
        gameDisplay.fill(white)
#sets initial game score
        score(count-2)

#creates next snake body part on screen
        food = numSelect()
        numDisplay(pygame.image.load(food.piDigit(count+1)), food_x, food_y)


#generates snake body
        # ~ for x in range(1,len(pi_string)):
            # ~ numDisplay(pygame.image.load(pi_string[x]), snake_position[x][0], snake_position[x][1])
        [numDisplay(pygame.image.load(pi_string[x]), snake_position[x][0], snake_position[x][1]) for x in range(1,len(pi_string))]       

#creates user controls

            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT and x_change == 0:
                x_change = -number_width
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change == 0:
                x_change = number_width
                y_change = 0
            elif event.key == pygame.K_UP and y_change == 0:
                y_change = -number_width
                x_change = 0
            elif event.key == pygame.K_DOWN and y_change == 0:
                y_change = number_width
                x_change = 0

        snake_position[0][0] += x_change
        snake_position[0][1] += y_change

#for loop to shift everything up one
        for x in reversed(range(1,len(pi_string))):
            snake_position[x][0] = snake_position[x-1][0]
            snake_position[x][1] = snake_position[x-1][1]
            
        # ~ snake_position  = [snake_position[a-1] for a in reversed(range(1,len(pi_string)))]
#if statement to detect food collision
        if food_x == snake_position[0][0] and food_y == snake_position[0][1]:
            count +=1
            food_x, food_y = -100, -100
            pi_string.append(food.piDigit(count))
            snake_position.append([food_x,food_y])
#            y_position.append(food_y)
            food_x = random.randrange(number_width*2,display_width-number_width*2,number_width)
            food_y = random.randrange(number_width*2,display_height-number_width*2,number_width)
            while [food_x,food_y] in snake_position:
                food_x = random.randrange(number_width*2,display_width-number_width*2, number_width)
                food_y = random.randrange(number_width*2,display_height-number_width*2, number_width)



#draws snake head
        numDisplay(pygame.image.load(pi_string[0]), snake_position[0][0], snake_position[0][1])

#ends game if snake hits edge

        if snake_position[0][0] > display_width-number_width or snake_position[0][0] < 0+number_width or snake_position[0][1] > display_height-number_width or snake_position[0][1] < 0+number_width:
            crashed = True
            
        if snake_position[0] in snake_position[2:]:
            crashed = True
            
         
 

#displayes snake on screen
        #numDisplay(pygame.image.load(pi_string[0]), x_position[0], y_position[0])
   

#these two statements need to be at the end of the pithon definition

        pygame.display.update()
        clock.tick(7)

pithon()
#specific method to quit pygame
pygame.quit()
quit()
