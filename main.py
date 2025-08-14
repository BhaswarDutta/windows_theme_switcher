from InquirerPy import inquirer
from pathlib import Path
import ctypes
import json5
import os
import json

# Theme selctor with nice TUI
# Gives Key name for Dictionaries from user choice
theme = inquirer.select(  # type: ignore
    message="🎨SELECT YOUR THEME",
    choices=["Catppuccin", "Synthwave '84", "Nord", "Everforest", "Gruvbox"],
).execute()


# realative paths of wallapapers in a dict
wall_dict = {
    "Catppuccin": "images/catppuccin.png",
    "Synthwave '84": "images/synthwave.png",
    "Nord": "images/nord.jpg",
    "Everforest": "images/everforest.png",
    "Gruvbox": "images/gruvbox.png",
}

# absolute path of selected wallapaper as a string
wallpaper = str(Path(wall_dict[theme]).resolve())

# change wallpaper
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper, 3)


# Dict with VSCode Theme names
vscode_theme_dict = {
    "Catppuccin": "Catppuccin Mocha",
    "Synthwave '84": "SynthWave '84",
    "Nord": "Nord",
    "Everforest": "Everforest Dark",
    "Gruvbox": "Gruvbox Dark Soft",
}


# returns path of settings.json for VSCode
def get_vscode_settings_path_windows() -> Path:
    appdata = Path(os.getenv("APPDATA", ""))
    path = appdata / "Code" / "User" / "settings.json"

    if path.exists():
        return path
    else:
        raise FileNotFoundError("VSCode stable settings.json not found.")


# changes theme of VSCode as per selected theme
settings_path = get_vscode_settings_path_windows()
new_theme = vscode_theme_dict[theme]
with open(settings_path, "r") as file:
    vscode_settings = json5.load(file)

# changes theme
vscode_settings["workbench.colorTheme"] = new_theme

# saves modified json
with open(settings_path, "w") as file:
    file.write(json.dumps(vscode_settings, indent=4))


windows_terminal_theme_dict = {
    "Catppuccin": "Catppuccin Mocha",
    "Synthwave '84": "SynthWave 84",
    "Nord": "Nord",
    "Everforest": "Everforest Dark Medium",
    "Gruvbox": "GruvboxDark",
}


def get_windows_terminal_settings_path_windows() -> Path:
    appdata = Path(os.getenv("LOCALAPPDATA", ""))
    path = (
        appdata
        / "Packages"
        / "Microsoft.WindowsTerminal_8wekyb3d8bbwe"
        / "LocalState"
        / "settings.json"
    )

    if path.exists():
        return path
    else:
        raise FileNotFoundError("Windows Terminal settings.json not found.")


# Load settings.json (with comments allowed)
settings_path = get_windows_terminal_settings_path_windows()
new_theme = windows_terminal_theme_dict[theme]

with open(settings_path, "r", encoding="utf-8") as file:
    terminal_settings = json5.load(file)

# Change default color scheme
terminal_settings["profiles"]["defaults"]["colorScheme"] = new_theme


# Save using standard JSON (keeps double quotes)
with open(settings_path, "w", encoding="utf-8") as file:
    json.dump(terminal_settings, file, indent=4)
