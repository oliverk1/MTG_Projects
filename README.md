# mtg-project
Various programs to help with sorting through Magic the Gathering cards.
Programs:
API-MTG-Autofill.py: My first experimentation with API and is used to get a list of names of all MTG cards, open a textbox
                     and autofill any text with MTG cards.
API-MTG-CardFinder(NOEXCHANGERATE).py: Further API experimentation with .json. Input a card name and this code returns the
                     price, release date and link to the card on the MTG Gatherer website.
API-MTG-AutofillDownloadCardAndInventory.py: Combination of Autofill and CardFinder. Textbox will autofill card name and
                     upon a button press append the card to "inventory.txt" and saves a png of the card including the price.
DeckCost(No)Download.py: Written to integrate inventory and deck collection files from https://www.moxfield.com/. Will return
                     the cost to build the deck and what cards are missing. Downloads a .png of the card with price in name.
mtg_text_img_identifier.py: Accesses the webcam to take a photo of a card. Compares image and text of card with .jpg of MTG
                     cards and returns the closest match to identify which card has been photographed.
