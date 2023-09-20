import json, os

BUILDINGS = [ "SPD", "CDMG", "ATK", "DEF", "HP", "WATER_ATK", "FIRE_ATK",
              "WIND_ATK", "LIGHT_ATK", "DARK_ATK", "TOWER_ATK", "TOWER_SPD",
              "MANA_SPD", "MANA", "ENERGY_SPD", "ENERGY" 
            ]


class Building:

    def __init__(self, name: str):
        self.name = name

        with open(os.path.dirname(__file__) + "/data.json") as json_file:
            self.building = json.load(json_file)["buildings"][name]
            self.level = self.building["current_level"]

    def get_spent_glory_points(self) -> int:
        upgrades = self.building["upgrade"]
        result = 0

        for level in upgrades:
            if int(level) > self.level:
                break
            result += upgrades[level]["cost"]
        
        return result
    
    def get_needed_glory_points(self) -> int:
        upgrades = self.building["upgrade"]
        last_level = int(list(upgrades.keys())[-1])
        result = 0

        for level in range(self.level + 1, last_level + 1):
            result += upgrades[str(level)]["cost"]
        
        return result
    
    def get_total_glory_points(self) -> int:
        upgrades = self.building["upgrade"]

        result = 0

        for level in upgrades:
            result += upgrades[level]["cost"]

        return result
    
    def __str__(self) -> str:
        needed_glory_points = self.get_needed_glory_points()
        result = f"Building name : {self.name}\nCurrent Level : {self.level}\nNeeded glory points to max : {needed_glory_points}"
        return f"------------\n{result}\n------------\n"

def get_total_glory_points() -> int:
    result = 0

    for building_name in BUILDINGS:
        building = Building(building_name)

        result += building.get_total_glory_points()

    return result


def get_total_needed_glory_points() -> int:
    result = 0

    for building_name in BUILDINGS:
        building = Building(building_name)

        result += building.get_needed_glory_points()

    return result


def get_total_spent_glory_points() -> int:
    result = 0

    for building_name in BUILDINGS:
        building = Building(building_name)

        result += building.get_spent_glory_points()

    return result


def convert_cristals_to_glory(cristals: int, has_bonus: bool = False) -> int:
    multiplier = 4/3 if has_bonus else 1
    return convert(cristals, multiplier)


def convert_glory_to_cristals(glory: int, has_bonus: bool = False) -> int:
    multiplier = 0.75 if has_bonus else 1
    return convert(glory, multiplier)


def convert_glory_to_arena(glory: int, has_bonus: bool = False) -> int:
    multiplier = 1/4 if has_bonus else 1/3
    return convert(glory, multiplier)


def convert_cristals_to_arena(cristals: int) -> int:
    return int(cristals * (1/3))


def convert_arena_to_cristals(cristals: int) -> int:
    return convert(cristals, 3)


def convert_arena_to_glory(glory: int, has_bonus: bool = False) -> int:
    multiplier = 4 if has_bonus else 3
    return convert(glory, multiplier)


def convert(resource: int, multiplier: int) -> int:
    return int(resource * multiplier)


if __name__ == "__main__":
    total_needed_glory_points = get_total_needed_glory_points()
    total_spent_glory_points = get_total_spent_glory_points()

    print(f"Total glory points needed : {total_needed_glory_points}")
    print(f"Total glory points spent : {total_spent_glory_points}")

    [print(Building(building_name)) for building_name in BUILDINGS]

    cristals = 300
    print(f"{cristals} cristals = {convert_cristals_to_glory(cristals, True)}")

    glory = 8100
    print(f"{glory} Glory points = {convert_glory_to_cristals(glory)}")

