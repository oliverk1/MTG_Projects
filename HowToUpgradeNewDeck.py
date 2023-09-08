def newdeck():
    file = open("newdeck.txt", "r")
    deck = file.read()
    collection = deck.split("\n")
    collection = [i.split(" ", 1) for i in collection]
    file.close()
    return collection

def olddeck():
    file = open("olddeck.txt", "r")
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
                cardsMissing.append([(numDeck - numOwned), row[1]])
                collectionList.remove(i)
                deckList.remove(row)
    for row in deckList:
        if row in collectionList:
            extraCardsOwned.append(row)
        else:
            cardsMissing.append(row)
    return cardsMissing

def userInfo(cardsMissing):
    for row in cardsMissing:
        print(str(row[0])+"x",row[1])

print("Cards taken out of deck:")
cardsMissing = cardInCollection(newdeck(), olddeck())
userInfo(cardsMissing)
print("\nCards to add:")
cardsMissing = cardInCollection(olddeck(), newdeck())
userInfo(cardsMissing)
