from time import sleep as s
a=str(input())
if a =='e':
    pass
else:
    print('bye')
    s(4)
    exit()
from random import randint as r
class enemy:
    name = 'cow'
    hp = 5
    onset = 1
    def __init__(self, name, hp, onset):
        self.name = name
        self.hp = hp
        self.onset = onset
en = []
bull = enemy('bull', 40, r(2, 3))
en.append('bull')
spider = enemy('spider', 30, r(1, 3))
en.append('spider')
gargoyle = enemy('gargoyle', 60, r(2, 5))
en.append('gargoyle')
goblin = enemy('goblin', 55, r(2, 5))
en.append('goblin')
goblin_dog = enemy('goblin dog', 35, r(1, 2))
en.append('goblin_dog')
skeleton = enemy('skeleton', 55, r(3, 5))
en.append('skeleton')
uhp=100
med=0
for x in range(8):
    z=r(0, 5)
    c=en[z]
    print('uhp', uhp, 'medkit', med)
    if c =='bull':
        print(bull.name)
        ehp=bull.hp
        eon=bull.onset
    if c =='spider':
        print(spider.name)
        ehp = spider.hp
        eon = spider.onset
    if c =='gargoyle':
        print(gargoyle.name)
        ehp = gargoyle.hp
        eon = gargoyle.onset
    if c =='goblin':
        print(goblin.name)
        ehp = goblin.hp
        eon = goblin.onset
    if c =='goblin_dog':
        print(goblin_dog.name)
        ehp = goblin_dog.hp
        eon = goblin_dog.onset
    if c =='skeleton':
        print(skeleton.name)
        ehp = skeleton.hp
        eon = skeleton.onset
    print('enemy hp', ehp)
    uonset=r(5, 6)
    while ehp>0:
        if uhp<0:
            print('you died')
            s(1)
            exit()
        else:
            aa = str(input())
            if aa=='a':
                ehp-=uonset
                uhp-=eon
            if aa=='m':
                med-=1
                uhp+=r(20, 30)
            print('uhp', uhp, 'medkit', med, 'enemy hp', ehp)
    m=r(1, 4)
    if m==1:
        med+=1
        print('+оптечка')
    else:
        pass

print('dange clear')



















