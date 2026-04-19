class EncodingManager:
    """
    Manažer šifrování využívající vlastní substituční tabulku (znakovou mapu).
    Zajišťuje převod hesla do nečitelné podoby a jeho následné dešifrování.
    """

    def __init__(self) -> None:
        # Mapa znaků pro substituci (vlastní algoritmus)
        self.algorithm = {
            'a': ',', 'á': '?', 'b': '<', 'c': '.', 'č': ':', 'd': '>', 'ď': '║', 'e': '_', 'ě': '*',
            'é': 'ů', 'f': '"', 'g': '$', 'h': '§', 'i': '!', 'í': 'ß', 'j': '¨', 'k': '¤', 'l': 'ú',
            'm': '/', 'n': '÷', 'ň': ')', 'o': '(', 'ó': '×', 'p': '´', 'q': 'ˇ', 'r': '¸', 'ř': '=',
            's': '%', 'š': '°', 't': '\\', 'ť': '|', 'u': '#', 'ú': '&', 'ů': '{', 'v': '}', 'w': 'đ',
            'x': 'Đ', 'y': '[', 'ý': ']', 'z': 'ł', 'ž': 'Ł', '1': '€', '2': '♂', '3': '↔', '4': '►',
            '5': '▓', '6': 'ö', '7': 'ę', '8': '├', '9': 'ő', ' ': '☻', ',': '☼', '.': '♥', ';': ';'
        }


    def encrypt(self, text: str) -> str:
        """Zašifruje vstupní text pomocí substituční mapy."""
        cypher = ''
        for letter in text:
            if (letter.isupper()):
                add = '-' # Označení pro velké písmeno
            else:
                add = ''

            cypher += add + self.algorithm[letter.lower()]

        return cypher

    def encryptList(self, list: list[str]) -> list:
        """Pomocná metoda pro zašifrování celého seznamu řetězců."""
        encryptedList = []
        for item in list:
            encryptedList.append(self.encrypt(item))

        return encryptedList

    def decrypt(self, cypher: str) -> str:
        """Převede zašifrovaný řetězec zpět na čitelný text."""
        text = ''
        upper = False
        for symbol in cypher:
            if (symbol == '-'):
                upper = True
                continue

            if (symbol == '\n'):
                break

            # Vyhledání klíče (původního znaku) podle hodnoty (šifry) v mapě
            letter = list(self.algorithm.keys())[list(self.algorithm.values()).index(symbol)]

            if (upper):
                letter = letter.upper()
                upper = False

            text += letter

        return text
