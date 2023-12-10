from Obj.game import Game


class Category:

    def __init__(self, uuid: str, name: str, games: list[Game] = []) -> None:
        self.uuid = uuid
        self.games: list[Game] = games
        self.name = name


    def getUUID(self) -> str:
        return self.uuid

    def getGames(self) -> list[Game]:
        return self.games

    def addGame(self, game: Game) -> None:
        self.games.append(game)

    def getName(self) -> str:
        return self.name