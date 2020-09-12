import random

from armor import Armor

class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String starting_health: Integer current_health: Integer'''
        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization

        self.abilities = list()
        self.armors = list()

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

        self.deaths = 0
        self.kills = 0

    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        if (len(self.abilities) <= 0 and len(opponent.abilities) <= 0):
            print('Seeing no fighter has any abilities, it is a draw between {0} and {1}'.format(self.name, opponent.name))
            return
        elif (len(self.abilities) <= 0 or len(opponent.abilities) <= 0):
            print('Seeing that {0} is the only one with any abilities they win!'.format(self.name if len(self.abilities) > 0 else opponent.name))
            if len(self.abilities) > 0:
                self.add_kill()
                opponent.add_death()
            else:
                opponent.add_kill()
                self.add_death()
            return

        while self.is_alive() and opponent.is_alive():
            print('{0} takes damage as {1} attacks'.format(opponent.name, self.name))
            opponent.take_damage(self.attack())
            if(not opponent.is_alive()):
                break
            print('{0} takes damage as {1} attacks'.format(self.name, opponent.name))
            self.take_damage(opponent.attack())

        print('{0} is the winner!'.format(self.name if self.is_alive() else opponent.name))
        if self.is_alive():
            self.add_kill()
            opponent.add_death()
        else:
            opponent.add_kill()
            self.add_death()


    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        self.armors.append(armor)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''

        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def attack(self):
        '''Calculate the total damage from all ability attacks.
            return: total_damage:Int
        '''

        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def defend(self, damage_amt):
        '''Calculate the total block amount from all armor blocks.
            return: total_block:Int
        '''
        b = 0
        for armor in self.armors:
            b = armor.block()
        return b

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        armor = self.defend(damage)
        self.current_health = self.current_health - (damage - armor) if damage - armor >= 0 else self.current_health
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        return (True if self.current_health > 0 else False)





if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())


