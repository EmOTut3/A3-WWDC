# Initializing
import pygame # Importing the installed library pygame
from random import * # For random selection
from string import * # For some string methods
from time import * # for sleep function
pygame.init() # Initializing the library

# Variables
display_width = 1000  # The width of the game window
display_height = 800 # The height of the game window
score = -1 # Start score

gameDisplay = pygame.display.set_mode((display_width, display_height)) # Creating the game window
pygame.display.set_caption('Guess The Right Ingredient!') # Set the name of the window 
clock = pygame.time.Clock() # Initialize the clock to set FPS (Frames per second)

superlargeText = pygame.font.Font('freesansbold.ttf', 120)
largeText = pygame.font.Font('freesansbold.ttf', 50)
smallText = pygame.font.Font('freesansbold.ttf', 25)

# Special variables 
all_ingredients_array = ["blueberries", "flour", "butter", "eggs", "sugar", "strawberries", "milk", "peanut", "hammer", "screwdriver", "stick", "tomato", "battery"]
blueberry_pancake_recipe = ["blueberries", "flour", "butter", "eggs", "sugar", "milk"]
strawberry_cake_recipe = ["strawberries", "flour", "butter", "eggs", "sugar", "milk"]
croissant_recipe = ["butter", "flour", "eggs", "milk"]
gingerbread_man_recipe = ["ginger", "flour", "butter", "eggs", "sugar"]
brownie_recipe = ["chocolate", "flour", "butter", "eggs", "sugar", "milk"]
recipes_array = ["strawberry_cake", "blueberry_pancake", "croissant", "gingerbread_man", "brownie"]
recipes_dictionary = {
    "strawberry_cake" : strawberry_cake_recipe,
    "blueberry_pancake" : blueberry_pancake_recipe,
    "croissant" : croissant_recipe,
    "gingerbread_man" : gingerbread_man_recipe,
    "brownie" : brownie_recipe
}
ingredient_size = 180
recipe_size = 300
image_dictionary = {
    "battery" : pygame.transform.scale(pygame.image.load("battery_image.png"), (ingredient_size, ingredient_size)),
    "blueberries" : pygame.transform.scale(pygame.image.load("blueberry_image.png"), (ingredient_size, ingredient_size)),
    "blueberry_pancake" : pygame.transform.scale(pygame.image.load("blueberry_pancake_image.png"), (recipe_size+10, recipe_size+10)),
    "brownie" : pygame.transform.scale(pygame.image.load("brownie_image.png"), (recipe_size-20, recipe_size-20)),
    "butter" : pygame.transform.scale(pygame.image.load("butter_image.png"), (ingredient_size, ingredient_size)),
    "chocolate" : pygame.transform.scale(pygame.image.load("chocolate_image.png"), (ingredient_size, ingredient_size)),
    "croissant" : pygame.transform.scale(pygame.image.load("croissant_image.png"), (recipe_size, recipe_size)),
    "eggs" : pygame.transform.scale(pygame.image.load("eggs_image.png"), (ingredient_size, ingredient_size)),
    "flour" : pygame.transform.scale(pygame.image.load("flour_image.png"), (ingredient_size, ingredient_size)),
    "ginger" : pygame.transform.scale(pygame.image.load("ginger_image.png"), (ingredient_size, ingredient_size)),
    "gingerbread_man" : pygame.transform.scale(pygame.image.load("gingerbread_man_image.png"), (recipe_size-25, recipe_size-25)),
    "hammer" : pygame.transform.scale(pygame.image.load("hammer_image.png"), (ingredient_size, ingredient_size)),
    "milk" : pygame.transform.scale(pygame.image.load("milk_image.png"), (ingredient_size, ingredient_size)),
    "peanut" : pygame.transform.scale(pygame.image.load("peanut_image.png"), (ingredient_size, ingredient_size)),
    "screwdriver" : pygame.transform.scale(pygame.image.load("screwdriver_image.png"), (ingredient_size, ingredient_size)),
    "stick" : pygame.transform.scale(pygame.image.load("stick_image.png"), (ingredient_size, ingredient_size)),
    "strawberries" : pygame.transform.scale(pygame.image.load("strawberry_image.png"), (ingredient_size, ingredient_size)),
    "strawberry_cake" : pygame.transform.scale(pygame.image.load("strawberry_cake_image.png"), (recipe_size-20, recipe_size-20)),
    "sugar" : pygame.transform.scale(pygame.image.load("sugar_image.png"), (ingredient_size, ingredient_size)),
    "tomato" : pygame.transform.scale(pygame.image.load("tomato_image.png"), (ingredient_size, ingredient_size)),
}
intro_image = pygame.image.load("intro_image.png")
game_over_image = pygame.image.load("game_over_image.png")
menu_screen_sound = pygame.mixer.Sound("menu_screen_sound.wav")
correct_sound = pygame.mixer.Sound("correct_sound.wav")
game_over_sound = pygame.mixer.Sound("game_over_sound.wav")

