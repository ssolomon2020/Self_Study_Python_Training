# The Ultimate Introduction to PyGame
# https://www.youtube.com/watch?v=AY9MnQ4x3zk
# Clear Code Tutorial Published July 11, 2021 on YouTube
# Project folder:
# https://github.com/clear-code-projects/UltimatePygameIntro
# Other Videos by Clear Code:
# https://www.youtube.com/c/ClearCode/
# Art and Music Sources from tutorial:
# https://opengameart.org/content/platformer-art-pixel-edition
# https://opengameart.org/content/5-chiptunes-action

# Start Script
import pygame # Import pygame module
from sys import exit # Import exit from sys module

pygame.init() # Initialize pygame

# Display Surface
screen = pygame.display.set_mode((800,400)) # Set screen as variable for display mode set to 800 x 400 pixel canvas.
pygame.display.set_caption('Pixel Runner') # Set caption text for title bar to display Pixel Runner
clock = pygame.time.Clock() # Set clock as variable for pygame time clock

test_surf = pygame.Surface((100,200)) # Set test_surf to create surface 100 x 200 pixels
test_surf.fill('Grey') # Fill test_surf surface with the color Grey

# Keep game runnning
while True: # If the while loop is true in value:
    for event in pygame.event.get(): # For an event in pygame event get:
        if event.type == pygame.QUIT: # If the event type is equal to pygame quit:
            pygame.quit() # Quit pygame
            exit() # Then Exit
    # Draw all our elements
    screen.blit(test_surf,(200,100)) # Draw blit on screen canvas from test_surf at coordinate 200,100 in window.
    
    # Update everything
    pygame.display.update()
    clock.tick(60)