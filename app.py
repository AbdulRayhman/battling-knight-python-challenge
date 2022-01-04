from pathlib import Path
from json import dumps
from board import ArenaBoard


class Game:
    _arena = ArenaBoard()
    _gameMoves = None

    def __init__(self) -> None:
        self._arena.getArenaBoard()
        self._arena.renderArenaBoard()

    def readMoveFromFile(self):
        movesData = Path('./movements.txt').read_text()
        moves = movesData.strip().split('\n')
        moves.pop(0)
        moves.pop(moves.__len__()-1)
        self._gameMoves = moves
        for mov in self._gameMoves:
            self._arena.moveKnightInArenaBoard(
                mov.split(':')[0], mov.split(':')[1])

    def writeToFile(self, data):
        Path('./result.json').write_text(dumps(data))

    def getFormattedPosition(self, p):
        return p.to_json() if p else None

    def itemHaveKnight(self, item):
        itemPos = item.pos
        return True if itemPos.knight else False

    def getItemData(self, item):
        return None if item == None else item.name

    def finalResult(self):
        finalRes = {
            "Red": [self.getFormattedPosition(self._arena.R.pos), self._arena.R.status, self.getItemData(self._arena.R.item), self._arena.R.base_attack, self._arena.R.base_defence],
            "Yellow": [self.getFormattedPosition(self._arena.Y.pos), self._arena.Y.status, self.getItemData(self._arena.Y.item), self._arena.Y.base_attack, self._arena.Y.base_defence],
            "Blue": [self.getFormattedPosition(self._arena.B.pos), self._arena.B.status, self.getItemData(self._arena.B.item), self._arena.B.base_attack, self._arena.B.base_defence],
            "Green": [self.getFormattedPosition(self._arena.G.pos), self._arena.G.status, self.getItemData(self._arena.G.item), self._arena.G.base_attack, self._arena.G.base_defence],
            "MagicStaff": [self.getFormattedPosition(self._arena._magicStaff.pos), self.itemHaveKnight(self._arena._magicStaff)],
            "Helmet": [self.getFormattedPosition(self._arena._helmet.pos), self.itemHaveKnight(self._arena._helmet)],
            "Dagger": [self.getFormattedPosition(self._arena._dagger.pos), self.itemHaveKnight(self._arena._dagger)],
            "Axe": [self.getFormattedPosition(self._arena._axe.pos), self.itemHaveKnight(self._arena._axe)], }
        self.writeToFile(finalRes)


if __name__ == '__main__':
    game = Game()
    game.readMoveFromFile()
    game.finalResult()