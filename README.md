# Simplay

Jednoduchý herní launcher programovaný v Pythonu

## Funkce
- Zabezpečení přístupu
- Organizace her do kategorií
- Možnost přidání vlastních her
- Každá hra se otvírá v zvláštním okně
- Měření odehraného času


## Návod
### Instalace
Pro instalaci je třeba nainstalovat některé externí balíčky:
- PyQt5
  ~~~
  pip install PyQt5
  ~~~
- PySide2
  ~~~
  pip install PySide2
  ~~~
- PySide6
  ~~~
  pip install PySide6
  ~~~
- qtpy
  ~~~
  pip install qtpy
  ~~~
- CustomWidgets
  - pro instalaci této knihovny do os windows je potřeba doinstalovat knihovnu pipwin
    ~~~
    pip install pipwin
    ~~~
    - z této knihovny následně nainstalujeme cairocffi
      ~~~
      pipwin install cairocffi
      ~~~
  - poté nainstalujeme samotné CustomWidgets
    ~~~
    pip install QT-PyQt-PySide-Custom-Widgets
    ~~~
  - a pro jistotu upgradujeme na nejnovější verzi
    ~~~
    pip install --upgrade QT-PyQt-PySide-Custom-Widgets
    ~~~

### Zabezpečení přístupu
Pokud si přejete zaheslovat aplikaci proti neoprávněnému užívání, lze toho docílit pomocí následujících kroků:

1. Přejděte do záložky **Zabezpečení** vlevo dole
2. Zadejte heslo a klikněte na **Nastavit**
3. Následně budete přesměrováni na domovskou stránku. To značí, že se nastavení hesla povedlo a při dalším spuštění bude program vyžadovat nastavené heslo

*Nastavené heslo je šifrované pomocí našeho algoritmu a nelze ho tedy tak jednoduše prolomit.*

### Přidání vlastní hry
Do našeho launcheru lze, kromě již přidaných her, přidávat hry vlastní. Je však třeba dodržet požadovaný typ spustitelného souboru: soubor musí být ve formátu *.exe*, nebo *.py*

1. Klikněte na tlačítko **Přidat hru** v hlavním okně nahoře
2. Otevře se dialogové okno, ve kterém najdete hru, kterou chcete přidat
3. Potvrďte tlačítkem **Otevřít** a hra bude přidána

Pro následné spuštění hry stačí kliknout na tlačítko spustit u dané hry.


## Autoři
- Tomáš Klose
     - Zabezpečení přístupu
     - Přidávání her
     - Spouštění her

- Lukáš Hajnyš
     - Měření odehraného času
     - Defaultní hry
     - Vytváření kategorií
