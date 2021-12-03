from random import randint


class Box:
    def __init__(self, _x, _y):
        self.coordinates = [(_x, _y), (_x + 1, _y), (_x, _y + 1), (_x + 1, _y + 1)]
        self.TopLeft = (_x, _y)
        self.TopLine = (self.coordinates[0], self.coordinates[1])
        self.RightLine = (self.coordinates[1], self.coordinates[3])
        self.BottomLine = (self.coordinates[2],  self.coordinates[3])
        self.LeftLine = (self.coordinates[0],  self.coordinates[2])
        self.lines = ([self.TopLine, self.RightLine, self.BottomLine, self.LeftLine])
        self.top = False
        self.right = False
        self.bottom = False
        self.left = False
        self.owner = None
        self.complete = False
        self.value = randint(1, 5)

    def connectDot(self, coordinates):
        line = coordinates
        success = False
        if line in self.lines:
            if line == self.TopLine and self.top is False:
                self.top = True
                success = True
            elif line == self.RightLine and self.right is False:
                self.right = True
                success = True
            elif line == self.BottomLine and self.bottom is False:
                self.bottom = True
                success = True
            elif line == self.LeftLine and self.left is False:
                self.left = True
                success = True
        if self.top is True and self.right is True and self.bottom is True and self.left is True:
            self.complete = True
        return success
