# Simplay — Herní Launcher a Organizátor

Simplay je funkční herní launcher vytvořený v Pythonu, který slouží k centralizaci her a sledování herního času.

## 🚀 Klíčové Vlastnosti
- **Centralizovaná Knihovna:** Možnost přidávat vlastní hry (.exe, .py) a spouštět je přímo z aplikace.
- **Organizace:** Třídění her do vlastních kategorií pro lepší přehled.
- **Zabezpečení:** Vlastní implementace šifrování přístupového hesla pomocí substituční znakové mapy.
- **Statistiky:** Automatické měření času stráveného v aplikaci a jeho ukládání pro budoucí přehled.
- **Custom UI:** Bezrámové okno s vlastním designem a podporou přesouvání (dragging).

## 🛠 Technologický Stack
- **Jazyk:** Python 3.x
- **GUI:** PyQt5 / QtPy (Framework pro moderní desktopová rozhraní)
- **Data:** XML (lxml) pro perzistentní ukládání her a kategorií
- **Zabezpečení:** Vlastní algoritmus pro kódování citlivých dat

## ⚙️ Instalace a Spuštění

Pro spuštění aplikace je potřeba mít nainstalovaný Python a následující knihovny:

1. **Instalace závislostí:**
   ```bash
   pip install qtpy PyQt5 lxml
   ```

2. **Spuštění aplikace:**
   ```bash
   python src/main.py
   ```

## 👥 Autoři
- Tomáš Klose
- Lukáš Hajnyš