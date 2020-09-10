import numpy as np

class Ray(object):
    def __init__(self, E=None, uCoord=None, vCoord=None,
                 PLANEDISTANCE=None, U=None, V=None, W=None):
        self.E = E
        self.U = U
        self.V = V
        self.W = W
        self.uCoord = uCoord
        self.vCoord = vCoord
        self.PLANEDISTANCE = PLANEDISTANCE
    def getE(self):
        return self.E
    def getUcoord(self):
        return self.uCoord
    def getVcoord(self):
        return self.vCoord
    def getD(self):
        return (((-(self.PLANEDISTANCE))*(self.W)) + ((self.uCoord)*(self.U))
                                                   + ((self.vCoord)*(self.V)))

class Sphere(object):

    def __init__(self, center=None, radius=None, color=None):
        self.center = center
        self.radius = radius
        self.color = None

    def getCenter():
        return self.center

    def getRadius():
        return self.radius

class Group(Sphere):

    def __init__(self, name=None):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

class Material(object):

    def __init__(self, value=0):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class Color(object):

    def __init__(self, value=0):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

class HitRecord(object):

    def __init__(self, value=0):
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
