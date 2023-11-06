class EncodingManager:

    def __init__(self) -> None:
        self.algorithm = {
            'a': ',', 'á': '?', 'b': '<', 'c': '.', 'č': ':', 'd': '>', 'ď': '║', 'e': '_', 'ě': '*',
            'é': 'ů', 'f': '"', 'g': '$', 'h': '§', 'i': '!', 'í': 'ß', 'j': '¨', 'k': '¤', 'l': 'ú',
            'm': '/', 'n': '÷', 'ň': ')', 'o': '(', 'ó': '×', 'p': '´', 'q': 'ˇ', 'r': '¸', 'ř': '=',
            's': '%', 'š': '°', 't': '\\', 'ť': '|', 'u': '#', 'ú': '&', 'ů': '{', 'v': '}', 'w': 'đ',
            'x': 'Đ', 'y': '[', 'ý': ']', 'z': 'ł', 'ž': 'Ł', '1': '€', '2': '♂', '3': '↔', '4': '►',
            '5': '▓', '6': 'ö', '7': 'ę', '8': '├', '9': 'ő', ' ': '☻', ',': '☼', '.': '♥', ';': ';'
        }


    def encrypt(self, text: str) -> str:
        cypher = ''
        for letter in text:
            if (letter.isupper()):
                add = '-'
            else:
                add = ''

            cypher += add + self.algorithm[letter.lower()]

        return cypher

    def encryptList(self, list: list[str]) -> list:
        encryptedList = []
        for item in list:
            encryptedList.append(self.encrypt(item))

        return encryptedList

    def decrypt(self, cypher: str) -> str:
        text = ''
        upper = False
        for symbol in cypher:
            if (symbol == '-'):
                upper = True
                continue                
            
            if (symbol == '\n'):
                break

            letter = list(self.algorithm.keys())[list(self.algorithm.values()).index(symbol)]

            if (upper):
                letter = letter.upper()
                upper = False

            text += letter
        
        return text