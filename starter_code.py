import pygame, random

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()
# Define Classes
class Game():
    """A class to help control and update gameplay"""

    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
        """Initialize the game"""
        self.player = player
        self.alien_group = pygame.sprite.Group()
        self.alien_bullet_group = pygame.sprite.Group()
        self.player_bullet_group = pygame.sprite.Group()
    def update(self):
        """Update the game"""
        self.player.update()
        self.alien_group.update()
        self.alien_bullet_group.update()
    def draw(self):
        """Draw the game"""
        self.player.draw(display_surface)
        self.alien_group.draw(display_surface)
        self.alien_bullet_group.draw(display_surface)
        self.player_bullet_group.draw(display_surface)
    def shift_aliens(self):
        """Shift the aliens"""


    def check_collisions(self):
        """Check for collisions"""
        check_alien_collisions = pygame.sprite.spritecollide(self, self.alien_group, False)
        check_player_collisions = pygame.sprite.spritecollide(self, self.player_bullet_group, False)

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""

    def start_new_round(self):
        """Start a new round"""


    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        check_player_status = pygame.sprite.spritecollide(self, self.player_bullet_group, False)
        check_alien_status = pygame.sprite.spritecollide(self, self.alien_group, False)
        check_round_status = pygame.sprite.spritecollide(self, self.player_bullet_group, False)

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        pause_game = pygame.sprite.Group()
        self.start_new_round()


    def reset_game(self):
        """Reset the game"""
        pass

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        # TODO: assign pygame.image.load("player_ship.png") to self.image
        # TODO: assign self.image.get_rect() to self.rect
        # TODO: assign WINDOW_WIDTH //2 to self.rect.centerx
        # TODO: assign WINDOW_HEIGHT to self.rect.bottom

        # TODO: assign 5 to self.lives
        # TODO: assign 8 to self.velocity
        # TODO: assign bullet_group to self.bullet_group

        # TODO: assign pygame.mixer.Sound("player_fire.wav") to self.shoot_sound

    def update(self):
        """Update the player"""
        # TODO: assign pygame.key.get_pressed() to keys

        # Move the player within the bounds of the screen
        # TODO: if keys[pygame.K_LEFT] and self.rect.left > 0:
        # TODO: subtract self.velocity from self.rect.x
        # TODO: if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
        # TODO: add self.velocity to self.rect.x

    def fire(self):
        """Fire a bullet"""
        # Restrict the number of bullet on screen at a time
        # TODO: if len(self.bullet_group) <2:
        # TODO: call self.shoot_sound.play() with no arguments
        # TODO: call PlayerBullet() with self.rect.centerx, self.rect.top, and self.bullet_group as the arguments

    def reset(self):
        """Reset the players position"""
        # TODO: assign WINDOW_WIDTH // 2 to self.rect.centerx


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""

    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        self.image.pygame.image.load("images/alien.png")
        self.image.get_rect().center = (x, y)
        self.velocity = velocity
        self.bullet_group = bullet_group
        self.rect.topleft = x, y

        self.starting = x
        self.starting = y


        self.direction = 1
        self.velocity_change = 0
        self.bullet_group.add(self.bullet_group)

        self.shoot_sound.play("alien")



# Create bullet groups
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()
# Create a player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player(my_player_bullet_group)

# Create an alien group.  Will add Alien objects via the game's start new round method
my_alien_group = pygame.sprite.Group()
# Create a Game object
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
# TODO: call the my_game.start_new_round() function with no arguments.
my_game.start_new_round()

# The main game loop
running = True
while running:
    # TODO: not really a todo here just a note to WATCH YOUR INDENTING.
    # TODO: for event in pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check to see if the user wants to quit
        # TODO: if event.type == pygame.QUIT
        if event.type == pygame.QUIT:
            running = False
            # TODO: assign False to running
        # The player wants to fire
        # TODO: if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            # TODO: if event.key == pygame.K_SPACE:
            if event.key == pygame.K_SPACE:
                my_player.fire()
                # TODO: call my_player.fire() function with no arguments.

    # Fill the display
    # TODO: call display_surface.fill() function and pass in (0, 0, 0) for the argument.
    display_surface.fill((0, 0, 0))

    # Update and display all sprite groups
    # TODO: call my_player_group.update() with no arguments.
    my_player_group.update()
    # TODO: call my_player_group.draw() passing in display_surface as its argument
    my_player_group.draw(display_surface)
    # TODO: repeat the last 2 todo's with my_alien_group instead of my_player_group
    my_alien_group.update()
    my_alien_group.draw(display_surface)
    # TODO: repeat the last 2 todo's with my_player_bullet_group
    my_player_bullet_group.draw(display_surface)
    my_player_bullet_group.update()
    # TODO: repeat the last 2 todo's with my_alien_bullet_group
    my_alien_bullet_group.draw(display_surface)
    my_alien_bullet_group.update()
    # Update and draw Game object
    # TODO: call my_game.update() with no arguments
    my_game.update()
    # TODO: call my_game.draw() with no arguments
    my_game.draw()
    # Update the display and tick clock
    # TODO: call pygame.display.update() with no arguments
    pygame.display.update()

    # TODO: call clock.tick() with FPS as its only argument
    clock.tick(FPS)

# End the game
pygame.quit()