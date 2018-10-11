'''
#######################################################################################################################################################################
#88888888ba  88888888ba    ,ad8888ba,          88 88888888888 ,ad8888ba, 888888888888                       db        88                                         
#88      "8b 88      "8b  d8"'    `"8b         88 88         d8"'    `"8b     88                           d88b       88                                         
#88      ,8P 88      ,8P d8'        `8b        88 88        d8'               88                          d8'`8b      88                                         
#88aaaaaa8P' 88aaaaaa8P' 88          88        88 88aaaaa   88                88                         d8'  `8b     88 ,adPPYYba, 8b,dPPYba, 88,dPYba,,adPYba, 
88""""""'   88""""88'   88          88        88 88"""""   88                88         aaaaaaaa       d8YaaaaY8b    88 ""     `Y8 88P'   "Y8 88P'   "88"    "8a
88          88    `8b   Y8,        ,8P        88 88        Y8,               88         """"""""      d8""""""""8b   88 ,adPPPPP88 88         88      88      88
88          88     `8b   Y8a.    .a8P 88,   ,d88 88         Y8a.    .a8P     88                      d8'        `8b  88 88,    ,88 88         88      88      88
88          88      `8b   `"Y8888Y"'   "Y8888P"  88888888888 `"Y8888Y"'      88                     d8'          `8b 88 `"8bbdP"Y8 88         88      88      88
#######################################################################################################################################################################
'''
#!/usr/bin/env python3
from datetime import datetime#Tímpádem už nemusím volat datetime.datetime.něco ale jen datetime.něco
from threading import Timer
import sys
import random
import time
import webbrowser
import re

regExpression = re.compile('^[0-9]{2}:[0-9]{2}:[0-9]{2}$')#Nevím přesně, proč je to takhle - Vstupní řetězec by měl mít tento formát
#Funkce, která počítá, jestli jsou hodiny v pořádku - že např uživatel nezvolí 66:66:878 hodin

# Jako parametr se vkládá seznam s uživatelsky zvolenýma hodinama, minutama a vteřinama spuštění
def inputCheck(timeList):

    isHourCorrect = 0 <= int(timeList[0]) <= 24
    isMinuteCorrect = 0 <= int(timeList[1]) <= 59
    isSecondCorrect = 0 <= int(timeList[2]) <= 59

    if isHourCorrect and isMinuteCorrect and isSecondCorrect:
        return True
    else:
        return False
#Hrozivá funkce, která spustí video
def IDontWantToLiveOnThisPlanetAnymore():
    listOfVideos = []
    file = open('horribleYoutubeVideos.txt','r') #Otevře soubor s odkazy YT videí pro čtení

#Projde celý soubor řádek po řádku a jednotlivé odkazy uloží do seznamu
    for line in file:
        listOfVideos.append(line)

    videoLink = random.choice(listOfVideos)#Náhodně vybere odkaz ze seznamu
    file.close() #zavře soubor
    webbrowser.open(videoLink)#Otevře browser s daným url
#Vypisuje do konzole odpočítávání
def countdownClass(remainingTime):
    while remainingTime > 0:
        print("Video will start in " + str(remainingTime) + "s")
        remainingTime -= 1
        time.sleep(1)
def UserInputValidator():
    # Vstup bude po uživateli požadován tak dlouho, dokud ho správně nezadá//Asi by se dal přepsat tak, aby funkce brala jen parametr a validovala input, takhle to ale prozatím stačí
    while True:
        try:
            userTime = input("Enter time in following format: hh:mm:ss ")
            isInputValid = regExpression.search(userTime)  # Nevím přesně, proč je to takhle - Pokud se uživatelský vstup rovná formátu řetězce

            if isInputValid:
                timeList = userTime.split(':')
                if inputCheck(timeList):
                    print("Input check succesfull :-)")
                    return timeList
                else:
                    print("Use this time format 0-24:0-59:0-59")

            else:
                print("The entered time doesn't match format")

        except:
            print("Unhandled exception")
def CalculateScriptShowTime(timeList):#Vypocte ze zadaneho uzivatelskeho vstupu cas spusteni a vrati countdown
    actualTime = datetime.now()  # do proměnné si uložím aktuální čas
    showTime = actualTime.replace(day=actualTime.day + 1, hour=int(timeList[0]), minute=int(timeList[1]),second=int(timeList[2]),microsecond=0)  # S pomocí uživatelských atributů nastaví čas spuštění, čas se musí nastavit na +1 den abych dostal 'aktuální' den
    delta_t = showTime - actualTime  # Rozdíl mezi těmito časy - např. když je aktuální čas 11:00 a naplánovaný čas 11:01, je tento rozdíl 0:00:59:999999
    countdown_s = delta_t.seconds + 1  # Převede časový rozdíl na sekundy
    return countdown_s
def userTimer(remainingTime):
    t = Timer(remainingTime, IDontWantToLiveOnThisPlanetAnymore)  # Ve správný čas spustí funkci
    t.start()
    countdownClass(remainingTime)


#Tady začíná program/měl bych ho nahradit main funkcí? - funkce, ve které je narvané úplně všechno
def Program():
    timeList = UserInputValidator()
    remainingTime = CalculateScriptShowTime(timeList)
    print(remainingTime)
    userTimer(remainingTime)
Program()





