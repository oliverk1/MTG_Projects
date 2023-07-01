import requests
import sys
from PyQt5.QtWidgets import *

def eur2gbp(eurPrice):
    exchange = 0.86326101
    gbpPrice = exchange * eurPrice
    gbpPrice = round(gbpPrice, 2)
    return gbpPrice

def getCardInfo(card):
    cardA = card.lower()
    cardA = cardA.replace(" ", "+")
    response = requests.get("https://api.scryfall.com/cards/named?fuzzy=" + cardA)
    info = response.json()
    prices = info['prices']
    priceNormal = str(prices['eur'])
    if priceNormal == "None":
        priceNormal = "NA"
    else:
        priceNormal = round((float(prices['eur']) * 0.86326101), 2)
    fileName = str(card) + " " + "£" + str(priceNormal) + ".png"
    fileName = fileName.replace("/", "-")
    img = info['image_uris']
    pngURL = img['png']
    img_data = requests.get(pngURL).content
    with open(fileName, 'wb') as handler:
        handler.write(img_data)
    f = open("inventory.txt", "a")
    f.close()
    f = open("inventory.txt", "r")
    lines = f.readlines()
    f.close()
    f = open("inventory.txt", "r")
    inventory = f.read()
    inventoryList = inventory.split("\n")
    inventoryList = [i.split(" ", 1) for i in inventoryList]
    f.close()
    replace = 0
    count = 0
    for i in range (len(inventoryList) - 1):
        if card == inventoryList[i][1]:
            num = int(inventoryList[i][0])+1
            lines[int(count)] = str(num)+" "+str(card)+"\n"
            replace = 1
        count = count + 1
    if replace == 1:
        with open('inventory.txt', 'w') as f:
            for row in lines:
                f.write(row)
    else:
        f = open ("inventory.txt", "a")
        f.write("1 "+str(card)+"\n")
        f.close()

def getCardNames():
    responseList = requests.get("https://api.scryfall.com/catalog/card-names")
    cardNames = responseList.json()
    namesList = cardNames['data']
    namesListLower = []
    namesListUpper = []
    for names in namesList:
        namesListLower.append(names.lower())
    for names in namesList:
       namesListUpper.append(names.upper())
    return namesList, namesListLower, namesListUpper

namesList, namesListLower, namesListUpper = getCardNames()

dictionary = {}
dictionaryUpper = dict(zip(namesListUpper, namesList))
dictionaryLower = dict(zip(namesListLower, namesList))
dictionaryNormal = dict(zip(namesList, namesList))
dictionary.update(dictionaryUpper)
dictionary.update(dictionaryLower)
dictionary.update(dictionaryNormal)

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        QWidget.__init__(self)
        completer = QCompleter(dictionary)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)

        self.pb = QPushButton()
        self.pb.setObjectName("connect")
        self.pb.setText("Done")
        self.pb.clicked.connect(self.button_click)

        layout = QFormLayout()
        layout.addWidget(self.lineedit)
        layout.addWidget(self.pb)
        self.setLayout(layout)

        self.setWindowTitle("MTG Card")

    def button_click(self):
        shost = self.lineedit.text()
        getCardInfo(dictionary[shost])
        self.lineedit.setText("")


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
