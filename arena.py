from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = Team('Team One')
        self.team_two = Team('Team Two')
        # will hold our teams.

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input(
            "What is the max damage of the ability?  ")

        return Ability(name, max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        name = input("What is the weapon name?  ")
        max_damage = input(
            "What is the max damage of the weapon?  ")

        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        #  Prompt the user for the necessary information to create a new armor object.
        #  return the new armor object with values set by user.
        name = input("What is the armor name?  ")
        max_block = input(
            "What is the max block of the armor?  ")

        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               hero.add_ability(self.create_ability())
               #HINT: First create the ability, then add it to the hero
           elif add_item == "2":
               hero.add_weapon(self.create_weapon())
               #HINT: First create the weapon, then add it to the hero
           elif add_item == "3":
               hero.add_armor(self.create_armor())
               #HINT: First create the armor, then add it to the hero
        return hero

    # build_team_one is provided to you
    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    # Now implement build_team_two
    #HINT: If you get stuck, look at how build_team_one is implemented
    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
        # Call the attack method that exists in your team objects
        # for that battle functionality.

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        print(self.team_one.name + " average K/D was: " + self.team_one.kd_stat())

        print(self.team_two.name + " average K/D was: " + self.team_two.kd_stat())


        # Here is a way to list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()