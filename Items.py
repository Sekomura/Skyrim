from typing import Dict, NamedTuple, Optional

from BaseClasses import Item, ItemClassification


class SkyrimItem(Item):
  game: str = "Skyrim"


class SkyrimItemData(NamedTuple):
   category: str
   code: Optional[int] = None
   classification: ItemClassification = ItemClassification.filler
   max_quantity: int = 1
   weight: int = 1
