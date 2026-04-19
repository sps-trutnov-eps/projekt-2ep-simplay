from lxml import etree

from obj.category import Category
from obj.game import *

class CategoryManager:
    """
    Správce kategorií, který organizuje hry do skupin.
    Umožňuje načítání a ukládání struktury kategorií v XML (data/categories.xml).
    """

    def __init__(self, game_manager: GameManager) -> None:
        self.game_manager = game_manager

        parser = etree.XMLParser(remove_blank_text=True)
        self.xml_tree = etree.parse("data/categories.xml", parser)
        self.xml_root = self.xml_tree.getroot()
        
        self.categories: list[Category] = []

        self.loadCategories()


    def loadCategories(self) -> None:
        """Načte kategorie a přiřadí k nim příslušné objekty her."""
        for child in self.xml_root:
            uuid, name, games = "", "" , []

            uuid = child.attrib["uuid"]
            name = child[0].text

            for xml_game in child[1]:
                game_uuid = xml_game.attrib["uuid"]
                game = self.game_manager.getGameByUUID(game_uuid)
                games.append(game)

            category = Category(uuid, name, games)
            self.categories.append(category)

    def getCategories(self) -> list[Category]:
        """Vrátí seznam všech načtených kategorií."""
        return self.categories

    def getCategoryByUUID(self, uuid: int) -> Category:
        """Vyhledá kategorii podle UUID."""
        for category in self.categories:
            if (int(category.getUUID()) == int(uuid)):
                return category

    def addCategory(self, name: str) -> None:
        """Vytvoří novou kategorii a uloží ji do XML."""
        uuid = str(self.getLastUUID() + 1)

        self.xml_root.append(self.__createCategoryXML(uuid, name, []))
        self.save()

        category = Category(uuid, name)
        self.categories.append(category)


    def getLastUUID(self) -> int:
        """Získá ID pro novou kategorii na základě počtu stávajících."""
        if (len(self.categories) > 0):
            if (len(self.categories) == 1):
                return 1
            return len(self.categories)
        return 0


    def save(self) -> None:
        """Uloží aktuální stav XML stromu do souboru."""
        with open("data/categories.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __createCategoryXML(self, uuid: str, name: str, games: list[Game]) -> etree.Element:
        """Vytvoří XML strukturu pro novou kategorii."""
        xml_category = etree.SubElement(self.xml_root, "category")
        xml_category.set("uuid", uuid)
        
        xml_name = etree.SubElement(xml_category, "name")
        xml_name.text = name
        xml_category.append(xml_name)

        xml_games = etree.SubElement(xml_category, "games")
        xml_category.append(xml_games)
        

        for game in games:
            xml_game = etree.SubElement(games, "game")
            xml_game.set("uuid", game.getUUID())
            xml_category.append(xml_name)
            

        return xml_category