import pygame
import time
import random
pygame.font.init()

# for window you need a width and a height
WIDTH, HEIGHT = 1000, 800
Win = pygame.display.set_mode((WIDTH, HEIGHT))  # Pass as a tuple

Space_background = pygame.transform.scale(pygame.image.load("Space_background.jpeg"), (WIDTH, HEIGHT)) #this loads the BG image

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 10
PROJECTILE_WIDTH = 8
PROJECTILE_HEIGHT = 18
PROJECTILE_VEL = 5
FONT = pygame.font.SysFont("Arial", 40)

# put draw in a separate function
def draw(player, elapsed_time, projectiles):
    Win.blit(Space_background, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    Win.blit(time_text, (10, 10))

    pygame.draw.rect(Win, "Orange", player)

    for projectile in projectiles:
        pygame.draw.rect(Win, "red", projectile)

    pygame.display.update()

# SET CAPTION FOR THE Window
pygame.display.set_caption("Space Fire")

def main():
    run = True

    # CHARACTER
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    # Projectiles with increasing difficulty as time goes on
    projectile_increments = 2000
    projectile_count = 0

    projectiles = []
    hit = False

    while run:
        projectile_count += clock.tick(40)
        elapsed_time = time.time() - start_time

        if projectile_count > projectile_increments:
            for _ in range(4):
                projectile_x = random.randint(0, WIDTH - PROJECTILE_WIDTH)
                projectile = pygame.Rect(projectile_x, -PROJECTILE_HEIGHT, PROJECTILE_WIDTH, PROJECTILE_HEIGHT)
                projectiles.append(projectile)
            
            projectile_increments = max(200, projectile_increments - 50)
            projectile_count = 0

        # Check for window close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_b] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for projectile in projectiles[:]:  # Loop over a copy of the list
            projectile.y += PROJECTILE_VEL  # Move projectile down
            if projectile.y > HEIGHT:
                projectiles.remove(projectile)
            elif projectile.colliderect(player):
                projectiles.remove(projectile)
                hit = True
                break

        if hit:
            game_over_text = FONT.render("Game Over!", 1, "Red")
            Win.blit(game_over_text, (WIDTH / 2 - game_over_text.get_width() / 2, HEIGHT / 2 - game_over_text.get_height() / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, projectiles)

    pygame.quit()

if __name__ == "__main__":
    main()
