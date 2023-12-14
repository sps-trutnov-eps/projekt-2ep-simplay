import os
import subprocess


class Game:

    def __init__(self, uuid: str, name: str, path: str) -> None:
        self.uuid = uuid
        self.name = name
        self.path = path


    def getUUID(self) -> str:
        return self.uuid

    def getName(self) -> str:
        return self.name

    def getPath(self) -> str:
        return self.path

    def run(self) -> None:
        extension = os.path.basename(self.path)
        extension = extension.split('.')[1]
        if extension == "exe":
            os.startfile(self.path)
        elif extension == "py":
            subprocess.call(["python", self.path])