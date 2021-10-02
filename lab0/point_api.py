# MIT 6.034 Lab 0: Getting Started

from copy import deepcopy
import time

class Point(object):
    """A Point has x and y coordinates and a secret ID."""
    def __init__(self, x, y):
        self._x = x # Don't modify this directly! Use .setX() etc
        self._y = y
        # secret ID to differentiate between newly created Points and copies of an original
        self.ID = "_".join(map(str, [time.time(), x, y]))
        # True if this point was created using "Point(...)" or was copied from such a point
        self._constructed = True

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def setX(self, new_value):
        self._x = new_value
        return self

    def setY(self, new_value):
        self._y = new_value
        return self

    def copy(self):
        copy = deepcopy(self)
        copy.ID = "_".join(map(str, [time.time(), self._x, self._y]))
        return copy

    def coords_equal(self, other):
        try:
            return (self._x == other._x and self._y == other._y)
        except:
            return False

    def identical(self, other):
        try:
            return self.coords_equal(other) and self.ID == other.ID
        except:
            return False

    def __eq__(self, other):
        return self.coords_equal(other)

    def __str__(self):
        return "Point(%s, %s)" % (str(self._x), str(self._y))

    __repr__ = __str__
