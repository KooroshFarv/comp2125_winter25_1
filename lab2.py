import random


#  weapon array
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear bomb']




for weapon in weapons:
    print(weapon)

# rolling dice and putting it in weaponRoll
try:
    userInput = input('Enter a number between 1 - 6 ')
    weaponRoll = int(userInput)

    if(weaponRoll < 1 or weaponRoll > 6):
        raise ValueError

except ValueError:
    print('Input is Invalid. Try again')
    exit(1)

#  weaponRoll adding to heroCombat
heroCombatStrength = 100
heroCombatStrength += weaponRoll

#  weaponRoll as index
mainWeapon = weapons[weaponRoll -1 ]

print(f'Hero picked number {weaponRoll}, which is {mainWeapon}.')


# conditions 
if (weaponRoll <= 2):
    print('You rolled a weak weapon, friend')
elif (weaponRoll <= 4):
    print('Your weapon is meh')
else : 
    print('Nice weapon, Frined')
if(mainWeapon != 'Fist') :
    print('Thank goodness you didnt roll the fist')

