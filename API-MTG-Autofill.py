import requests
import sys
from PyQt5.QtWidgets import *

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

#def getCardInfo(card):
#    response = requests.get("https://api.scryfall.com/cards/named?fuzzy=wretched+throng")
#    print(response.status_code)
#    print(response.json())

namesList, namesListLower, namesListUpper = getCardNames()

dictionary = {}
dictionaryUpper = dict(zip(namesListUpper, namesList))
dictionaryLower = dict(zip(namesListLower, namesList))
dictionaryNormal = dict(zip(namesList, namesList))
dictionary.update(dictionaryUpper)
dictionary.update(dictionaryLower)
dictionary.update(dictionaryNormal)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        completer = QCompleter(dictionary)
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

