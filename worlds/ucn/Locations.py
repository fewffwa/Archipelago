from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location, MultiWorld






class UcnAdvancement(Location):
    game: str = "Ultimate Custom Night"

class AdvData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[MultiWorld, int], bool] = lambda multiworld, player: True
    locked_item: Optional[str] = None

advancement_table: Dict[str, AdvData] = {
"100pts": AdvData(
    region="Office",
    address=502000,
),
"200pts": AdvData(
    region="Office",
    address=502001,
),
"300pts": AdvData(
    region="Office",
    address=502002,
),
"400pts": AdvData(
    region="Office",
    address=502003,
),
"500pts": AdvData(
    region="Office",
    address=502004,
),
"600pts": AdvData(
    region="Office",
    address=502005,
),
"700pts": AdvData(
    region="Office",
    address=502006,
),
"800pts": AdvData(
    region="Office",
    address=502007,
),
"900pts": AdvData(
    region="Office",
    address=502008,
),
"1000pts": AdvData(
    region="Office",
    address=502009,
),
"1100pts": AdvData(
    region="Office",
    address=502010,
),
"1200pts": AdvData(
    region="Office",
    address=502011,
),
"1300pts": AdvData(
    region="Office",
    address=502012,
),
"1400pts": AdvData(
    region="Office",
    address=502013,
),
"1500pts": AdvData(
    region="Office",
    address=502014,
),
"1600pts": AdvData(
    region="Office",
    address=502015,
),
"1700pts": AdvData(
    region="Office",
    address=502016,
),
"1800pts": AdvData(
    region="Office",
    address=502017,
),
"1900pts": AdvData(
    region="Office",
    address=502018,
),
"2000pts": AdvData(
    region="Office",
    address=502019,
),
"2100pts": AdvData(
    region="Office",
    address=502020,
),
"2200pts": AdvData(
    region="Office",
    address=502021,
),
"2300pts": AdvData(
    region="Office",
    address=502022,
),
"2400pts": AdvData(
    region="Office",
    address=502023,
),
"2500pts": AdvData(
    region="Office",
    address=502024,
),
"2600pts": AdvData(
    region="Office",
    address=502025,
),
"2700pts": AdvData(
    region="Office",
    address=502026,
),
"2800pts": AdvData(
    region="Office",
    address=502027,
),
"2900pts": AdvData(
    region="Office",
    address=502028,
),
"3000pts": AdvData(
    region="Office",
    address=502029,
),
"3100pts": AdvData(
    region="Office",
    address=502030,
),
"3200pts": AdvData(
    region="Office",
    address=502031,
),
"3300pts": AdvData(
    region="Office",
    address=502032,
),
"3400pts": AdvData(
    region="Office",
    address=502033,
),
"3500pts": AdvData(
    region="Office",
    address=502034,
),
"3600pts": AdvData(
    region="Office",
    address=502035,
),
"3700pts": AdvData(
    region="Office",
    address=502036,
),
"3800pts": AdvData(
    region="Office",
    address=502037,
),
"3900pts": AdvData(
    region="Office",
    address=502038,
),
"4000pts": AdvData(
    region="Office",
    address=502039,
),
"4100pts": AdvData(
    region="Office",
    address=502040,
),
"4200pts": AdvData(
    region="Office",
    address=502041,
),
"4300pts": AdvData(
    region="Office",
    address=502042,
),
"4400pts": AdvData(
    region="Office",
    address=502043,
),
"4500pts": AdvData(
    region="Office",
    address=502044,
),
"4600pts": AdvData(
    region="Office",
    address=502045,
),
"4700pts": AdvData(
    region="Office",
    address=502046,
),
"4800pts": AdvData(
    region="Office",
    address=502047,
),
"4900pts": AdvData(
    region="Office",
    address=502048,
),
"5000pts": AdvData(
    region="Office",
    address=502049,
),
"5100pts": AdvData(
    region="Office",
    address=502050,
),
"5200pts": AdvData(
    region="Office",
    address=502051,
),
"5300pts": AdvData(
    region="Office",
    address=502052,
),
"5400pts": AdvData(
    region="Office",
    address=502053,
),
"5500pts": AdvData(
    region="Office",
    address=502054,
),
"5600pts": AdvData(
    region="Office",
    address=502055,
),
"5700pts": AdvData(
    region="Office",
    address=502056,
),
"5800pts": AdvData(
    region="Office",
    address=502057,
),
"5900pts": AdvData(
    region="Office",
    address=502058,
),
"6000pts": AdvData(
    region="Office",
    address=502059,
),
"6100pts": AdvData(
    region="Office",
    address=502060,
),
"6200pts": AdvData(
    region="Office",
    address=502061,
),
"6300pts": AdvData(
    region="Office",
    address=502062,
),
"6400pts": AdvData(
    region="Office",
    address=502063,
),
"6500pts": AdvData(
    region="Office",
    address=502064,
),
"6600pts": AdvData(
    region="Office",
    address=502065,
),
"6700pts": AdvData(
    region="Office",
    address=502066,
),
"6800pts": AdvData(
    region="Office",
    address=502067,
),
"6900pts": AdvData(
    region="Office",
    address=502068,
),
"7000pts": AdvData(
    region="Office",
    address=502069,
),
"7100pts": AdvData(
    region="Office",
    address=502070,
),
"7200pts": AdvData(
    region="Office",
    address=502071,
),
"7300pts": AdvData(
    region="Office",
    address=502072,
),
"7400pts": AdvData(
    region="Office",
    address=502073,
),
"7500pts": AdvData(
    region="Office",
    address=502074,
),
"7600pts": AdvData(
    region="Office",
    address=502075,
),
"7700pts": AdvData(
    region="Office",
    address=502076,
),
"7800pts": AdvData(
    region="Office",
    address=502077,
),
"7900pts": AdvData(
    region="Office",
    address=502078,
),
"8000pts": AdvData(
    region="Office",
    address=502079,
),
"8100pts": AdvData(
    region="Office",
    address=502080,
),
"8200pts": AdvData(
    region="Office",
    address=502081,
),
"8300pts": AdvData(
    region="Office",
    address=502082,
),
"8400pts": AdvData(
    region="Office",
    address=502083,
),
"8500pts": AdvData(
    region="Office",
    address=502084,
),
"8600pts": AdvData(
    region="Office",
    address=502085,
),
"8700pts": AdvData(
    region="Office",
    address=502086,
),
"8800pts": AdvData(
    region="Office",
    address=502087,
),
"8900pts": AdvData(
    region="Office",
    address=502088,
),
"9000pts": AdvData(
    region="Office",
    address=502089,
),
"9100pts": AdvData(
    region="Office",
    address=502080,
),
"9200pts": AdvData(
    region="Office",
    address=502091,
),
"9300pts": AdvData(
    region="Office",
    address=502092,
),
"9400pts": AdvData(
    region="Office",
    address=502093,
),
"9500pts": AdvData(
    region="Office",
    address=502094,
),
"9600pts": AdvData(
    region="Office",
    address=502095,
),
"9700pts": AdvData(
    region="Office",
    address=502096,
),
"9800pts": AdvData(
    region="Office",
    address=502097,
),
"9900pts": AdvData(
    region="Office",
    address=502098,
),
"10000pts": AdvData(
    region="Office",
    address=502099,
),    
}

events_table = {
}

location_table = {name: data.address for name, data in advancement_table.items() if data.address is not None}
locked_locations = {name: data for name, data in advancement_table.items() if data.locked_item}