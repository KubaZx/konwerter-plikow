import sys
import asyncio
from pathlib import Path
from utils.json_handler import load_json, save_json
from utils.yaml_handler import load_yaml, save_yaml
from utils.xml_handler import load_xml, save_xml

def detect_format(path):
    ext = Path(path).suffix.lower()
    if ext == '.json': return 'json'
    elif ext in ['.yml', '.yaml']: return 'yaml'
    elif ext == '.xml': return 'xml'
    else: raise ValueError("Nieobsługiwany format: " + ext)

async def async_main(input_file, output_file):
    input_fmt = detect_format(input_file)
    output_fmt = detect_format(output_file)

    loader = {'json': load_json, 'yaml': load_yaml, 'xml': load_xml}[input_fmt]
    saver = {'json': save_json, 'yaml': save_yaml, 'xml': save_xml}[output_fmt]

    try:
        data = await loader(input_file)
        await saver(data, output_file)
        print("Plik zapisany!")
    except Exception as e:
        print("Błąd:", e)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Brak argumentów – uruchom GUI
        import gui
        gui.uruchom_gui()
    elif len(sys.argv) == 3:
        # Są dwa argumenty – uruchom jako konwerter CLI
        asyncio.run(async_main(sys.argv[1], sys.argv[2]))
    else:
        print("Użycie: project.exe plik_wejściowy.xxx plik_wyjściowy.yyy")