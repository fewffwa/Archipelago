from worlds.generic.Rules import set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState

def _ucn_has_ability( ability: str, player: int):
    return CollectionState.has(ability, player)

def _ucn_has_animatronic( animatronic: str, player: int):
    return CollectionState.has(animatronic, player)

def _ucn_can_beat_animatronic (animatronic: str, requiredability: str, player: int):
    if _ucn_has_animatronic(animatronic, player) and _ucn_has_ability(requiredability, player):
        return True
    elif _ucn_has_animatronic(animatronic, player) and requiredability == None:
        return True
    else:
        return False

def _ucn_calculate_max_possible_score(player: int):
    maxscore = 0
    if _ucn_can_beat_animatronic("Freddy Fazbear", "Left Door", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Bonnie", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Chica", "Global Music Box", player) or _ucn_can_beat_animatronic("Chica", "Change Music", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Foxy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Toy Freddy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Toy Bonnie", "Mask", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Toy Chica", "Mask", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Mangle", "Snare", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("BB", "Side Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("JJ", "Side Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Withered Chica", "Snare", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Withered Bonnie", "Mask", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Marionette", "MusicBox", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Golden Freddy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Springtrap", "Forward Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Phantom Mangle", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Phantom Freddy", "Flashlight", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Phantom BB", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare Freddy", "Flashlight", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare Bonnie", "Bonnie Plush", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare Fredbear", "Left Door", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare", "Right Door", player):
        maxscore = maxscore + 200
    if (_ucn_can_beat_animatronic("Jack-O-Chica", "AC", player)) or (_ucn_can_beat_animatronic("Jack-O-Chica", "Right Door", player) and _ucn_can_beat_animatronic("Jack-O-Chica", "Left Door", player)):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare Mangle", "Nightmare Mangle Plush", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmarionne", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nightmare BB", "Flashlight", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Old Man Consequences", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Circus Baby", "Baby Plush", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Ballora", "Right Door", player) and _ucn_can_beat_animatronic("Ballora", "Left Door", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Funtime Foxy", None, player) and _ucn_can_beat_animatronic("Ballora", "Left Door", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Ennard", "Forward Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Trash and the Gang", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Helpy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Happy Frog", "Audio Lure", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Mr. Hippo", "Audio Lure", player) or _ucn_can_beat_animatronic("Mr. Hippo", "Heater", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Nedd Bear", "Audio Lure", player) or _ucn_can_beat_animatronic("Nedd Bear", "Heater", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Pigpatch", "Audio Lure", player) or _ucn_can_beat_animatronic("Pigpatch", "Heater", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Orville Elephant", "Heater", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Rockstar Foxy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Rockstar Freddy", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Rockstar Bonnie", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Rockstar Chica", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Music Man", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("El Chip", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Funtime Chica", None, player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Molten Freddy", "Forward Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Scrap Baby", "Shock", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Afton", "Side Vent", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Lefty", "Global Music Box", player):
        maxscore = maxscore + 200
    if _ucn_can_beat_animatronic("Phone Guy", None, player):
        maxscore = maxscore + 200
    return maxscore

    # Sets rules on entrances and advancements that are always applied
def set_rules(multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_location("100 points"), _ucn_calculate_max_possible_score(player) >= 100)
    set_rule(multiworld.get_location("200 points"), _ucn_calculate_max_possible_score(player) >= 200)
    set_rule(multiworld.get_location("300 points"), _ucn_calculate_max_possible_score(player) >= 300)
    set_rule(multiworld.get_location("400 points"), _ucn_calculate_max_possible_score(player) >= 400)
    set_rule(multiworld.get_location("500 points"), _ucn_calculate_max_possible_score(player) >= 500)
    set_rule(multiworld.get_location("600 points"), _ucn_calculate_max_possible_score(player) >= 600)
    set_rule(multiworld.get_location("700 points"), _ucn_calculate_max_possible_score(player) >= 700)
    set_rule(multiworld.get_location("800 points"), _ucn_calculate_max_possible_score(player) >= 800)
    set_rule(multiworld.get_location("900 points"), _ucn_calculate_max_possible_score(player) >= 900)
    set_rule(multiworld.get_location("1000 points"), _ucn_calculate_max_possible_score(player) >= 1000)
    set_rule(multiworld.get_location("1100 points"), _ucn_calculate_max_possible_score(player) >= 1100)
    set_rule(multiworld.get_location("1200 points"), _ucn_calculate_max_possible_score(player) >= 1200)
    set_rule(multiworld.get_location("1300 points"), _ucn_calculate_max_possible_score(player) >= 1300)
    set_rule(multiworld.get_location("1400 points"), _ucn_calculate_max_possible_score(player) >= 1400)
    set_rule(multiworld.get_location("1500 points"), _ucn_calculate_max_possible_score(player) >= 1500)
    set_rule(multiworld.get_location("1600 points"), _ucn_calculate_max_possible_score(player) >= 1600)
    set_rule(multiworld.get_location("1700 points"), _ucn_calculate_max_possible_score(player) >= 1700)
    set_rule(multiworld.get_location("1800 points"), _ucn_calculate_max_possible_score(player) >= 1800)
    set_rule(multiworld.get_location("1900 points"), _ucn_calculate_max_possible_score(player) >= 1900)
    set_rule(multiworld.get_location("2000 points"), _ucn_calculate_max_possible_score(player) >= 2000)
    set_rule(multiworld.get_location("2100 points"), _ucn_calculate_max_possible_score(player) >= 2100)
    set_rule(multiworld.get_location("2200 points"), _ucn_calculate_max_possible_score(player) >= 2200)
    set_rule(multiworld.get_location("2300 points"), _ucn_calculate_max_possible_score(player) >= 2300)
    set_rule(multiworld.get_location("2400 points"), _ucn_calculate_max_possible_score(player) >= 2400)
    set_rule(multiworld.get_location("2500 points"), _ucn_calculate_max_possible_score(player) >= 2500)
    set_rule(multiworld.get_location("2600 points"), _ucn_calculate_max_possible_score(player) >= 2600)
    set_rule(multiworld.get_location("2700 points"), _ucn_calculate_max_possible_score(player) >= 2700)
    set_rule(multiworld.get_location("2800 points"), _ucn_calculate_max_possible_score(player) >= 2800)
    set_rule(multiworld.get_location("2900 points"), _ucn_calculate_max_possible_score(player) >= 2900)
    set_rule(multiworld.get_location("3000 points"), _ucn_calculate_max_possible_score(player) >= 3000)
    set_rule(multiworld.get_location("3100 points"), _ucn_calculate_max_possible_score(player) >= 3100)
    set_rule(multiworld.get_location("3200 points"), _ucn_calculate_max_possible_score(player) >= 3200)
    set_rule(multiworld.get_location("3300 points"), _ucn_calculate_max_possible_score(player) >= 3300)
    set_rule(multiworld.get_location("3400 points"), _ucn_calculate_max_possible_score(player) >= 3400)
    set_rule(multiworld.get_location("3500 points"), _ucn_calculate_max_possible_score(player) >= 3500)
    set_rule(multiworld.get_location("3600 points"), _ucn_calculate_max_possible_score(player) >= 3600)
    set_rule(multiworld.get_location("3700 points"), _ucn_calculate_max_possible_score(player) >= 3700)
    set_rule(multiworld.get_location("3800 points"), _ucn_calculate_max_possible_score(player) >= 3800)
    set_rule(multiworld.get_location("3900 points"), _ucn_calculate_max_possible_score(player) >= 3900)
    set_rule(multiworld.get_location("4000 points"), _ucn_calculate_max_possible_score(player) >= 4000)
    set_rule(multiworld.get_location("4100 points"), _ucn_calculate_max_possible_score(player) >= 4100)
    set_rule(multiworld.get_location("4200 points"), _ucn_calculate_max_possible_score(player) >= 4200)
    set_rule(multiworld.get_location("4300 points"), _ucn_calculate_max_possible_score(player) >= 4300)
    set_rule(multiworld.get_location("4400 points"), _ucn_calculate_max_possible_score(player) >= 4400)
    set_rule(multiworld.get_location("4500 points"), _ucn_calculate_max_possible_score(player) >= 4500)
    set_rule(multiworld.get_location("4600 points"), _ucn_calculate_max_possible_score(player) >= 4600)
    set_rule(multiworld.get_location("4700 points"), _ucn_calculate_max_possible_score(player) >= 4700)
    set_rule(multiworld.get_location("4800 points"), _ucn_calculate_max_possible_score(player) >= 4800)
    set_rule(multiworld.get_location("4000 points"), _ucn_calculate_max_possible_score(player) >= 4900)
    set_rule(multiworld.get_location("5000 points"), _ucn_calculate_max_possible_score(player) >= 5000)
    set_rule(multiworld.get_location("5100 points"), _ucn_calculate_max_possible_score(player) >= 5100)
    set_rule(multiworld.get_location("5200 points"), _ucn_calculate_max_possible_score(player) >= 5200)
    set_rule(multiworld.get_location("5300 points"), _ucn_calculate_max_possible_score(player) >= 5300)
    set_rule(multiworld.get_location("5400 points"), _ucn_calculate_max_possible_score(player) >= 5400)
    set_rule(multiworld.get_location("5500 points"), _ucn_calculate_max_possible_score(player) >= 5500)
    set_rule(multiworld.get_location("5600 points"), _ucn_calculate_max_possible_score(player) >= 5600)
    set_rule(multiworld.get_location("5700 points"), _ucn_calculate_max_possible_score(player) >= 5700)
    set_rule(multiworld.get_location("5800 points"), _ucn_calculate_max_possible_score(player) >= 5800)
    set_rule(multiworld.get_location("5900 points"), _ucn_calculate_max_possible_score(player) >= 5900)
    set_rule(multiworld.get_location("6000 points"), _ucn_calculate_max_possible_score(player) >= 6000)
    set_rule(multiworld.get_location("6100 points"), _ucn_calculate_max_possible_score(player) >= 6100)
    set_rule(multiworld.get_location("6200 points"), _ucn_calculate_max_possible_score(player) >= 6200)
    set_rule(multiworld.get_location("6300 points"), _ucn_calculate_max_possible_score(player) >= 6300)
    set_rule(multiworld.get_location("6400 points"), _ucn_calculate_max_possible_score(player) >= 6400)
    set_rule(multiworld.get_location("6500 points"), _ucn_calculate_max_possible_score(player) >= 6500)
    set_rule(multiworld.get_location("6600 points"), _ucn_calculate_max_possible_score(player) >= 6600)
    set_rule(multiworld.get_location("6700 points"), _ucn_calculate_max_possible_score(player) >= 6700)
    set_rule(multiworld.get_location("6800 points"), _ucn_calculate_max_possible_score(player) >= 6800)
    set_rule(multiworld.get_location("6900 points"), _ucn_calculate_max_possible_score(player) >= 6900)
    set_rule(multiworld.get_location("7000 points"), _ucn_calculate_max_possible_score(player) >= 7000)
    set_rule(multiworld.get_location("7100 points"), _ucn_calculate_max_possible_score(player) >= 7100)
    set_rule(multiworld.get_location("7200 points"), _ucn_calculate_max_possible_score(player) >= 7200)
    set_rule(multiworld.get_location("7300 points"), _ucn_calculate_max_possible_score(player) >= 7300)
    set_rule(multiworld.get_location("7400 points"), _ucn_calculate_max_possible_score(player) >= 7400)
    set_rule(multiworld.get_location("7500 points"), _ucn_calculate_max_possible_score(player) >= 7500)
    set_rule(multiworld.get_location("7600 points"), _ucn_calculate_max_possible_score(player) >= 7600)
    set_rule(multiworld.get_location("7700 points"), _ucn_calculate_max_possible_score(player) >= 7700)
    set_rule(multiworld.get_location("7800 points"), _ucn_calculate_max_possible_score(player) >= 7800)
    set_rule(multiworld.get_location("7900 points"), _ucn_calculate_max_possible_score(player) >= 7900)
    set_rule(multiworld.get_location("8000 points"), _ucn_calculate_max_possible_score(player) >= 8000)
    set_rule(multiworld.get_location("8100 points"), _ucn_calculate_max_possible_score(player) >= 8100)
    set_rule(multiworld.get_location("8200 points"), _ucn_calculate_max_possible_score(player) >= 8200)
    set_rule(multiworld.get_location("8300 points"), _ucn_calculate_max_possible_score(player) >= 8300)
    set_rule(multiworld.get_location("8400 points"), _ucn_calculate_max_possible_score(player) >= 8400)
    set_rule(multiworld.get_location("8500 points"), _ucn_calculate_max_possible_score(player) >= 8500)
    set_rule(multiworld.get_location("8600 points"), _ucn_calculate_max_possible_score(player) >= 8600)
    set_rule(multiworld.get_location("8700 points"), _ucn_calculate_max_possible_score(player) >= 8700)
    set_rule(multiworld.get_location("8800 points"), _ucn_calculate_max_possible_score(player) >= 8800)
    set_rule(multiworld.get_location("8900 points"), _ucn_calculate_max_possible_score(player) >= 8900)
    set_rule(multiworld.get_location("9000 points"), _ucn_calculate_max_possible_score(player) >= 9000)
    set_rule(multiworld.get_location("9100 points"), _ucn_calculate_max_possible_score(player) >= 9100)
    set_rule(multiworld.get_location("9200 points"), _ucn_calculate_max_possible_score(player) >= 9200)
    set_rule(multiworld.get_location("9300 points"), _ucn_calculate_max_possible_score(player) >= 9300)
    set_rule(multiworld.get_location("9400 points"), _ucn_calculate_max_possible_score(player) >= 9400)
    set_rule(multiworld.get_location("9500 points"), _ucn_calculate_max_possible_score(player) >= 9500)
    set_rule(multiworld.get_location("9600 points"), _ucn_calculate_max_possible_score(player) >= 9600)
    set_rule(multiworld.get_location("9700 points"), _ucn_calculate_max_possible_score(player) >= 9700)
    set_rule(multiworld.get_location("9800 points"), _ucn_calculate_max_possible_score(player) >= 9800)
    set_rule(multiworld.get_location("9900 points"), _ucn_calculate_max_possible_score(player) >= 9900)
    set_rule(multiworld.get_location("10000 points"), _ucn_calculate_max_possible_score(player) >= 10000)






# Sets rules on completion condition
def set_completion_rules(multiworld: MultiWorld, player: int):
    completion_requirements = _ucn_calculate_max_possible_score(player) >= getattr(multiworld, "score_required")[player]
    multiworld.completion_condition[player] = lambda state: completion_requirements(state)
