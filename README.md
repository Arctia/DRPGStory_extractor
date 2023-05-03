
# DRPG Dialogue Extraction Tool

This code is designed to extract dialogue and text data from mobile games and organize it into an Excel spreadsheet or in Txts files. It includes translation capabilities using the Google Translate API.

# Dependencies

This code requires the following dependencies:

    deep_translator
    dataloader
    openpyxl
    json

# Usage

To use this code, simply run the DialogueExtractor class with the appropriate arguments. It will extract dialogue and text data from the mobile game and organize it into an Excel spreadsheet. To specify the language of the game and the output language, change the jp argument to True or False.

The resulting Excel spreadsheet will include columns for the original text, the translated text, and any additional metadata such as character names or episode titles.

If you want txt files use text.py instead
