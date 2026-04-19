import time
from pathlib import Path

class TimeCount:
    """
    Třída pro sledování celkového času stráveného v aplikaci.
    Naměřená data ukládá do souboru data/time.txt v sekundách.
    """

    def __init__(self):
        # Definice cesty k souboru relativně k umístění tohoto skriptu
        # Cesta: src/obj/time/time_count.py -> src/data/time.txt
        self.data_path = Path(__file__).parent.parent.parent / "data" / "time.txt"
        
        # Zaznamenání času spuštění aplikace
        self.start_time = time.time()
        self.current_time = 0
        self.played_time = 0
        
        # Načtení dříve uloženého času s ošetřením chyb
        try:
            if self.data_path.exists():
                with open(self.data_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    self.played_time = int(content) if content else 0
            else:
                self.played_time = 0
        except (FileNotFoundError, ValueError, PermissionError):
            self.played_time = 0


    def end(self) -> None:
        """Vypočítá uplynulý čas od spuštění a přičte jej k celkovému uloženému času."""
        self.current_time = time.time()
        # Celkový čas = (současný čas - čas spuštění) + dříve odehraný čas
        total_seconds = int(self.current_time) - int(self.start_time) + int(self.played_time)

        try:
            # Ujistíme se, že složka existuje
            self.data_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_path, "w", encoding="utf-8") as f:
                f.write(str(total_seconds))
        except PermissionError:
            pass # V produkci by zde bylo logování chyby

    @staticmethod
    def getPlayedTime() -> float:
        """Vrátí celkový odehraný čas převedený na hodiny (zaokrouhleno na 2 desetinná místa)."""
        data_path = Path(__file__).parent.parent.parent / "data" / "time.txt"
        try:
            if data_path.exists():
                with open(data_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    seconds = int(content) if content else 0
                    return round(seconds / 3600, 2)
            return 0.0
        except (FileNotFoundError, ValueError, PermissionError):
            return 0.0