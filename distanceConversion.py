#!/usr/local/env python3
# distanceConversion.py
# George Karrys
# one mile = 1.609 kilometers

from sys import exit
import miles
import kilometers

# validValue variable used in both functions
validValue = True


def mainConversion():
    """ Main function to convert between miles and kilometers"""
    # continueProgram variable only needed inside main function
    continueProgram = True

    while continueProgram:
        distance = float(
            input("Please enter a distance value to be converted: "))
        conversion = str.upper(
            input("Please enter the unit of length, M for miles or KM for Kilometers: "))
        if conversion == "M":
            convertedDistance = kilometers.convertToKilometers(distance)
            print("The distance of " + str(distance) + " miles is equivalent to " +
                  str(round((convertedDistance), 3)) + " kilometers.")
            newConversion()
        elif conversion == "KM":
            convertedDistance = miles.convertToMiles(distance)
            print("The distance of " + str(distance) + " kilometers is equivalent to " +
                  str(round((convertedDistance), 3)) + " miles.")
            newConversion()
        else:
            validValue = False
            print("This is not a valid imput!")
            exit()


def newConversion():
    ''' Function to allow user to continue with conversions'''
    newConversion = " "
    if validValue is True:
        newConversion = str.upper(
            input("Press X to quit or enter to continue: "))
        if newConversion == "X":
            exit()
        elif newConversion == "":
            mainConversion()
        else:
            print("This is not a valid imput")
            exit()


mainConversion()
