import os


class Category:

    def __init__(self, uuid: str, category: str, path: str) -> None:
        self.uuid = uuid
        self.category = category
        self.path = path


    def getUUID(self) -> str:
        return self.uuid

    def getCategory(self) -> str:
        return self.category

    def getPath(self) -> str:
        return self.path

    def run(self) -> None:
        extension = os.path.basename(self.path)
        extension = extension.split('.')[1]
        os.startfile(self.path)