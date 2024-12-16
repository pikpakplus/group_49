from random import randint, choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.name} health: {self.health} damage: {self.damage}"


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability if hasattr(hero, 'ability') else None

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health -= self.damage
        print(f"Boss {self.name} attacked all heroes.")

    def __str__(self):
        return super().__str__() + f" defence: {self.__defence}"


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        if self.health > 0:
            boss.health -= self.damage


# Герои с уникальными способностями
class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'REVIVE')
        self.used_revive = False

    def apply_super_power(self, boss, heroes):
        if not self.used_revive:
            for hero in heroes:
                if hero.health <= 0:
                    hero.health = 100
                    self.health = 0
                    self.used_revive = True
                    print(f'Witcher {self.name} revived {hero.name} and sacrificed himself.')
                    break


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'BOOST')
        self.rounds_left = 4

    def apply_super_power(self, boss, heroes):
        if self.rounds_left > 0:
            for hero in heroes:
                hero.damage += 5
            print(f'Magic {self.name} boosted all heroes\' attack!')
            self.rounds_left -= 1


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STEAL')

    def apply_super_power(self, boss, heroes):
        stolen_health = 30
        boss.health -= stolen_health
        target = choice(heroes)
        target.health += stolen_health
        print(f'Hacker {self.name} stole {stolen_health} health from Boss and gave it to {target.name}.')


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'PROTECT')

    def apply_super_power(self, boss, heroes):
        portion = boss.damage // 5
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += portion
                self.health -= portion
        print(f'Golem {self.name} absorbed part of Boss damage.')


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'INVISIBLE')
        self.invisible_rounds = 2

    def apply_super_power(self, boss, heroes):
        if self.invisible_rounds > 0:
            print(f'{self.name} avoided damage this round.')
            self.invisible_rounds -= 1


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'STUN')

    def apply_super_power(self, boss, heroes):
        if randint(1, 2) == 1:
            boss.damage = 0
            print(f'Thor {self.name} stunned the Boss! Boss deals no damage this round.')


class Gambler(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'ROLL_DICE')

    def apply_super_power(self, boss, heroes):
        die1 = randint(1, 6)
        die2 = randint(1, 6)
        if die1 == die2:
            boss.health -= die1 * die2
            print(f'Gambler {self.name} rolled doubles! Boss takes {die1 * die2} damage.')
        else:
            teammate = choice(heroes)
            teammate.health -= die1 + die2
            print(f'Gambler {self.name} failed! {teammate.name} loses {die1 + die2} health.')


class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, 'SUMMON_SAITAMA')

    def apply_super_power(self, boss, heroes):
        if randint(1, 10) == 1:
            boss.health = 0
            print(f'King {self.name} summoned Saitama! Boss defeated instantly.')


# Игровые функции
def is_game_over(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!")
        return True
    if all(hero.health <= 0 for hero in heroes):
        print("Boss won!")
        return True
    return False


def play_round(boss, heroes):
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            hero.attack(boss)
            if hasattr(hero, 'apply_super_power'):
                hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f"--- Boss ---\n{boss}")
    print(f"--- Heroes ---")
    for hero in heroes:
        print(hero)
    print("\n")


def start_game():
    boss = Boss("Lord", 1000, 50)
    heroes = [
        Witcher("Geralt", 150, 0),
        Magic("Subaru", 200, 10),
        Hacker("Neo", 180, 10),
        Golem("Rocky", 400, 5),
        Avrora("Shade", 200, 10),
        Thor("Thunder", 300, 20),
        Gambler("Dice", 200, 10),
        King("King", 150, 0)
    ]

    show_statistics(boss, heroes)
    while not is_game_over(boss, heroes):
        play_round(boss, heroes)


start_game()
