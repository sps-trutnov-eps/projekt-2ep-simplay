from lxml import etree

from obj.game import Game

class GameManager:
    """
    Správce her, který zajišťuje načítání, přidávání a odebírání her.
    Data jsou ukládána do XML souboru data/games.xml.
    """

    def __init__(self) -> None:
        parser = etree.XMLParser(remove_blank_text=True)
        self.xml_tree = etree.parse("data/games.xml", parser)
        self.xml_root = self.xml_tree.getroot()

        self.games = []

        self.loadGames()

    def loadGames(self) -> None:
        """Načte seznam všech her z XML souboru při inicializaci."""
        for child in self.xml_root:
            uuid = child.attrib["uuid"]
            name = child[0].text
            path = child[1].text

            game = Game(uuid, name, path)
            self.games.append(game)

    def getGames(self) -> list[Game]:
        """Vrátí aktuální seznam všech her."""
        return self.games

    def getGameByUUID(self, uuid: int) -> Game:
        """Vyhledá hru podle jejího unikátního ID."""
        for game in self.games:
            if (int(game.getUUID()) == int(uuid)):
                return game

    def addGame(self, name: str, path: str) -> None:
        """Přidá novou hru do seznamu i do XML souboru."""
        uuid = str(self.getLastUUID() + 1)

        self.__saveXMLGame(uuid, name, path)

        game = Game(uuid, name, path)
        self.games.append(game)

    def removeGame(self, uuid: str) -> None:
        """Odstraní hru ze seznamu i z XML souboru podle UUID."""
        self.__removeXMLGame(uuid)

        for game in self.games:
            if (game.getUUID() == uuid):
                self.games.remove(game)

    def getLastUUID(self) -> int:
        """Pomocná metoda pro generování unikátního ID pro novou hru."""
        if (len(self.games) > 0):
            if (len(self.games) == 1):
                return 1
            return len(self.games)
        return 0

    def __saveXMLGame(self, uuid: str, name: str, path: str) -> None:
        """Interní metoda pro zápis nové hry do XML struktury a její uložení na disk."""
        self.xml_root.append(self.__createGameXML(uuid, name, path))
        with open("data/games.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __removeXMLGame(self, uuid) -> None:
        """Interní metoda pro odstranění záznamu hry z XML souboru."""
        for game in self.xml_tree.xpath(str.format("//game[@uuid=\"{0}\"]", uuid)):
            game.getparent().remove(game)

        with open("data/games.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __createGameXML(self, uuid: str, name: str, path: str) -> etree.Element:
        """Vytvoří nový XML element reprezentující hru."""
        xml_game = etree.SubElement(self.xml_root, "game")
        xml_game.set("uuid", uuid)

        xml_name = etree.SubElement(xml_game, "name")
        xml_name.text = name
        xml_game.append(xml_name)

        xml_path = etree.SubElement(xml_game, "path")
        xml_path.text = path
        xml_game.append(xml_path)

        return xml_game
