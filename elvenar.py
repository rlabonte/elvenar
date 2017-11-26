class Item:
    """Base Type for all in-game items"""
    def __init__(self, name, production_cost, quantity):
        self.d_name = name
        self.d_production_cost = production_cost
        self.d_quantity = quantity
    def cost(self):
        """Returns the production cost of this item"""
        total_cost = {}
        if self.d_production_cost:
            for prod in self.d_production_cost:
                cost = prod.cost()
                for item in cost:
                    if item in total_cost:
                        total_cost[item] += cost[item] / self.d_quantity
                    else:
                        total_cost[item] = cost[item]  / self.d_quantity
        else:
            total_cost[self.d_name] = 1

        return total_cost
    def print(self):
        """Print the cost of this Item"""
        cost = self.cost()
        print("To produce " + str(self.d_quantity) + " " + self.d_name +
              " it costs:")
        if len(cost) == 1:
            print("Nothing (Base type)")
        else:
            for item in cost:
                print(str(cost[item] * self.d_quantity) + " " + item + ", ", end="")
            print("")

class Production:
    """Represents one unit of production of an Item"""
    def __init__(self, item_type, quantity):
        self.d_type = ITEMS[item_type]
        self.d_quantity = quantity
    def cost(self):
        """The cost of producing this item"""
        total_cost = {}
        item_cost = self.d_type.cost()
        for item in item_cost:
            total_cost[item] = item_cost[item] * self.d_quantity
        return  total_cost

def get_base_items(item_, quantity):
    """Get all Items needed to produce x elements"""
    nb_prod = quantity
    prod = ITEMS[item_].cost()
    for items in prod:
        prod[items] *= nb_prod
    return prod


ITEMS = {}
SUPPLY = "Supply"
GOLD = "Gold"
ORCS = "Orcs"
ELIXIR = "Elixir"
GEMS = "Gems"
DUST = "Dust"
HARD_SHROOM = "HardShroom"
PSYCHO_SHROOM = "PsychoShroom"
POWER_SHROOM = "PowerShroom"
DUNG = "Dung"
WISDOM_SHROOM = "Shroom of wisdom"
ARMAMENT = "Armament"
DEBRIS = "Deris"
LOOT = "Loot"


"""Base Items"""
ITEMS[SUPPLY] = Item("Supply", [], 1)
ITEMS[GOLD] = Item("Gold", [], 1)
ITEMS[ORCS] = Item("Orcs", [], 1)

"""Goods"""
ITEMS[ELIXIR] = Item("Elixir", [], 1)
ITEMS[GEMS] = Item("Gems", [], 1)
ITEMS[DUST] = Item("Dust", [], 1)

"""Derived Items"""
ITEMS[HARD_SHROOM] = Item("HardShroom", [Production(GEMS, 91)], 560)
ITEMS[PSYCHO_SHROOM] = Item("PsychoShroom", [Production(DUST, 130)], 400)
ITEMS[POWER_SHROOM] = Item("PowerShroom", [Production(ELIXIR, 290)], 240)
ITEMS[DUNG] = Item("Dung", [Production(PSYCHO_SHROOM, 280),
                            Production(ORCS, 40)],
                   72)
ITEMS[WISDOM_SHROOM] = Item("Shroom of wisdom", [Production(DUNG, 100)], 80)
ITEMS[ARMAMENT] = Item("Armament", [Production(GOLD, 31000),
                                    Production(ORCS, 40),
                                    Production(SUPPLY, 2700)],
                       160)
ITEMS[DEBRIS] = Item("Deris", [Production(PSYCHO_SHROOM, 630),
                               Production(ORCS, 40)],
                     48)
ITEMS[LOOT] = Item("Loot", [Production(POWER_SHROOM, 370),
                            Production(ARMAMENT, 630),
                            Production(ORCS, 40)],
                   192)

"""I have"""
I_HAVE = {SUPPLY : 800000,
          GOLD : 9778000,
          ORCS : 296,
          ELIXIR : 130000,
          LOOT : 1974}
I_WANT = {LOOT : 6500}

PT = "I want "
for item in I_WANT:
    PT += str(I_WANT[item]) + " " + item + ", "
print(PT[:-2])

PT = "I have "
for item in I_HAVE:
    PT += str(I_HAVE[item]) + " " + item + ", "
print(PT[:-2])

I_NEED = {}
PT = "I Need "
for item in I_WANT:
    if not I_HAVE[item]:
        I_NEED[item] = I_WANT[item]
    elif I_HAVE[item] >= I_WANT[item]:
        continue
    else:
        I_NEED[item] = I_WANT[item] - I_HAVE[item]

PT = "I need "
for item in I_NEED:
    PT += str(I_NEED[item]) + " " + item + ", "
print(PT[:-2])

PT = "And to get this I will need "
NEEDED = {}
for item in I_NEED:
    cost = get_base_items(item, I_NEED[item])
    for i in cost:
        if i in NEEDED:
            NEEDED[i] += cost[i]
        else:
            NEEDED[i] = cost[i]

for i in NEEDED:
    PT += str("%1.0f" % NEEDED[i]) + " " + i + ", "
print(PT[:-2])