# Colors
black = (0, 0, 0) 
white = (255, 255, 255)
background_pink = (246, 205, 208)
text_color = (91 ,49, 33)
orange = (151, 109, 93)
hot_pink = (219, 97, 114)
med_pink = (238, 134, 133)

# Functions
def pick_three_ingredients():
    temp_array = all_ingredients_array
    recipe_string = pick_random_option_from_array(recipes_array)
    recipe_array = recipes_dictionary[recipe_string] # Random recipe for the round
    #print(recipe_array)
    correct_ingredient = pick_random_option_from_array(recipe_array) # Correct ingredient chosen from random recipe
    
    # Create array of incorrect ingredients
    incorrect_ingredient_array = remove_common_ingredients(temp_array, recipe_array)
    
    # Pick random ingredient from array of incorrect ingredients
    incorrect_ingredient_one = pick_random_option_from_array(incorrect_ingredient_array)
    
    # Remove incorrect ingredient one so it isn't chosen twice
    incorrect_ingredient_array.remove(incorrect_ingredient_one)
    
    # Choose the second incorrect ingredient
    incorrect_ingredient_two = pick_random_option_from_array(incorrect_ingredient_array)
    
    return [recipe_string, correct_ingredient, incorrect_ingredient_one, incorrect_ingredient_two]
    
def pick_random_option_from_array(array):
    # use randint() to get a random number and len() for length of the array
    return array[randint(0, (len(array) - 1))]

def remove_common_ingredients(array1, array2):
    temp = array1[:] # Duplicate array so original is unaffected
    for item in array2:
        if item in array1:
            temp.remove(item)    
    return temp

def image(image, x, y, size=False, text=False, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.blit(image, (x,y))

    if x + size > mouse[0] > x and y + size > mouse[1] > y:
        if text:
            label_color = hot_pink        
        if click[0] == 1 and action != None:
            action()     
        #print("YAY")
    else:
        if text:
            label_color = text_color        

        #print("NO")
    if text:
        message_display(text, smallText, label_color, x + size/2, y + size + 20) # Ingredient 1 text

    # utilise image size and x coordinate to find rect for collision determination
    
def text_objects(text, text_type, color):
    textSurface = text_type.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, text_type, color, x, y):    
    TextSurf, TextRect = text_objects(text, text_type, color)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

def button(text, x, y, w, h, button_color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, hover_color,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, button_color,(x,y,w,h))

    message_display(text, smallText, white, x+(w/2), y+(h/2))
    #smallText = pygame.font.SysFont("comicsansms",20)
    #textSurf, textRect = text_objects(msg, smallText)
    #textRect.center = ( (x+(w/2)), (y+(h/2)) )
    #gameDisplay.blit(textSurf, textRect)

def quit_game():
    pygame.quit()
    quit()
    
def game_intro():
    global score

    running = True # Set gameloop to true when its running
        
    score = -1
    
    pygame.mixer.Sound.play(menu_screen_sound)

        
    while running:
        for event in pygame.event.get(): # For each captured event from player
            if event.type == pygame.QUIT: # Check if quit event
                quit_game() # Make running false to close game
        
            image(intro_image, 0, 0, size=display_width, text=False, action=main)
        
            pygame.display.update() # Update the screen

