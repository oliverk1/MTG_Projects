# mtg-project
Various programs to help with sorting through Magic the Gathering cards.\n
Programs:\n
API-MTG-Autofill.py: My first experimentation with API and is used to get a list of names of all MTG cards, open a textbox\n
                     and autofill any text with MTG cards.\n
API-MTG-CardFinder(NOEXCHANGERATE).py: Further API experimentation with .json. Input a card name and this code returns the\n
                     price, release date and link to the card on the MTG Gatherer website.\n
API-MTG-AutofillDownloadCardAndInventory.py: Combination of Autofill and CardFinder. Textbox will autofill card name and\n
                     upon a button press append the card to "inventory.txt" and saves a png of the card including the price.\n
DeckCost(No)Download.py: Written to integrate inventory and deck collection files from https://www.moxfield.com/. Will return\n
                     the cost to build the deck and what cards are missing. Downloads a .png of the card with price in name.\n
mtg_text_img_identifier.py: Accesses the webcam to take a photo of a card. Compares image and text of card with .jpg of MTG\n
                     cards and returns the closest match to identify which card has been photographed.\n
