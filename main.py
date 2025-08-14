from InquirerPy import inquirer

theme = inquirer.select(
    message="🎨SELECT YOUR THEME",
    choices=["Catpuccin", "Nord", "GruvBox", "Synthwave '84", "Everforest"],
).execute()

print(theme)
