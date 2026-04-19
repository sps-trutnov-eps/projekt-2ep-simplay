import time

class TimeCount:
    """
    Třída pro sledování celkového času stráveného v aplikaci.
    Naměřená data ukládá do souboru data/time.txt v sekundách.
    """

    def __init__(self):
        # Zaznamenání času spuštění aplikace
        self.start_time = time.time()
        self.current_time = 0
        self.played_time = 0
        
        # Načtení dříve uloženého času ze souboru
        with open("data/time.txt", "r") as f:
            content = f.read().strip()
            self.played_time = int(content) if content else 0


    def end(self) -> None:
        """Vypočítá uplynulý čas od spuštění a přičte jej k celkovému uloženému času."""
        self.current_time = time.time()
        # Celkový čas = (současný čas - čas spuštění) + dříve odehraný čas
        total_seconds = int(self.current_time) - int(self.start_time) + int(self.played_time)

        with open("data/time.txt", "w") as f:
            f.write(str(total_seconds))

    @staticmethod
    def getPlayedTime() -> float:
        """Vrátí celkový odehraný čas převedený na hodiny (zaokrouhleno na 2 desetinná místa)."""
        try:
            with open("data/time.txt", "r") as f:
                content = f.read().strip()
                seconds = int(content) if content else 0
                return round(seconds / 3600, 2)
        except (FileNotFoundError, ValueError):
            return 0.0