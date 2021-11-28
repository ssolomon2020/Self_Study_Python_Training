import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    # print(current_time)

pygame.init()
screen = pygame.display.set_mode((800,400)) # Set application canvas area
pygame.display.set_caption('Pixel Runner') # Set Title Bar Text
clock = pygame.time.Clock() # Create variable to call Clock
test_font = pygame.font.SysFont('8514oem.fon', 50) # Create variable to call system font
game_active = True
start_time = 0 

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/Ground.png').convert_alpha()

# score_surf = test_font.render('Pixel Runner', False, 'Black').convert_alpha()
# score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/Snail/Snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,304))
# snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player1.1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,303))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 303:
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 303:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        # if event.type == pygame.KEYUP:
        #    print('key up')
    
    if game_active:
        screen.blit(sky_surface,(0,0)) # Draw sky png at 0,0 coordinate
        screen.blit(ground_surface,(0,300)) # Draw ground starting at 0,300 coordinate
        #pygame.draw.rect(screen, '#c0e8ec',score_rect) # Draw rectangle on score rectangle
        #pygame.draw.rect(screen, '#c0e8ec',score_rect,10) # Draw rectangle around score rectangle
        # pygame.draw.ellipse(screen, 'Brown',pygame.Rect(50,200,100,100)) # Draw and fill ellipse with color brown at coordinates
        #screen.blit(score_surf,score_rect) # Call score_surf and rectangle variables and draw on canvas
        display_score()

        # Snail
        snail_rect.x -= 10
        if snail_rect.right <= 0: snail_rect.left = 800
        screen.blit(snail_surf,snail_rect)

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]
        #    print('jump')

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 303: player_rect.bottom = 303
        screen.blit(player_surf,player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #    print('jump')

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())

    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60) # Set clock to 60 updates a second
