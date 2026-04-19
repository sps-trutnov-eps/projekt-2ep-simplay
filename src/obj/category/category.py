from lxml import etree

from obj.game import Game

class Category:
    """
    Reprezentuje kategorii (skupinu) her.
    Zajišťuje propojení mezi hrami v paměti a jejich zápisem do XML souboru.
    """

    def __init__(self, uuid: str, name: str, games: list[Game] = []) -> None:
        self.uuid = uuid
        self.games: list[Game] = games
        self.name = name

        # Inicializace XML parseru pro možnost okamžité aktualizace dat
        parser = etree.XMLParser(remove_blank_text=True)
        xml_tree = etree.parse("data/categories.xml", parser)
        self.xml_root = xml_tree.getroot()


    def getUUID(self) -> str:
        """Vrátí unikátní identifikátor kategorie."""
        return self.uuid

    def getGames(self) -> list[Game]:
        """Vrátí seznam her přiřazených do této kategorie."""
        return self.games

    def addGame(self, game: Game) -> None:
        """
        Přidá hru do kategorie a okamžitě aktualizuje XML soubor.
        """
        self.games.append(game)
        # Vyhledání příslušné kategorie v XML stromu pomocí XPath
        games_element = self.xml_root.xpath("category[@uuid=" + self.uuid + "]/games")[0]

        # Vytvoření nového XML elementu pro hru
        game_element = etree.SubElement(games_element, "game")
        game_element.set("uuid", game.getUUID())

        games_element.append(game_element)

        # Uložení změn do souboru
        with open("data/categories.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def getName(self) -> str:
        """Vrátí název kategorie."""
        return self.name