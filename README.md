# Windows Theme Switcher

Inspired by [Omakub's](https://github.com/basecamp/omakub) Theme Switcher.

I really liked the idea of Omakub's Theme Switcher but didn't want to redo my Development Setup if I had to switch to Linux.

I need Windows for some specific apps but I also wanted the same feature.

Thus I wrote a python script for it.

Here's **Windows Theme Switcher**

## Features
- Clean CLI interface
- Changes Wallpaper based on Selected Theme
- Changes VSCode Theme based on Selected Theme
- Changes Windows Terminal Theme based on Selected Theme

## Themes Included
- Catppuccin (Mocha)
- Synthwave '84
- Nord
- Everforest
- Gruvbox
- *No light themes because I enjoy vision*

## Prerequisites
- Install the themes for VSCode
- Copy the settings.json for VSCode provided in the `configs` folder here
- Copy the settings.json for Windows Terminal provided in the `configs` folder here to install the themes for it
- Make sure needed extensions are installed for VSCode
- Make sure Powershell 7 is installed for Windows Terminal

## Steps
- Clone the repo or download and extract zip
- Install `uv` from [uv website](https://docs.astral.sh/uv/getting-started/installation/)
- Navigate to the folder and use `uv sync`
- Run the main file using `uv run main.py`
- Enjoy :D

### NOTES:
- This script might have bugs and problems as I tested it and use it only on my own machine, please feel free to report any bugs you find.
