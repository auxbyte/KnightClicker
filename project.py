class Character():
    def __init__(self, name, health, attack, gold):
        self.name = name
        self.health = health
        self.attack = attack
        self.gold = gold
        
    def Damage(offense, defense):
        defense_default = char[defense].health
        char[defense].health = char[defense].health - char[offense].attack
        print("%s attacked %s for %d damage. %s's health is %d"% (char[offense].name, char[defense].name, char[offense].attack, char[defense].name, char[defense].health))
        if char[defense].health < 1:
            print("%s has killed %s"% (char[offense].name, char[defense].name))
            if char[offense].name == "Player":
                char[defense].health = defense_default
                char[0].gold = char[0].gold + char[defense].gold
                print("%d gold gained"% (char[0].gold))
            else:
                print("Game Over")
class Shop():
    def __init__(self, name, cost, hpboost, atkboost, goldboost):
        self.name = name
        self.cost = cost
        self.hpboost = hpboost
        self.atkboost = atkboost
        self.goldboost = goldboost

    def Buy(itemid):
        if char[0].gold >= items[itemid].cost:
            char[0].gold = char[0].gold - items[itemid].cost
            if items[itemid].atkboost > 0:
                char[0].attack = char[0].attack + items[itemid].atkboost
                print("You bought a %s for %d. New Attack Total: %d"% (items[itemid].name, items[itemid].cost, char[0].attack))
        else:
            print("Too Expensive")

char = []
char.append(Character("Player", 10, 1, 0))
char.append(Character("low", 10, 1, 5))
char.append(Character("mid", 15, 2, 10))
char.append(Character("high", 25, 5, 50))
char.append(Character("boss", 50, 10, 1000))

items = []
#Shop(NAME, COST, HPBOOST, ATKBOOST, GOLDBOOST%)
items.append(Shop("Wood Sword", 10, 0, 5, 0))
items.append(Shop("Iron Sword", 20, 0, 10, 0))
items.append(Shop("Master Sword", 50, 0, 20, 0))

#====CHARACTER IDS====
#player = 0
#lowlevel = 1
#midlevel = 2
#highlevel = 3
#boss = 4
