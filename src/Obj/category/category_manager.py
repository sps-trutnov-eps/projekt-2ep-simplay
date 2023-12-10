from lxml import etree

from Obj.category import Category
from Obj.game import *

class CategoryManager:

    def __init__(self, game_manager: GameManager) -> None:
        self.game_manager = game_manager

        parser = etree.XMLParser(remove_blank_text=True)
        self.xml_tree = etree.parse("data/categories.xml", parser)
        self.xml_root = self.xml_tree.getroot()
        
        self.categories: list[Category] = []

        self.loadCategories()


    def loadCategories(self) -> None:
        uuid, name, games = "", "" , []                                                                               # Adding data from the file to the list
        
        for child in self.xml_root:
            uuid = child.attrib["uuid"]
            name = child[0].text

            for xml_game in child[1]:
                uuid = xml_game.attrib["uuid"]

                game = self.game_manager.getGameByUUID(uuid)
                games.append(game)

            category = Category(uuid, name, games)
            self.categories.append(category)

    def getCategories(self) -> list[Category]:
        return self.categories

    def getCategoryByUUID(self, uuid: int) -> Category:
        for category in self.categories:
            if (int(category.getUUID()) == uuid):
                return category

    def addCategory(self, name: str) -> None:
        uuid = str(self.getLastUUID() + 1)                                                                              # Creating UUID

        self.__saveXMLCategory(uuid, name, [])

        category = Category(uuid, name)                                                                                   # Adding changes to active list
        self.categories.append(category)


    def getLastUUID(self) -> int:                                                                                       # Getting last uuid        
        if (len(self.categories) > 0):
            if (len(self.categories) == 1):
                return 1
            return len(self.categories) - 1
        return 0


    def __saveXMLCategory(self, uuid: str, name: str, games: list[Game]) -> None:
        self.xml_root.append(self.__createCategoryXML(uuid, name, games))                                                    # Adding changes to the file
        with open("data/categories.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __createCategoryXML(self, uuid: str, name: str, games: list[Game]) -> etree.Element:                                        # Creating new XML for game record
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