import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class Calculation:
    rollercoaster = [
        # Rollercoaster is brought up a steep incline by a lift
        # Flatline before the drop * /
        [2000, 0, 0],  # Drop and then decline to 326 degrees
        [3274, 300, -0.001],  # Flatline before into a loop
        [20226, 326, 0],  # Incline to 360/0 degrees
        [5500, 0, 0.1],  # Flatline before the incline to the loop
        [5000, 0, 0],  # Incline into the loop
        [5000, 0, 0.1],  # Loop 1
        [4623.999998, 593, 3000],  # Decline after the loop
        [2500, 345, 0.01],  # FlatLand after the loop
        [5000, 1, 0],  # Flatland incline into the next loop
        [2500, 1, 0.01],  # Loop 2
        [1225, 158, 3000],  # FlatLine decline
        [3000, 350, 0.01],  # Flatland flat
        [4200, 0, 0.01],  # Incline into the hill
        [7000, 25, 0.01],  # InclineHill into 0 degrees
        [950, 95, -0.1],  # InclineFlatLand
        [50, 0, 0],  # DeclineHillAngle change
        [200, 360, -0.1],  # DeclineHill distance
        [6800, 340, -0.001],  # Incline before a loop
        [3000, 333.2, 0.1],  # Loop 3
        [2450, 315, 3000],  # Decline after a Loop
        [3000, 330, 0.1],  # FlatLand Flat
        [1000, 345, 0.01],  # FlatLand into a incline for a Hill
        [500, 5, 0.1],  # FlatLandIncline
        [1000, 55, 0],  # FlatLandHilLDecline
        [5500, 55, -0.01],  # flatLandFlatLandInclineLoop
        [1500, 0, 0.01],  # Incline before the loop
        [1500, 15, 0.01],  # 4th Loop
        [735, 95, 3000],  # Loop4
        [1500, 345, 0.01],  # flatLandFlatLineDecline
        [1000, 0, 0.01],  # FlatLand1
        [1500, 10, 0.01]]  # FlatLand2

    mass = 3000
    gravity = 9.8
    fGravity = mass * gravity

    def calcNormalForceTrack(distance, angle, angleIncrementation):
        fNormal = []

        for i in range(distance):
            angle_rad = math.radians(angle)
            fNormal.append(math.cos(angle_rad) * (-Calculation.fGravity))
            angle += angleIncrementation

        return fNormal

    def calcNormalForceLoop(velocity, radius, mass):
        fNormal = []

        for i in range(radius):
            fNormal.append(((((mass * math.pow(velocity, 2)) /
                              radius) + Calculation.fGravity)))

        return fNormal

    def getNormalForce():
        fNormal = []
        for i in range(len(Calculation.rollercoaster)):
            fNormalTrack = Calculation.calcNormalForceTrack(
                Calculation.rollercoaster[i][0], Calculation.rollercoaster[i][1], Calculation.rollercoaster[i][2])
            fNormalLoop = Calculation.calcNormalForceLoop(
                Calculation.rollercoaster[i][0], Calculation.rollercoaster[i][1], Calculation.rollercoaster[i][2])
            fNormal.append(fNormalTrack)
            fNormal.append(fNormalLoop)
        return fNormal


def getFrictionForce(frictionCoefficient):
    fNormal = []
    fFriction = []
    for i in range(len(Calculation.rollercoaster)):
        fNormal.append(Calculation.getNormalForce())
        fFriction.append(Calculation.calcFrictionForce(
            fNormal, frictionCoefficient))

    return fFriction


# def getVelocity(distance):
# def getAirResistenece (vIntial, dragCoeff, dim1, dim2, mass, distance):

def main():

    cal = Calculation()

    fNormal = cal.getNormalForce()
    fFriction = cal.getFrictionForce()

    ax = plt

    ax.plot([fNormal], color="Blue")
    ax.plot([fFriction], color="Red")
    plt.show()


main()
