from random import randint
from time import sleep

class Hero():
    def __init__ (self,name,health,armor,power,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Great the hero ->',self.name)
        print('Health level:',self.health)
        print('Armor class',self.armor)
        print('Impact force:',self.power)
        print('Weapon:',self.weapon, "\n")

    def Strike(self,enemies):
        print('->STRIKE!')
        print(self,"attacks",enemies.name ,'using',self.weapon,'\n')
        if enemy.armor < 0 :
            enemy.health += enemy.armor
            enemy.armor = 0
        print(enemy.name,'swayed.')
        print('Armor class dropped to',enemy.armor)
        print('Health level decreased to',enemy.health,'\n')


    def check_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Warrior(Hero):
    def hello(self):
        print('-> NEW HERO! A skilled warrior appears from the forest depths', self.name)


    def attack(self,enemy):
        print(self.name, 'attacks fearlessly', enemy.name)
        print('The fight outcome for', self.name)
        self.print_info()
        print("The fight outcome for", enemy.name)
        enemy.print_info()


   
        

Knight = Warrior('Sriwijaya',100,50,70,"Pedang")
print('Hail to thee, good knight', Knight.name)
print('You are standing at the entrance to the forest full of deadly dangers. Are you ready to go there and fight the enemies (yes/no)?')
answer = input()
if answer == 'yes':
    play = True
else:
    play = False

enemies = list()
enemies.append(Warrior('Arjuno', 15,15,10,'Panah'))
enemies.append(Warrior('Brahmana', 10,15,5,'Keris'))
enemies.append(Warrior('Hayam Wuruk', 10,15,5,'Pedang'))
enemies.append(Warrior('Ken Arok', 10,15,5,'Belati'))


while play:
    enemy = enemies[randint(0,len(enemies)-1)]
    enemy.hello()
    enemy.print_info

is_attack = input('Join the fight (yes/no)?')
if is_attack == 'yes':
    if randint(0,1) == 1:
        fighters = [Knight,enemies]

    else:
        fighters = [enemies,Knight]

    fighters [0].Strike(fighters[1])
    fighters [0].attack(fighters[1])
print('---')

if enemy.check_alive() ==  False:
    print(enemy.name ,'died by sword of', Knight.name , 'died in battle with enemies')
    enemies.remove(enemy)


if Knight.check_alive()== False:
    print('The brave knight', Knight.name ,'died in battle with enemies')
    play = False

if len(enemies) == 0:
    print('The brave knight', Knight.name,'defeated all the enemies!')




    play = False
print('That is the end of the fairy tale')
