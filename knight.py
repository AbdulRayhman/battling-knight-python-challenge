from dataclasses import dataclass, field
from item import Item
from position import Pos
STATUS_OPTS = ('LIVE', 'DEAD', 'DROWNED')


@dataclass
class Knight:
    clr: str
    name: str
    pos: Pos
    status: str = STATUS_OPTS[0]
    item: Item = None
    base_attack: int = 1
    base_defence: int = 1

    def update_status(self, idx):
        self.status = STATUS_OPTS[idx]
