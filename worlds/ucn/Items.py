from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification, MultiWorld


class UcnItem(Item):
    game = "Ultimate Custom Night"


class UcnItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True


item_data_table: Dict[str, UcnItemData] = {
        "Freddy Fazbear": UcnItemData(
        code=502100,
        type=ItemClassification.progression,
    ),
        "Bonnie": UcnItemData(
        code=502101,
        type=ItemClassification.progression,
    ),

        "Chica": UcnItemData(
        code=502102,
        type=ItemClassification.progression,
    ),
        "Foxy": UcnItemData(
        code=502103,
        type=ItemClassification.progression,
    ),
        "Toy Freddy": UcnItemData(
        code=502104,
        type=ItemClassification.progression,
    ),
        "Toy Bonnie": UcnItemData(
        code=502105,
        type=ItemClassification.progression,
    ),
        "Toy Chica": UcnItemData(
        code=502106,
        type=ItemClassification.progression,
    ),
        "Mangle": UcnItemData(
        code=502107,
        type=ItemClassification.progression,
    ),
        "BB": UcnItemData(
        code=502108,
        type=ItemClassification.progression,
    ),
        "Withered Chica": UcnItemData(
        code=502109,
        type=ItemClassification.progression,
    ),
        "Withered Bonnie": UcnItemData(
        code=502110,
        type=ItemClassification.progression,
    ),
        "JJ": UcnItemData(
        code=502111,
        type=ItemClassification.progression,
    ),
        "Marionette": UcnItemData(
        code=502112,
        type=ItemClassification.progression,
    ),
        "Golden Freddy": UcnItemData(
        code=502113,
        type=ItemClassification.progression,
    ),
        "Springtrap": UcnItemData(
        code=502114,
        type=ItemClassification.progression,
    ),
        "Phantom Freddy": UcnItemData(
        code=502115,
        type=ItemClassification.progression,
    ),
        "Pahntom Mangle": UcnItemData(
        code=502116,
        type=ItemClassification.progression,
    ),
        "Phantom BB": UcnItemData(
        code=502117,
        type=ItemClassification.progression,
    ),
        "Nightmare Freddy": UcnItemData(
        code=502118,
        type=ItemClassification.progression,
    ),
        "Nightmare Bonnie": UcnItemData(
        code=502119,
        type=ItemClassification.progression,
    ),
        "Nightmare Fredbear": UcnItemData(
        code=502120,
        type=ItemClassification.progression,
    ),
        "Nightmare": UcnItemData(
        code=502121,
        type=ItemClassification.progression,
    ),
        "Jack-O-Chica": UcnItemData(
        code=502122,
        type=ItemClassification.progression,
    ),
        "Nightmare Mangle": UcnItemData(
        code=502123,
        type=ItemClassification.progression,
    ),
        "Nightmarionne": UcnItemData(
        code=502124,
        type=ItemClassification.progression,
    ),
        "Nightmare BB": UcnItemData(
        code=502125,
        type=ItemClassification.progression,
    ),
        "Old Man Consequences": UcnItemData(
        code=502126,
        type=ItemClassification.progression,
    ),
        "Circus Baby": UcnItemData(
        code=502127,
        type=ItemClassification.progression,
    ),
        "Ballora": UcnItemData(
        code=502128,
        type=ItemClassification.progression,
    ),
        "Funtime Foxy": UcnItemData(
        code=502129,
        type=ItemClassification.progression,
    ),
        "Ennard": UcnItemData(
        code=502130,
        type=ItemClassification.progression,
    ),
        "Trash and the Gang": UcnItemData(
        code=502131,
        type=ItemClassification.progression,
    ),
        "Helpy": UcnItemData(
        code=502132,
        type=ItemClassification.progression,
    ),
        "Happy Frog": UcnItemData(
        code=502133,
        type=ItemClassification.progression,
    ),
        "Mr. Hippo": UcnItemData(
        code=502134,
        type=ItemClassification.progression,
    ),
        "Pigpatch": UcnItemData(
        code=502135,
        type=ItemClassification.progression,
    ),
        "Orville Elephant": UcnItemData(
        code=502136,
        type=ItemClassification.progression,
    ),
        "Rockstar Freddy": UcnItemData(
        code=502138,
        type=ItemClassification.progression,
    ),
        "Rockstar Bonnie": UcnItemData(
        code=502139,
        type=ItemClassification.progression,
    ),
        "Rockstar Chica": UcnItemData(
        code=502140,
        type=ItemClassification.progression,
    ),
        "Rockstar Foxy": UcnItemData(
        code=502141,
        type=ItemClassification.progression,
    ),
        "Music Man": UcnItemData(
        code=502142,
        type=ItemClassification.progression,
    ),
        "El Chip": UcnItemData(
        code=502143,
        type=ItemClassification.progression,
    ),
        "Molten Freddy": UcnItemData(
        code=502144,
        type=ItemClassification.progression,
    ),
        "Funtime Chica": UcnItemData(
        code=502145,
        type=ItemClassification.progression,
    ),
        "Scrap Baby": UcnItemData(
        code=502146,
        type=ItemClassification.progression,
    ),
        "Afton": UcnItemData(
        code=502147,
        type=ItemClassification.progression,
    ),
        "Lefty": UcnItemData(
        code=502148,
        type=ItemClassification.progression,
    ),
        "Phone Guy": UcnItemData(
        code=502149,
        type=ItemClassification.progression,
    ),
        "Left Door": UcnItemData(
        code=502150,
        type=ItemClassification.progression,
    ),
        "Right Door": UcnItemData(
        code=502151,
        type=ItemClassification.progression,
    ),
        "Music Box": UcnItemData(
        code=502152,
        type=ItemClassification.progression,
    ),
        "Change Music": UcnItemData(
        code=502153,
        type=ItemClassification.progression,
    ),
        "Global Music Box": UcnItemData(
        code=502154,
        type=ItemClassification.progression,
    ),
        "Mask": UcnItemData(
        code=502155,
        type=ItemClassification.progression,
    ),
        "Side Vent": UcnItemData(
        code=502156,
        type=ItemClassification.progression,
    ),
        "Forward Vent": UcnItemData(
        code=502157,
        type=ItemClassification.progression,
    ),
        "Snare": UcnItemData(
        code=502158,
        type=ItemClassification.progression,
    ),
        "Flashlight": UcnItemData(
        code=502159,
        type=ItemClassification.progression,
    ),
        "Nightmare Bonnie Plush": UcnItemData(
        code=502160,
        type=ItemClassification.progression,
    ),
        "Nightmare Mangle Plush": UcnItemData(
        code=502161,
        type=ItemClassification.progression,
    ),
        "Circus Baby Plush": UcnItemData(
        code=502162,
        type=ItemClassification.progression,
    ),
        "Deathcoin": UcnItemData(
        code=502163,
        type=ItemClassification.useful,
    ),
        "Audio Lure": UcnItemData(
        code=502164,
        type=ItemClassification.progression,
    ),
        "Heater": UcnItemData(
        code=502165,
        type=ItemClassification.progression,
    ),
        "Shock": UcnItemData(
        code=502166,
        type=ItemClassification.progression,
    ),
        "Silent Vent": UcnItemData(
        code=502167,
        type=ItemClassification.useful,
    ),
        "AC": UcnItemData(
        code=502168,
        type=ItemClassification.progression,
    ),
        "Generator": UcnItemData(
        code=502169,
        type=ItemClassification.useful,
    ),
        "Frigid Upgrade": UcnItemData(
        code=502170,
        type=ItemClassification.useful,
    ),
        "3 Coins Upgrade": UcnItemData(
        code=502171,
        type=ItemClassification.useful,
    ),
        "Battery Upgrade": UcnItemData(
        code=502172,
        type=ItemClassification.useful,
    ),
        "DD Trap": UcnItemData(
        code=502173,
        type=ItemClassification.trap,
    ),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
