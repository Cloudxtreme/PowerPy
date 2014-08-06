#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

#    Programmer -    Stephen Coman
#    Date       -    7/26/2014
#    Item       -    Applicaiton entery point

# Applicaiton Description

# Imported modules
#===============================================================================
from urllib.request import urlopen
import readline


class Powerball():
    def __init__(self,playDate,playOne, playTwo, playThree, playFour, playFive, powerBall):
        self.playDate  = playDate
        self.playOne   = playOne
        self.playTwo   = playTwo
        self.playThree = playThree
        self.playFour  = playFour
        self.playFive  = playFive
        self.powerBall = powerBall

    def set_date_powerball( playDate):
        self.playDate = playDate

    def set_play_picks(playOne, playTwo, playThree, playFour, playFive):
        self.playOne   = playOne
        self.playTwo   = playTwo
        self.playThree = playThree
        self.playFour  = playFour
        self.playFive  = playFive
        return setStatus

#    def verifiy_play_picks(playOne, playTwo, playThree, playFour, playFive):
        

    def set_power_pick(powerPlay):
        self.powerBall = powerBall
        
        return setStatus

    def get_play_picks(self):
        return self.playOne, self.playTwo, self.playThree, self.playFour, self.playFive

    def get_power_pick(self):
        return self.powerBall
    

class PBDatabase():
    def __init__(self):
        self.webSite = 'http://www.powerball.com/powerball/winnums-text.txt'
        self.get_DB_file(self.webSite)


    def get_DB_file(self, urlDB):
        winDB = urlopen(urlDB)
        localFile = open('winnums-text.txt', 'wb')
        data = winDB.read()
        localFile.write(data)
        localFile.close()
        winDB.close()
