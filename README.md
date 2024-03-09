
# DRPG Dialogue Extraction Tool

This code is designed to extract dialogue and text data from mobile games and organize it into an Excel spreadsheet or in Txts files. It includes translation capabilities using the Google Translate API.

# Dependencies

This code requires the following dependencies:

    deep_translator
    unitypy
    openpyxl
    json

# Usage

To start install all dependencies, inside terminal in this folder run:

    pip install -r requirements.txt

then change Game Master folder path (master_folder="") to where DMM store the data in file ./StoryFiles/unpack.py (normally you can just replace the your_username part)

    C:\\Users\\your_username\\AppData\\LocalLow\\disgaearpg\\DisgaeaRPG\\assetbundle\\masters\\

To use the code when the game updates open cmd in the project folder then:

    cd StoryFiles
    py unpack.py
    cd ..
    py excell.py

The terminal will inform which chapter is being added, wait for it to end. It will take a bit of time since it uses google endpoints to translate stuff.

You can find the resulting Excel spreadsheet in Sheets folder. Those will include columns for the original text, the translated text, and any additional metadata such as character names or episode titles.

If you want txt files use text.py (outdated) instead of excell.py
