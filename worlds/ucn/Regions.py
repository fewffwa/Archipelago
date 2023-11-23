from typing import Dict, List, NamedTuple

class UcnRegionData(NamedTuple):
    connecting_regions: List[str] = []


region_data_table: Dict[str, UcnRegionData] = {
    "Menu": UcnRegionData(["Office"]),
    "Office": UcnRegionData(),
}