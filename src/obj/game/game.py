import os
import subprocess

class Game:
    """
    Reprezentuje jednotlivou hru v launcheru.
    Uchovává informace o názvu, cestě k souboru a unikátním ID.
    """

    def __init__(self, uuid: str, name: str, path: str) -> None:
        self.uuid = uuid
        self.name = name
        self.path = path


    def getUUID(self) -> str:
        """Vrátí unikátní identifikátor hry."""
        return self.uuid

    def getName(self) -> str:
        """Vrátí název hry."""
        return self.name

    def getPath(self) -> str:
        """Vrátí systémovou cestu ke spustitelnému souboru hry."""
        return self.path

    def run(self) -> None:
        """
        Spustí hru na základě přípony souboru.
        Podporuje .exe (přímé spuštění) a .py (spuštění přes interpret Pythonu).
        """
        # Získání přípony souboru pomocí standardní knihovny
        _, extension = os.path.splitext(self.path)
        extension = extension.lower().lstrip('.')
        
        if extension == "exe":
            os.startfile(self.path)
        elif extension == "py":
            # Spuštění python skriptu jako nového procesu
            subprocess.call(["python", self.path])