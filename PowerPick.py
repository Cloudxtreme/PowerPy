#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

#    Programmer -    Stephen Coman
#    Date       -    7/26/2014
#    Item       -    Applicaiton entery point

# Applicaiton Description

# Imported modules
#===============================================================================
from PPlib import *
import matplotlib.pyplot as plt

# Global values that can be accessed or adjusted as needed.
#===============================================================================
GlobalPPDBList = []

# Functions
#===============================================================================
def main():

    localDataBase = PBDatabase()
    ppDBFile = open('winnums-text.txt', 'r')
    
    for ppRecord in ppDBFile.readlines():
        if ppRecord != 'Draw Date   WB1 WB2 WB3 WB4 WB5 PB  PP' + '\n':
            rrList = ppRecord.split()
            ppDate = rrList[0]
            pbPP   = rrList[1:6]
            pbPP.sort()
            for index in range(0,5):
                pbPP[index] = int( pbPP[index])
            pbPB   = int(rrList[6])

            GlobalPPDBList.append( Powerball(ppDate, pbPP[0], pbPP[1], pbPP[2], pbPP[3], pbPP[4], pbPB))

        else:
            print('Hit -', ppRecord)

    ppDBFile.close()
    checkFrequency(59)

#def processPPDB():

def checkFrequency(dictRange):  # recommend 60
    dictRange = int(dictRange) + 1
    ppValues = dict()
    for dValue in range(1, dictRange):
        ppValues[dValue] = 0

    for index in GlobalPPDBList:
        picks = index.get_play_picks()
        for cycle in range(0,5):
            keyValue = picks[cycle]
            count = ppValues[keyValue]
            count = count + 1
            
            ppValues[keyValue] = count

    X = range(1, dictRange)        
    Y = []
    for dValue in range(1, dictRange):
#        print(dValue, ppValues[dValue])
        Y.append(ppValues[dValue])

    plt.figure(1)
    plt.subplot(211)
    plt.plot(X, Y)

    plt.subplot(212)
    plt.bar(range(len(X)), Y)
    plt.show()

"""
    plt.subplot(213)    
    plt.hist(Y, bins = 10)

    plt.subplot(214)
    plt.boxplot(Y)
"""    
    
       

# Main Program Execution Loop
#===============================================================================
main()
