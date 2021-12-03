from DotsAndBoxes import *

integers = input("Please enter the length, width, and difficulty level(easy, medium, hard): ").split()
m = int(integers[0])
n = int(integers[1])
level = integers[2]
game = DotsAndBoxes(m, n, level)
game.playGame()