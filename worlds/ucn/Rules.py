from worlds.generic.Rules import set_rule, add_rule, add_item_rule
from BaseClasses import MultiWorld, CollectionState

def _ucn_has_ability(state:CollectionState, ability: str, player: int):
    return state.has(ability, player)

def _ucn_has_animatronic( state:CollectionState, animatronic: str, player: int):
    return  state.has(animatronic, player)

def _ucn_can_beat_animatronic (state:CollectionState, animatronic: str, requiredability: str, player: int):
    if _ucn_has_animatronic(state, animatronic, player) and _ucn_has_ability(state, requiredability, player):
        
        return True
    elif _ucn_has_animatronic(state, animatronic, player) and requiredability == None:
        return True
        
    else:
        return False

def _ucn_calculate_max_possible_score(state:CollectionState, player: int):
    maxscore = 0
    if _ucn_can_beat_animatronic( state,"Freddy Fazbear", "Left Door", player):
        maxscore = maxscore + 200   
    if _ucn_can_beat_animatronic( state,"Bonnie", None, player):
        maxscore = maxscore + 200 
        
    if _ucn_can_beat_animatronic( state,"Chica", "Global Music Box", player) or _ucn_can_beat_animatronic(state, "Chica", "Change Music", player):
        maxscore = maxscore + 200 
        
    if _ucn_can_beat_animatronic( state,"Foxy", None, player):
        maxscore = maxscore + 200
        
    if _ucn_can_beat_animatronic( state,"Toy Freddy", None, player):
        maxscore = maxscore + 200
        
    if _ucn_can_beat_animatronic( state,"Toy Bonnie", "Mask", player):
        maxscore = maxscore + 200
        
    if _ucn_can_beat_animatronic( state,"Toy Chica", "Mask", player):
        maxscore = maxscore + 200
        
    if _ucn_can_beat_animatronic( state,"Mangle", "Snare", player):
        maxscore = maxscore + 200 
 
    if _ucn_can_beat_animatronic( state,"BB", "Side Vent", player):
        maxscore = maxscore + 200 
 
    if _ucn_can_beat_animatronic( state,"JJ", "Side Vent", player):
        maxscore = maxscore + 200 
   
    if _ucn_can_beat_animatronic( state,"Withered Chica", "Snare", player):
        maxscore = maxscore + 200
   
    if _ucn_can_beat_animatronic( state,"Withered Bonnie", "Mask", player):
        maxscore = maxscore + 200 
      
    if _ucn_can_beat_animatronic( state,"Marionette", "Music Box", player):
        maxscore = maxscore + 200 
       
    if _ucn_can_beat_animatronic( state,"Golden Freddy", None, player):
        maxscore = maxscore + 200
       
    if _ucn_can_beat_animatronic( state,"Springtrap", "Forward Vent", player):
        maxscore = maxscore + 200 
       
    if _ucn_can_beat_animatronic( state,"Phantom Mangle", None, player):
        maxscore = maxscore + 200
    
    if _ucn_can_beat_animatronic( state,"Phantom Freddy", "Flashlight", player):
        maxscore = maxscore + 200 
           
    if _ucn_can_beat_animatronic( state,"Phantom BB", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nightmare Freddy", "Flashlight", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nightmare Bonnie", "Bonnie Plush", player):
        maxscore = maxscore + 200
   
    if _ucn_can_beat_animatronic( state,"Nightmare Fredbear", "Left Door", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nightmare", "Right Door", player):
        maxscore = maxscore + 200
    
    if (_ucn_can_beat_animatronic (state, "Jack-O-Chica", "AC", player)) or (_ucn_can_beat_animatronic(state, "Jack-O-Chica", "Right Door", player) and _ucn_can_beat_animatronic(state,"Jack-O-Chica", "Left Door", player)):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nightmare Mangle", "Nightmare Mangle Plush", player):
        maxscore = maxscore + 200
    
    if _ucn_can_beat_animatronic( state,"Nightmarionne", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nightmare BB", "Flashlight", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Old Man Consequences", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Circus Baby", "Circus Baby Plush", player):
        maxscore = maxscore + 200
    
    if _ucn_can_beat_animatronic( state,"Ballora", "Right Door", player) and _ucn_can_beat_animatronic(state,"Ballora", "Left Door", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Funtime Foxy", None, player) and _ucn_can_beat_animatronic(state,"Ballora", "Left Door", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Ennard", "Forward Vent", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Trash and the Gang", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Helpy", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Happy Frog", "Audio Lure", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Mr. Hippo", "Audio Lure", player) or _ucn_can_beat_animatronic(state,"Mr. Hippo", "Heater", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Nedd Bear", "Audio Lure", player) or _ucn_can_beat_animatronic(state,"Nedd Bear", "Heater", player):
        maxscore = maxscore + 200
    
    if _ucn_can_beat_animatronic( state,"Pigpatch", "Audio Lure", player) or _ucn_can_beat_animatronic(state,"Pigpatch", "Heater", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Orville Elephant", "Heater", player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Rockstar Foxy", None, player):
        maxscore = maxscore + 200 
    
    if _ucn_can_beat_animatronic( state,"Rockstar Freddy", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Rockstar Bonnie", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Rockstar Chica", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Music Man", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"El Chip", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Funtime Chica", None, player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Molten Freddy", "Forward Vent", player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Scrap Baby", "Shock", player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Afton", "Side Vent", player):
        maxscore = maxscore + 200 

    if _ucn_can_beat_animatronic( state,"Lefty", "Global Music Box", player):
        maxscore = maxscore + 200 
      
    if _ucn_can_beat_animatronic( state,"Phone Guy", None, player):
        maxscore = maxscore + 200
        
   
    return maxscore

    # Sets rules on entrances and advancements that are always applied
def set_gamerules(multiworld: MultiWorld, player: int):
    set_rule(multiworld.get_location("freebie", player), lambda state,: True)
    set_rule(multiworld.get_location("100pts", player), lambda state,: _ucn_calculate_max_possible_score(state, player) >= 100)
    set_rule(multiworld.get_location("200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 200)
    set_rule(multiworld.get_location("300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 300)
    set_rule(multiworld.get_location("400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 400)
    set_rule(multiworld.get_location("500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 500)
    set_rule(multiworld.get_location("600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 600)
    set_rule(multiworld.get_location("700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 700)
    set_rule(multiworld.get_location("800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 800)
    set_rule(multiworld.get_location("900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 900)
    set_rule(multiworld.get_location("1000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1000)
    set_rule(multiworld.get_location("1100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1100)
    set_rule(multiworld.get_location("1200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1200)
    set_rule(multiworld.get_location("1300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1300)
    set_rule(multiworld.get_location("1400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1400)
    set_rule(multiworld.get_location("1500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1500)
    set_rule(multiworld.get_location("1600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1600)
    set_rule(multiworld.get_location("1700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1700)
    set_rule(multiworld.get_location("1800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1800)
    set_rule(multiworld.get_location("1900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 1900)
    set_rule(multiworld.get_location("2000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2000)
    set_rule(multiworld.get_location("2100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2100)
    set_rule(multiworld.get_location("2200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2200)
    set_rule(multiworld.get_location("2300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2300)
    set_rule(multiworld.get_location("2400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2400)
    set_rule(multiworld.get_location("2500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2500)
    set_rule(multiworld.get_location("2600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2600)
    set_rule(multiworld.get_location("2700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2700)
    set_rule(multiworld.get_location("2800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2800)
    set_rule(multiworld.get_location("2900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2900)
    set_rule(multiworld.get_location("3000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3000)
    set_rule(multiworld.get_location("2100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2100)
    set_rule(multiworld.get_location("2200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2200)
    set_rule(multiworld.get_location("2300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2300)
    set_rule(multiworld.get_location("2400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2400)
    set_rule(multiworld.get_location("2500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2500)
    set_rule(multiworld.get_location("2600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2600)
    set_rule(multiworld.get_location("2700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2700)
    set_rule(multiworld.get_location("2800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2800)
    set_rule(multiworld.get_location("2900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 2900)
    set_rule(multiworld.get_location("3000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3000)
    set_rule(multiworld.get_location("3100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3100)
    set_rule(multiworld.get_location("3200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3200)
    set_rule(multiworld.get_location("3300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3300)
    set_rule(multiworld.get_location("3400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3400)
    set_rule(multiworld.get_location("3500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3500)
    set_rule(multiworld.get_location("3600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3600)
    set_rule(multiworld.get_location("3700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3700)
    set_rule(multiworld.get_location("3800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3800)
    set_rule(multiworld.get_location("3900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 3900)
    set_rule(multiworld.get_location("4000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4000)
    set_rule(multiworld.get_location("4100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4100)
    set_rule(multiworld.get_location("4200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4200)
    set_rule(multiworld.get_location("4300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4300)
    set_rule(multiworld.get_location("4400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4400)
    set_rule(multiworld.get_location("4500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4500)
    set_rule(multiworld.get_location("4600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4600)
    set_rule(multiworld.get_location("4700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4700)
    set_rule(multiworld.get_location("4800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4800)
    set_rule(multiworld.get_location("4900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 4900)
    set_rule(multiworld.get_location("5000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5000)
    set_rule(multiworld.get_location("5100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5100)
    set_rule(multiworld.get_location("5200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5200)
    set_rule(multiworld.get_location("5300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5300)
    set_rule(multiworld.get_location("5400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5400)
    set_rule(multiworld.get_location("5500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5500)
    set_rule(multiworld.get_location("5600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5600)
    set_rule(multiworld.get_location("5700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5700)
    set_rule(multiworld.get_location("5800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5800)
    set_rule(multiworld.get_location("5900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 5900)
    set_rule(multiworld.get_location("6000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6000)
    set_rule(multiworld.get_location("6100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6100)
    set_rule(multiworld.get_location("6200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6200)
    set_rule(multiworld.get_location("6300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6300)
    set_rule(multiworld.get_location("6400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6400)
    set_rule(multiworld.get_location("6500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6500)
    set_rule(multiworld.get_location("6600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6600)
    set_rule(multiworld.get_location("6700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6700)
    set_rule(multiworld.get_location("6800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6800)
    set_rule(multiworld.get_location("6900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 6900)
    set_rule(multiworld.get_location("7000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7000)
    set_rule(multiworld.get_location("7100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7100)
    set_rule(multiworld.get_location("7200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7200)
    set_rule(multiworld.get_location("7300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7300)
    set_rule(multiworld.get_location("7400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7400)
    set_rule(multiworld.get_location("7500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7500)
    set_rule(multiworld.get_location("7600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7600)
    set_rule(multiworld.get_location("7700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7700)
    set_rule(multiworld.get_location("7800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7800)
    set_rule(multiworld.get_location("7900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 7900)
    set_rule(multiworld.get_location("8000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8000)
    set_rule(multiworld.get_location("8100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8100)
    set_rule(multiworld.get_location("8200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8200)
    set_rule(multiworld.get_location("8300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8300)
    set_rule(multiworld.get_location("8400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8400)
    set_rule(multiworld.get_location("8500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8500)
    set_rule(multiworld.get_location("8600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8600)
    set_rule(multiworld.get_location("8700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8700)
    set_rule(multiworld.get_location("8800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8800)
    set_rule(multiworld.get_location("8900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 8900)
    set_rule(multiworld.get_location("9000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9000)
    set_rule(multiworld.get_location("9100pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9100)
    set_rule(multiworld.get_location("9200pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9200)
    set_rule(multiworld.get_location("9300pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9300)
    set_rule(multiworld.get_location("9400pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9400)
    set_rule(multiworld.get_location("9500pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9500)
    set_rule(multiworld.get_location("9600pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9600)
    set_rule(multiworld.get_location("9700pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9700)
    set_rule(multiworld.get_location("9800pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9800)
    set_rule(multiworld.get_location("9900pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 9900)
    set_rule(multiworld.get_location("10000pts", player), lambda state, : _ucn_calculate_max_possible_score(state, player) >= 10000)
