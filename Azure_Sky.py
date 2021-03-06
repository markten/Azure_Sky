import pygame
from constants import *
from player import Player
from enemies import *
from math import pi

def direct_player(player, ldown, rdown):
    if ldown == True and rdown == True:
        player.direction = 0
    if ldown == True and rdown == False:
        player.direction = -1
    if ldown == False and rdown == True:
        player.direction = 1
    if ldown == False and rdown == False:
        player.direction = 0

def check_bullet_age(bullet_group):
    
    removed_bullets = pygame.sprite.Group()
    
    for bullet in bullet_group:
        if bullet.age > MAX_BULLET_AGE:
            removed_bullets.add(bullet)
    
    return removed_bullets

### Main Loop
def main():

    ### Initialize the pygame & screen/window
    pygame.init()
    SIZE = ( WINDOW_X_SIZE, WINDOW_Y_SIZE)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("GWGD - Intro to Python Game")
    screen.fill(BLACK)
    font = pygame.font.Font("fonts/nokiafc22.ttf", 12)

    ### Create clock and timers
    clock = pygame.time.Clock()
    pygame.time.set_timer(STREAM_TIMER, 3000)
    pygame.time.set_timer(CLUSTER_TIMER, 2000)
     
    ### Define important game variables
    running = True
    playing_game = False
    at_title_screen = True
    score = 0
    ldown = False
    rdown = False
    bullet_timer = 0
    make_stream = False
    make_cluster = False
    player_damage_type = NONE
    boss_damage_type = NONE
    
    ### Play music if desired
    GAME_MUSIC = pygame.mixer.Sound("sounds/Rymdkraft_Ultramumie.wav")
    GAME_MUSIC.play()
    
    ### Create Groups
    enemy_bullet_list = pygame.sprite.Group()
    player_bullet_list = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    ### Instantiate sprites
    player = Player()
    all_sprites.add(player)
    boss = Boss()
    all_sprites.add(boss)
    
    while running:
        ### Begin even processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ldown = True
                if event.key == pygame.K_RIGHT:
                    rdown = True
                if event.key == pygame.K_RETURN:
                    playing_game = True
                    at_title_screen = False
                if event.key == pygame.K_SPACE:
                    player_bullet_list.add(generate_player_bullet(player.rect.centerx, player.rect.centery))
                    all_sprites.add(player_bullet_list)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ldown = False
                if event.key == pygame.K_RIGHT:
                    rdown = False
            if event.type == STREAM_TIMER:
                make_stream = True
            if event.type == CLUSTER_TIMER:
                make_cluster = True
        ### End event processing
      
        if playing_game:
            ### Begin game logic
            
            #
            if make_cluster == True:
                temp_group = generate_bullet_cluster(boss.rect.centerx, boss.rect.centery)
                enemy_bullet_list.add(temp_group)
                all_sprites.add(temp_group)
                
            if make_stream == True:
                temp_group = generate_bullet_stream(boss.rect.centerx, boss.rect.centery)
                enemy_bullet_list.add(temp_group)
                all_sprites.add(temp_group)
            
            #
            temp_group = check_bullet_age(enemy_bullet_list)
            enemy_bullet_list.remove(temp_group)
            all_sprites.remove(temp_group)
            
            # Player Collisions
            bullet_collision_list = pygame.sprite.spritecollide(player, enemy_bullet_list, True)
            for bullet in bullet_collision_list:
                player_damage_type = player.damage()
            
            # Boss Collisions
            bullet_collision_list = pygame.sprite.spritecollide(boss, player_bullet_list, True)
            for bullet in bullet_collision_list:
                boss_damage_type = boss.damage()
 
            if player_damage_type == DEATH:
                playing_game = False
                at_title_screen = True
                print("Player died")
            
            if boss_damage_type == DEATH:
                playering_game = False
                at_title_screen = True
                print("You Win: The boss was defeated")
            
            direct_player(player, ldown, rdown)
            all_sprites.update()
            
            ### End game logic
         
         
            ### Begin drawing screen
            screen.fill(AZURE)
            
            # Create score box & Health indicator
            pygame.draw.rect(screen, BLACK, [ 0, 0, WINDOW_X_SIZE, 30])
            pygame.draw.line(screen, GRAY, [ 0, 30], [ WINDOW_X_SIZE, 30], 3)
            scoretext = font.render("Score: " + str(score), True, WHITE)
            screen.blit(scoretext, [ 10, 10])
            
            shieldtext = font.render("Shield: " + str(player.current_shields), True, WHITE)
            screen.blit(shieldtext, [ 200, 10])
            
            hptext = font.render("Health: " + str(player.current_hitpoints), True, WHITE)
            screen.blit(hptext, [ 300, 10])
            
            bosshptext = font.render("Boss Health: " + str(boss.current_hitpoints), True, WHITE)
            screen.blit(bosshptext, [ 400, 10])
            
            # Draw Sprites
            all_sprites.draw(screen)
            
            # Draw shields
            if player_damage_type == SHIELD_DAMAGE:
                pygame.draw.arc(screen, BLUE, [ player.rect.x, player.rect.y, player.rect.w, player.rect.h],  0, pi, 2)
            if player_damage_type == HP_DAMAGE:
                pygame.draw.arc(screen, RED, [ player.rect.x, player.rect.y, player.rect.w, player.rect.h],  0, pi, 1)
            
            # Update display
            pygame.display.flip()
            
            ### End drawing screen
            
            score += 1
            player_damage_type = NONE
            boss_damage_type = NONE
            bullet_timer += 1
            make_stream = False
            make_cluster = False
            if bullet_timer > 60:
                bullet_timer = 0
            
            
        
        if at_title_screen:
            all_sprites.remove(enemy_bullet_list)
            all_sprites.remove(player_bullet_list)
            enemy_bullet_list.remove(enemy_bullet_list)
            player_bullet_list.remove(player_bullet_list)
            player.reset()
            boss.reset()
            
            screen.fill(AZURE)
            titletext = font.render("Press Enter to Begin...", True, WHITE)
            screen.blit(titletext, [ 300, 10])
            pygame.display.flip()
        
        ### Limit FPS
        clock.tick(20)

    pygame.quit()

if __name__ == "__main__":
    main()