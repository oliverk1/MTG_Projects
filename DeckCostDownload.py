import csv
import requests

def collection():
    collection = []
    collectionList = []
    with open("./collection.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            collection.append(row)
    for row in collection:
        collectionList.append(row[0] + " " + row[2])
    collectionList.remove("Count Name")
    collectionList = [i.split(" ", 1) for i in collectionList]
    return collectionList

def deck():
    file = open("./deck.txt", "r")
    deck = file.read()
    deckList = deck.split("\n")
    deckList = [i.split(" ", 1) for i in deckList]
    file.close()
    return deckList

def cardInCollection(collectionList, deckList):
    extraCardsOwned = []
    cardsMissing = []
    for row in deckList:
        for i in collectionList:
            numDeck = int(row[0])
            numOwned = int(i[0])
            if row[1] == i[1] and numDeck <= numOwned:
                extraCardsOwned.append(row)
                collectionList.remove(i)
                deckList.remove(row)
            elif row[1] == i[1] and numDeck > numOwned:
                print(numDeck,numOwned)
                cardsMissing.append([(numDeck - numOwned), row[1]])
                collectionList.remove(i)
                deckList.remove(row)
    for row in deckList:
        if row in collectionList:
            extraCardsOwned.append(row)
        else:
            cardsMissing.append(row)
    return cardsMissing

def getPrice(info,row):
    if 'prices' in info:
        prices = info['prices']
        priceNormal = str(prices['eur'])
        if priceNormal == "None":
            priceNormal = "NA"
        else:
            priceNormal = round((float(prices['eur'])*0.86326101), 2)
            priceNormal = float(priceNormal) * float(row[0])
    else:
        priceNormal = "NA"
    return priceNormal

def getCardInfo(cardsMissing):
    count = 0
    for row in cardsMissing:
        card = row[1]
        response = requests.get("https://api.scryfall.com/cards/named?fuzzy="+card)
        info = response.json()
        priceNormal = getPrice(info,row)
        name = str(row[0]) + "x" + " " + str(card) + " " + "£" + str(priceNormal) + ".png"
        name = name.replace("/","-")
        if 'image_uris' in info:
            img = info['image_uris']
            pngURL = img['png']
        else:
            img = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg/revision/latest?cb=20140813141013"
        img_data = requests.get(pngURL).content
        with open(name, 'wb') as handler:
            handler.write(img_data)
        cardsMissing[count].append(priceNormal)
        count = count + 1
    return cardsMissing


def userInfo(cardsMissing):
    total = 0
    for row in cardsMissing:
        print(str(row[0])+"x",str(row[1])+",","Cost: £"+str(row[2]))
        if str(row[2]) != "NA":
            total = total + float(row[2])
    print("\nTotal cost of missing cards: £"+str(round(total, 2)),
          "\nCards have been downloaded succesfully.")

cardsMissing = getCardInfo(cardInCollection(collection(), deck()))
userInfo(cardsMissing)
