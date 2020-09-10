#import dependenices
import numpy as np
import math
from structures import Ray, Sphere

#define view plane height and width
NsubX = 20
NsubY = 15

#eye posistions in canconial frame
EYEXPOS = 0
EYEYPOS = 0
EYEZPOS = 0

# eye e, also known as the rays origin
E = np.array([EYEXPOS, EYEYPOS, EYEZPOS])

#canonical axes {U, V, W}
U = np.array([1, 0, 0])
V = np.array([0, 1, 0])
W = np.array([0, 0, 1])

#Plane distance, distance from E to view plane
PLANEDISTANCE = -1

#Light posistion
LIGHTXPOS = 4.0
LIGHTYPOS = 4.0
LIGHTZPOS = -8.0

#create light vector
L = np.array([LIGHTXPOS, LIGHTYPOS, LIGHTZPOS])

#define Plane bounds (unit)
tBOUND = 1.0
bBOUND = -1.0
lBOUND = -1.0
rBOUND = 1.0

#array of i,j coords; corresponding u, v coords (not the vectors)
IJArray = np.array([0, 0])
UVArray = np.array([0, 0])

#iterate over all points on view plane, perform arithmitc,
#create a list of U and V cords
for i in range(0, NsubX):
    for j in range(0, NsubY):
        currentCoordIJ = np.array([i, j])
        u = lBOUND + (rBOUND - lBOUND) * (i + 0.5)/(NsubX)
        v = bBOUND + (tBOUND - bBOUND) * (j + 0.5)/(NsubY)
        currentCoordUV = np.array([u, v])
        IJArray = np.vstack((IJArray, currentCoordIJ))
        UVArray = np.vstack((UVArray, currentCoordUV))

listOfUCoords = []
listOfVCoords = []
listhit = []

#alternate between ordering of u and v coords, add them to seperate lists
first = True
for item in UVArray.flat:
    if first is True:
        listOfUCoords.append(item)
        first = False
    else:
        listOfVCoords.append(item)
        first = True

#initialize count to zero, likewise w/ intersections
count = 0
numberIntersections = 0
#traverse over our array of uv coords
for x in np.nditer(UVArray):
    #as long as the count (current point) is less than the total points in scene
    if count < (NsubX * NsubY):
        #generate ray name
        rayName = ("Ray" + str(count))
        print("***RAY: " + rayName + "***")
        #determine current u and v coord
        uCoord = listOfUCoords[count]
        vCoord = listOfVCoords[count]
        #create ray object based on ray name, normals and other scene params
        rayName = Ray(E, uCoord, vCoord, PLANEDISTANCE, U, V, W)
        E = rayName.getE()
        uCoord = rayName.getUcoord()
        vCoord = rayName.getVcoord()
        D = rayName.getD()
        print("*E", E)
        print("*D", D)
        print("*uCoord", uCoord)
        print("*vCoord", vCoord)
        print("*PLANEDISTANCE", PLANEDISTANCE)
        print("*U", U)
        print("*V", V)
        print("*W", W)
        print("*SPHERE1")
        #defining center vector our first sphere here
        C = np.array([.65, 0.10, -1.25])
        print("*C", C)
        #and radius
        R = 0.3
        print("*R", R)
        #calculating our discrim to see if we need to record and calc hit/t
        discrim = (((D).dot(E-C))**2) - (D).dot(D)*((E-C).dot(E-C)-R**2)
        print("*Discrim", discrim)
        #no intersection: adds a blank
        if (discrim < 0):
            print("%NO INTERSECTION")
            listhit.append(" ")
        #intersection with 2 solutions, determine and find vectors for shading
        elif (discrim > 0):
            numberIntersections += 1
            print("#INTERSECTION (2 sol.)")
            tsub0 = ((-D).dot(E-C) + math.sqrt(discrim))/((D).dot(D))
            tsub1 = ((-D).dot(E-C) - math.sqrt(discrim))/((D).dot(D))
            print("First solution", tsub0)
            print("Second solution", tsub1)
            P1 = (E) + (tsub0) * (D)
            P2 = (E) + (tsub1) * (D)
            N = 2*(P1 - C)
            color = (1)*(5)*max(0, (N).dot(L))
            print("Shading Rep ", color)
            print("Possible point 1", P1)
            print("Possible point 2", P2)
            print("Surface normal at point is ", N)
            listhit.append("*")
        else:
            print("Grazed")
            listhit.append(".")
        print("*SPHERE2")
        C = np.array([.2, 0.50, -1.25])
        print("*C", C)
        print("*R", R)
        discrim = (((D).dot(E-C))**2) - (D).dot(D)*((E-C).dot(E-C)-R**2)
        print("*Discrim", discrim)
        if (discrim < 0):
            print("%NO INTERSECTION")
        elif (discrim > 0):
        #intersection with 2 solutions, determine and find vectors for shading
            numberIntersections += 1
            print("#INTERSECTION (2 sol.)")
            tsub0 = ((-D).dot(E-C) + math.sqrt(discrim))/((D).dot(D))
            tsub1 = ((-D).dot(E-C) - math.sqrt(discrim))/((D).dot(D))
            print("First solution", tsub0)
            print("Second solution", tsub1)
            P1 = (E) + (tsub0) * (D)
            P2 = (E) + (tsub1) * (D)
            N = 2*(P1 - C)
            color = (1)*(5)*max(0, (N).dot(L))
            print("Possible point 1", P1)
            print("Possible point 2", P2)
            print("Surface normal at point is ", N)
            print("Shading Rep ", color)
            if (listhit[count] != "*"):
                del listhit[count]
                listhit.insert(count, "x")
        else:
            print("Grazed")
        count += 1
    else: break
print("Number of intersections", numberIntersections)
listhitArray = np.asarray(listhit)
print(np.array_str(np.reshape(listhitArray, (NsubX, NsubY))))
#prints visual representation with np
