from .Items import UcnItem, UcnItemData, item_table, item_data_table
from .Locations import  advancement_table, location_table
from .Regions import region_data_table
from .Rules import set_gamerules
from worlds.generic.Rules import exclusion_rules
from BaseClasses import Location, Region, Entrance, Tutorial, Item, ItemClassification
from .Options import ucn_options
from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, components, Type
from multiprocessing import Process
from typing import List
from typing import List

from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Regions import region_data_table





class UcnLocation(Location):
    game = "Ultimate Custom Night"



class UcnWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Ultimate Custom Night software on your computer. This guide covers "
        "single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Fewffwa"]
    )]


class UcnWorld(World):
    """
    Welcome to the ultimate FNAF mashup, featuring 50 selectable characters and custom difficulties!
    """
    game = "Ultimate Custom Night"
    option_definitions = ucn_options
    web = UcnWeb()

    location_name_to_id = location_table
    item_name_to_id = item_table

    data_version = 1

    def create_items(self) -> None:
        item_pool: List[UcnItem] = []
        for name, item in item_data_table.items():
            if item.code and item.can_create(self.multiworld, self.player):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def set_rules(self):
        set_gamerules(self.multiworld, self.player)
        location = self.multiworld.get_location("10000pts", self.player)
        self.multiworld.completion_condition[self.player] = lambda state: state.can_reach(location)

    def create_regions(self) -> None:
        # Create regions.
        for region_name in region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        for region_name, region_data in region_data_table.items():
            region = self.multiworld.get_region(region_name, self.player)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in advancement_table.items()
                if location_data.region == region_name and location_data.can_create(self.multiworld, self.player)
            }, UcnLocation)
            region.add_exits(region_data_table[region_name].connecting_regions)

        # Place locked locations.
        for location_name, location_data in locked_locations.items():
            # Ignore locations we never created.
            if not location_data.can_create(self.multiworld, self.player):
                continue

            locked_item = self.create_item(advancement_table[location_name].locked_item)
            self.multiworld.get_location(location_name, self.player).place_locked_item(locked_item)


    def create_item(self, name: str) -> UcnItem:
        return UcnItem(name, item_data_table[name].type, item_data_table[name].code, self.player)
    
    def create_event(self, name: str, classification: ItemClassification) -> Item:
        return UcnItem(None, classification, None, self.player)
    
locked_locations = {name: data for name, data in advancement_table.items() if data.locked_item}