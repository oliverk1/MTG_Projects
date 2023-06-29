import requests

def eur2gbp(eurPrice):
    gbpPrice = exchange * eurPrice
    gbpPrice = round(gbpPrice, 2)
    return gbpPrice

def getCardInfo(card):
    response = requests.get("https://api.scryfall.com/cards/named?fuzzy="+card)
    info = response.json()
    multiverseid = info['multiverse_ids']
    prices = info['prices']
    priceNormal = str(prices['eur'])
    pricefoil = str(prices['eur_foil'])
    if priceNormal == "None":
        priceNormal = "N/A"
    else:
        priceNormal = eur2gbp(float(prices['eur']))
    if pricefoil == "None":
        pricefoil = "N/A"
    else:
        pricefoil = eur2gbp(float(prices['eur_foil']))
    print("\nCard Name:", info['name'],
          "\nReleased:", info['released_at'],
          "\nPrices:", "£"+str(priceNormal)+",", "£"+str(pricefoil), "Foil",
          "\nURL: https://gatherer.wizards.com/Pages/Card/Details.aspx?multiverseid="+str(multiverseid[0]))

def ValidCard():
    while True:
        card = input("\nWhat is the name of the card? ")
        response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + card)
        if str(response) == "<Response [404]>":
            print("Invalid Card")
            continue
        else:
            break
    card = card.lower()
    card = card.replace(" ", "+")
    return card

def ValidRerun():
    while True:
        Rerun = input("\nWould you like to input another card? (Y/N) ")
        if Rerun == "Y" or Rerun == "y":
            return True
            break
        elif Rerun == "N" or Rerun == "n":
            return False
            break
        else:
            print("Please enter Y/N.")

def MainProgram():
    print("This program will search any Magic The Gathering card and return the release date,\nprice and URL of the card.")
    global exchange
    response = requests.get("http://data.fixer.io/api/latest?access_key=109e3c24b23fa0cdc7a32a8e0eaae2d5")
    exchange = response.json()
    exchange = exchange['rates']
    exchange = float(exchange['GBP'])
    while True:
        getCardInfo(ValidCard())
        if ValidRerun() == False:
            break

MainProgram()