def game_over():
    global score
    
    running = True # Set gameloop to true when its running
    
    gameDisplay.fill(background_pink) # Sets pink background
    
    pygame.mixer.Sound.play(game_over_sound)

    while running:

        for event in pygame.event.get(): # For each captured event from player
            if event.type == pygame.QUIT: # Check if quit event
                quit_game() # Make running false to close game

    #print("Take this L ugly")
    
        # Text for gameover
            #message_display("GAME OVER!", superlargeText, text_color, display_width/2, display_height/2-150) # TITLE TEXT
            image(game_over_image, 0, 0, size=False, text=False, action=None)
    
        # Text for score for that game 
            message_display("Your score was: " + str(score), largeText, text_color, display_width/2, display_height/2) # TITLE TEXT
    
        # Button to go back to main menu 
            button("Main Menu", 150, display_height/1.6, 250, 60, hot_pink, med_pink, game_intro)
        
        # Button to quit game
            button("Quit", display_width-400, display_height/1.6, 250, 60, hot_pink, med_pink, quit_game)
        
            pygame.display.update() # Update the screen
        
        # do this at the end after all the screen change stuff

def main():
    global score
    
    running = True # Set gameloop to true when its running
    
    gameDisplay.fill(background_pink) # Sets pink background
    
    choice_array = pick_three_ingredients() # Choose recipe and ingredients 
    
    # pick first choice
    first_ingredient = choice_array[randint(1, 3)]
    # remove from list
    choice_array.remove(first_ingredient)
    # pick second choice
    second_ingredient = choice_array[randint(1, 2)]
    # remove from list
    choice_array.remove(second_ingredient)
    
    score = score + 1
    
    if score > 0:
        pygame.mixer.Sound.play(correct_sound)


    #print(str(50+ingredient_size/2) + ", " + str(50+ingredient_size/2+ingredient_size))
    #print(str(display_height/1.75+ingredient_size+20) + ", " + str(display_height/1.75+ingredient_size+20+ingredient_size))
    while running:

        for event in pygame.event.get(): # For each captured event from player
            if event.type == pygame.QUIT: # Check if quit event
                running = False # Make running false to close game

            #print(event)
            message_display(str(score), largeText, hot_pink, 40, 40) # TITLE TEXT

            image(image_dictionary[choice_array[0]], display_width/2-recipe_size/2, 0) # Recipe 
            message_display(capwords(choice_array[0].replace("_", " ")), smallText, text_color, display_width/2, recipe_size-20) # Recipe text
            message_display("GUESS THE RIGHT INGREDIENT!", largeText, text_color, display_width/2, display_height/2-30) # TITLE TEXT
            
            if first_ingredient in recipes_dictionary[choice_array[0]]:
                image(image_dictionary[first_ingredient], 50, display_height/1.75, ingredient_size, capwords(first_ingredient.replace("_", " ")), main) # Ingredient 1
            else:
                image(image_dictionary[first_ingredient], 50, display_height/1.75, ingredient_size, capwords(first_ingredient.replace("_", " ")), game_over) # Ingredient 1

            if second_ingredient in recipes_dictionary[choice_array[0]]:
                image(image_dictionary[second_ingredient], (display_width/2-ingredient_size/2), display_height/1.75, ingredient_size, capwords(second_ingredient.replace("_", " ")), main) # Ingredient 2
            else:
                image(image_dictionary[second_ingredient], (display_width/2-ingredient_size/2), display_height/1.75, ingredient_size, capwords(second_ingredient.replace("_", " ")), game_over) # Ingredient 2
            
            if choice_array[1] in recipes_dictionary[choice_array[0]]:
                image(image_dictionary[choice_array[1]], (display_width-ingredient_size-25), display_height/1.75, ingredient_size, capwords(choice_array[1].replace("_", " ")), main) # Ingredient 3
            else:
                image(image_dictionary[choice_array[1]], (display_width-ingredient_size-25), display_height/1.75, ingredient_size, capwords(choice_array[1].replace("_", " ")), game_over) # Ingredient 3

            pygame.display.update() # Update the screen
            clock.tick(60) # Set fps to 60

    quit_game()

# LET THE HUNGERGAMES BEGIN - Running the main function to start the game 
game_intro()
