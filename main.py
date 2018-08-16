# coding:utf-8

"""
See README.md ;)

I might have reinvented the wheel. idk I needed some training in string handling in python.

"""


class OOHOTH:

    def __init__(self, leftText, rightText):
        self.left = leftText
        self.right = rightText

    def generate(self, leftsize, rightsize):
        resultat = ""
        leftSplitter = Splitter(text=self.left, length=leftsize)
        rightSplitter = Splitter(text=self.right, length=rightsize)

        self.gauche = leftSplitter.decorate(leftSplitter.split())
        self.droite = rightSplitter.decorate(rightSplitter.split())

        while len(self.gauche) > len(self.droite):
            self.droite[len(self.droite)] = ''.join(" " for c in range(0, len(self.droite[0])))

        while len(self.gauche) < len(self.droite):
            self.gauche[len(self.gauche)] = ''.join(" " for c in range(0, len(self.gauche[0])))


    def print(self):
        for i in range(0, len(self.gauche)):
            print(self.gauche[i] + self.droite[i])

        print("¯\_(ツ)_/¯".center(len(self.gauche[0]) + len(self.droite[0]), " "))


class Splitter:
    text = ""
    length = 0

    def __init__(self, text, length):
        self.text = text
        self.length = length

    def split(self):
        resultat = {}
        position = 0

        lines_number = int(len(self.text) / self.length)

        for j in range(0, lines_number):
            resultat[j] = self.text[position: position + self.length]
            position += self.length

        if len(self.text) % self.length != 0:
            resultat[lines_number] = self.text[position: len(self.text)]

        return resultat

    def show(self, tableOfStrings):
        for i in range(0, len(tableOfStrings)):
            print(tableOfStrings[i])

    def decorate(self, tableOfStrings):
        lalinea = ''.join(chr(9473) for c in range(0, 10))
        deco = {}
        nb = (len(tableOfStrings[0]) + 2)
        lalinea = ''.join(chr(9473) for c in range(0, nb))
        deco[0] = str(chr(9487) + lalinea + chr(9491))
        for l in range(0, len(tableOfStrings)):
            deco[l + 1] = str(chr(9475) + ' ' + tableOfStrings[l].ljust(len(tableOfStrings[0])) + ' ' + chr(9475))

        deco[len(tableOfStrings) + 1] = str(chr(9495) + lalinea + chr(9499))
        return deco


ohohoh = OOHOTH("Many many people swore to protect country from inside enemies",
                "There is no 46 yet, despite everything that is taped")
ohohoh.generate(20, 20)
ohohoh.print()
