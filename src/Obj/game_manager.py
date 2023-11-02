from lxml import etree
import xml

from game import Game


class GameManager:

    def __init__(self) -> None:
        parser = etree.XMLParser(remove_blank_text=True)
        self.xml_tree = etree.parse("../data/games.xml", parser)
        self.xml_root = self.xml_tree.getroot()

        self.games = []


        self.loadGames()


    def loadGames(self) -> None:
        uuid, name, path = "", "", ""                                                                                   # Adding data from the file to the list
        
        for child in self.xml_root:                                                                                     
            uuid = child.attrib["uuid"]
            name = child[0].text
            path = child[1].text

            game = Game(uuid, name, path)
            self.games.append(game)

    def addGame(self, name: str, path: str) -> None:
        print(self.getLastUUID())
        uuid = str(self.getLastUUID() + 1)                                                                              # Creating UUID

        self.xml_root.append(self.createGameXML(uuid, name, path))                                                      # Adding changes to the file
        with open("../data/games.xml", "wb") as f:
            f.write(etree.tostring(self.xml_root, xml_declaration=True, encoding="UTF-8", pretty_print=True))

        game = Game(uuid, name, path)                                                                                   # Adding changes to active list
        self.games.append(game)

    def removeGame(self, uuid: str) -> None:
        for game in self.xml_root:
            if (game.tag == "game"):
                if (game.attrib["uuid"] == uuid):
                    pass
                    # TODO: Create removing


    def getLastUUID(self) -> int:                                                                                       # Getting last uuid             
        if (len(self.games) > 0):
            if (len(self.games) == 1):
                return 1
            return len(self.games) - 1
        return 0

    def createGameXML(self, uuid: str, name: str, path: str) -> etree.Element:                                          # Creating new XML for game record
        xml_game = etree.SubElement(self.xml_root, "game")
        xml_game.set("uuid", uuid)

        xml_name = etree.SubElement(xml_game, "name")
        xml_name.text = name
        xml_game.append(xml_name)

        xml_path = etree.SubElement(xml_game, "path")
        xml_path.text = path
        xml_game.append(xml_path)

        return xml_game



gm = GameManager()
gm.addGame('Sibenice', 'path/to/file')
gm.removeGame("3")