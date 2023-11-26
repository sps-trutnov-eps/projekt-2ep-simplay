from lxml import etree

from obj.add_category.category import Category


class CategoryManager:

    def __init__(self) -> None:
        parser = etree.XMLParser(remove_blank_text=True)
        self.xml_tree = etree.parse("data/category.xml", parser)
        self.xml_root = self.xml_tree.getroot()

        self.categories = []


        self.loadCategories()


    def loadCategories(self) -> None:
        uuid, category_name, path = "", "", ""                                                                                   # Adding data from the file to the list
        
        for child in self.xml_root:                                                                                     
            uuid = child.attrib["uuid"]
            category_name = child[0].text
            path = child[1].text

            category = Category(uuid, category_name, path)
            self.categories.append(category)

    def getCategories(self) -> list[Category]:
        return self.categories

    def getCategoryByUUID(self, uuid: int) -> Category:
        for category in self.categories:
            if (category.getUUID() == uuid):
                return category

    def addCategory(self, category_name: str, path: str) -> None:
        uuid = str(self.getLastUUID() + 1)                                                                              # Creating UUID

        self.__saveXMLCategory(uuid, category_name, path)

        category = Category(uuid, category_name, path)                                                                                   # Adding changes to active list
        self.categories.append(category)

    def removeCategory(self, uuid: str) -> None:
        self.__removeXMLGame(uuid)

        for category in self.categories:                                                                                         # Removing the game from the list
            if (category.getUUID() == uuid):
                self.categories.remove(category)

    def getLastUUID(self) -> int:                                                                                       # Getting last uuid             
        if (len(self.categories) > 0):
            if (len(self.categories) == 1):
                return 1
            return len(self.categories) - 1
        return 0


    def __saveXMLCategory(self, uuid: str, category_name: str, path: str) -> None:
        self.xml_root.append(self.__createCategoryXML(uuid, category_name, path))                                                    # Adding changes to the file
        with open("data/category.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __removeXMLGame(self, uuid) -> None:
        for category in self.xml_tree.xpath(str.format("//category[@uuid=\"{0}\"]", uuid)):                                     # Removing the game from xml
            category.getparent().remove(category)

        with open("data/category.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

    def __createCategoryXML(self, uuid: str, category_name: str, path: str) -> etree.Element:                                        # Creating new XML for game record
        xml_category = etree.SubElement(self.xml_root, "game")
        xml_category.set("uuid", uuid)

        xml_category_name = etree.SubElement(xml_category, "category_name")
        xml_category_name.text = category_name
        xml_category.append(category_name)

        xml_path = etree.SubElement(xml_category, "path")
        xml_path.text = path
        xml_category.append(xml_path)

        return xml_category