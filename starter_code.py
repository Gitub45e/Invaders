import pygame, random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define Classes
class Game():
    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):
     pass

    def update(self):
     pass

    def draw(self):
     pass

    def shift_aliens(self):
        """Shift the aliens"""
        pass

    def check_collisions(self):
        """Check if the aliens collide with the player"""
        pass

    def check_round_completion(self):
        """Check if the round is complete"""
        pass


    def start_new_round(self):
        """Start a new round"""
        pass

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
        pass


    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass


class Player(pygame.sprite.Sprite):
    """A class to model a spaceship the user can control"""

    def __init__(self, bullet_group):
        """Initialize the player"""
        super().__init__()
        pass

    def update(self):
        """Update the player"""
        pass

    def fire(self):
        """Fire a bullet"""
        pass

    def reset(self):
        """Reset the players position"""
        pass


class Alien(pygame.sprite.Sprite):
    """A class to model an enemy alien"""
    
    def __init__(self, x, y, velocity, bullet_group):
        """Initialize the alien"""
        super().__init__()
        pass

    def update(self):
        """Update the alien"""
        pass

    def fire(self):
        """Fire a bullet"""
        pass

    def reset(self):
        """Reset the alien position"""
        pass


class PlayerBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the player"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        pass

    def update(self):
        """Update the bullet"""
        pass


class AlienBullet(pygame.sprite.Sprite):
    """A class to model a bullet fired by the alien"""

    def __init__(self, x, y, bullet_group):
        """Initialize the bullet"""
        super().__init__()
        pass

    def update(self):
        """Update the bullet"""
        pass


#Create bullet groups
# TODO: assign pygame.sprite.Group() to my_player_bullet_group
# TODO: assign pygame.sprite.Group() to my_alien_bullet_group
my_player_bullet_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()
#Create a player group and Player object
# TODO: assign pygame.sprite.Group() to my_player_group
my_player_group = pygame.sprite.Group()
# TODO: assign Player(my_player_bullet_group) to my_player
my_player = Player(my_player_bullet_group)
# TODO: call the my_player_group.add() function and pass in my_player as the argument.

#Create an alien group.  Will add Alien objects via the game's start new round method
# TODO: assign pygame.sprite.Group() to my_alien_group
my_alien_group = pygame.sprite.Group()
#Create a Game object
# TODO: assign Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group) to my_game
my_game = Game(my_player, my_alien_group, my_player_bullet_group, my_alien_bullet_group)
# TODO: call the my_game.start_new_round() function with no arguments.

#The main game loop
# TODO: assign True to running
running = True
# TODO: while running:
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
        #The player wants to fire
        # TODO: if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:
            # TODO: if event.key == pygame.K_SPACE:
         if event.key == pygame.K_SPACE:
            my_player.fire()
                # TODO: call my_player.fire() function with no arguments.


    #Fill the display
    # TODO: call display_surface.fill() function and pass in (0, 0, 0) for the argument.

    #Update and display all sprite groups
    # TODO: call my_player_group.update() with no arguments.
    # TODO: call my_player_group.draw() passing in display_surface as its argument

    # TODO: repeat the last 2 todo's with my_alien_group instead of my_player_group

    # TODO: repeat the last 2 todo's with my_player_bullet_group

    # TODO: repeat the last 2 todo's with my_alien_bullet_group

    #Update and draw Game object
    # TODO: call my_game.update() with no arguments
    # TODO: call my_game.draw() with no arguments

    #Update the display and tick clock
    # TODO: call pygame.display.update() with no arguments
    # TODO: call clock.tick() with FPS as its only argument

#End the game
pygame.quit()