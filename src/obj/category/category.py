from lxml import etree

from obj.game import Game


class Category:

    def __init__(self, uuid: str, name: str, games: list[Game] = []) -> None:
        self.uuid = uuid
        self.games: list[Game] = games
        self.name = name

        parser = etree.XMLParser(remove_blank_text=True)
        xml_tree = etree.parse("data/categories.xml", parser)
        self.xml_root = xml_tree.getroot()


    def getUUID(self) -> str:
        return self.uuid

    def getGames(self) -> list[Game]:
        return self.games

    def addGame(self, game: Game) -> None:
        self.games.append(game)
        games_element = self.xml_root.xpath("category[@uuid=" + self.uuid + "]/games")[0]

        game_element = etree.SubElement(games_element, "game")
        game_element.set("uuid", game.getUUID())

        games_element.append(game_element)


        with open("data/categories.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True, method="html"))

    def getName(self) -> str:
        return self.name