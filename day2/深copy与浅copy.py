import copy


def shallow_copy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.copy(c)
    print(id(c), id(d))
    a[0] = 10
    print(c)
    print(d)


def deep_copy():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c), id(d))
    a[0] = 10
    print(c)
    print(d)


class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.equipments = ['鞋子']


if __name__ == '__main__':

    #shallow_copy()
    # deep_copy()
    old_hero=Hero('骑士',100)
    new_hero=copy.deepcopy(old_hero)
    new_hero.hp=90
    new_hero.equipments.append('盔甲')
    print(old_hero.hp, old_hero.equipments)
    print(new_hero.hp, new_hero.equipments)

