from collections import deque
from Box import *


class Board:
    def __init__(self, _m, _n):
        self.playerScore = 0
        self.aiScore = 0
        self.m = _m
        self.n = _n
        self.boxes = self.generateBoxes(_m, _n)
        self.openVectors = self.generateVectors(_m, _n)
        self.connectedVectors = set()

        self.alpha = -100000
        self.beta = 100000

    def generateBoxes(self, m, n):
        cols = n
        rows = m
        boxes = [[Box(0, 0) for j in range(cols)] for i in range(rows)]
        for i in range(m):
            for j in range(n):
                boxes[i][j] = (Box(i, j))
        return boxes

    def generateVectors(self, m, n):
        vectors = deque()
        for i in range(0, m+1):
            for j in range(0, n):
                vectors.append(((j, i), (j + 1, i)))
                if i < m:
                    vectors.append(((j, i), (j, i + 1)))
            if i < m:
                vectors.append(((n, i), (n, i + 1)))
        return vectors

    def displayBoard(self):
        print("Player 1: %s" % self.playerScore)
        print("Player AI: %s" % self.aiScore)
        str1 = "\n  "
        for i in range(self.m + 1):
            str1 = str1 + "   %s" % i
        print(str1)

        boxVal = " "
        for i in range(self.m + 1):
            str1 = "%s " % i
            str2 = "     "
            for j in range(self.n + 1):
                if ((j - 1, i), (j, i)) in self.connectedVectors:
                    str1 = str1 + "---*"
                else:
                    str1 = str1 + "   *"

                if j < self.n:
                    if self.boxes[j][i - 1].TopLeft == (j, i - 1):
                        boxVal = self.boxes[j][i - 1].value
                else:
                    boxVal = " "

                if ((j, i - 1), (j, i)) in self.connectedVectors:
                    str2 = str2 + "| %s " % boxVal
                else:
                    str2 = str2 + "  %s " % boxVal
            print(str2)
            print(str1)
        print("")

    def move(self, coordinates, player):
        if player is True:
            player = 1
        elif player is False:
            player = 0
        if coordinates in self.openVectors:
            self.openVectors.remove(coordinates)
            self.connectedVectors.add(coordinates)
            self.checkBoxes(coordinates, player)
            return 0
        else:
            return -1

    def checkBoxes(self, coordinates, player):
        for i in range(self.m):
            for j in range(self.n):
                box = self.boxes[i][j]
                if coordinates in box.lines:
                    box.connectDot(coordinates)
                if box.complete is True and box.owner is None:
                    print(box.complete, box.owner is None)
                    box.owner = player
                    self.prevComplete = True
                    if player == 0:
                        self.playerScore += box.value
                    elif player == 1:
                        self.aiScore += box.value
