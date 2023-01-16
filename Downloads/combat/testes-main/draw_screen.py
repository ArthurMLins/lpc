import pygame


def draw_object(screen, player):
    # draw L left
    list_reacts = []
    
    l_left_1 = pygame.draw.rect(screen, "#c29f2e", (110, 300, 50, 20))
    l_left_1 = l_left_1.colliderect(player)
    list_reacts.append(l_left_1)
    
    l_left_2 = pygame.draw.rect(screen, "#c29f2e", (140, 320, 20, 160))
    l_left_2 = l_left_2.colliderect(player)
    list_reacts.append(l_left_2)
    
    l_left_3 = pygame.draw.rect(screen, "#c29f2e", (110, 480, 50, 20))
    l_left_3 = l_left_3.colliderect(player)
    list_reacts.append(l_left_3)
    
    #draw L right
    l_right_1 = pygame.draw.rect(screen, "#c29f2e", (840, 300, 50, 20))
    l_right_1 = l_right_1.colliderect(player)
    list_reacts.append(l_right_1)
    
    l_right_2 = pygame.draw.rect(screen, "#c29f2e", (840, 320, 20, 160))
    l_right_2 = l_right_2.colliderect(player)
    list_reacts.append(l_right_2)
    
    l_right_3 = pygame.draw.rect(screen, "#c29f2e", (840, 480, 50, 20))
    l_right_3 = l_right_3.colliderect(player)
    list_reacts.append(l_right_3)
    
    #upper rectangle
    rec_1 = pygame.draw.rect(screen, "#c29f2e", (480, 155, 40, 100))
    rec_1 = rec_1.colliderect(player)
    list_reacts.append(rec_1)
    
    #lower rectangle
    rec_2 = pygame.draw.rect(screen, "#c29f2e", (480, 545, 40, 100))
    rec_2 = rec_2.colliderect(player)
    list_reacts.append(rec_2)
    
    #right rectangle
    rec_3 = pygame.draw.rect(screen, "#c29f2e", (255, 380, 100, 40))
    rec_3 = rec_3.colliderect(player)
    list_reacts.append(rec_3)
    
    #left rectangle
    rec_4 = pygame.draw.rect(screen, "#c29f2e", (645, 380, 100, 40))
    rec_4 = rec_4.colliderect(player)
    list_reacts.append(rec_4)
    
    #draw screen
    screen_1 = pygame.draw.rect(screen, "#c29f2e", (0, 50, 1000, 25))
    screen_1 = screen_1.colliderect(player)
    list_reacts.append(screen_1)
    
    screen_2 = pygame.draw.rect(screen, "#c29f2e", (0, 725, 1000, 25))
    screen_2 = screen_2.colliderect(player)
    list_reacts.append(screen_2)
    
    screen_3 = pygame.draw.rect(screen, "#c29f2e", (975, 75,25, 1000))
    screen_3 = screen_3.colliderect(player)
    list_reacts.append(screen_3)
    
    screen_4 = pygame.draw.rect(screen, "#c29f2e", (0, 75, 25, 1000))
    screen_4 = screen_4.colliderect(player)
    list_reacts.append(screen_4)
    
    # collision detection
    if True in list_reacts:
        return False
    else:
        return True
