import speech_recognition as sr
import webbrowser as wb
from os import path
from pydub import AudioSegment

def getInput(request):
        r1 = sr.Recognizer()
        r2 = sr.Recognizer()
        r3 = sr.Recognizer()
        mic = sr.Microphone(device_index=1)
        spokenSentence = ""
        check = 0
        with mic as source:
                while len(spokenSentence) == 0:
                        if check == 1:
                                print('Sorry, I didn\'t get that...')
                        print(request)
                        r1.adjust_for_ambient_noise(source)
                        audio = r1.record(source=mic, duration=2)
                        try:
                                check = 1
                                spokenSentence = r2.recognize_google(audio)
                        except:
                                print("Nothing said")
        return spokenSentence

def checkEmotion():
        goodEmotionArray = ["good", "not too bad", "great", "fine", "ok", "amazing", "excited", "happy", "positive", "fantastic"]
        badEmotionArray = ["bad", "terrible", "sick", "flu", "not", "sad"]
        spokenArray = spokenSentence.split()
        print(spokenSentence)
        check = False
        for s in range(len(spokenArray)):
                word = spokenArray[s]
                if (check == False):
                        if word in goodEmotionArray:
                                check = True
                                print("That's great!")
                        elif word in badEmotionArray:
                                check = True
                                print("Aww I'm sorry")
        if (check == False):
              print("Uuh ok lol")

def checkDateofBirth(spokenSentence):
        ageArray = ["1", "2", "3", "4", "5", "6,", "7,", "8,", "9,", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
        spokenArr = spokenSentence.split()
        check = False
        for s in range(len(spokenArr)):
                if spokenArr[s] in spokenArr:
                        if (check == False):
                                check = True
                                print('you were born in %s' % (2020 - int(spokenArr[s])))
        if (check == False):
              print("Please enter a valid age")

def checkAge():
        spokenSentence = getInput('How old are you?')
        print(spokenSentence)
        checkDateofBirth(spokenSentence)
def checkState():
        spokenSentence = getInput('How are you?')
        print(spokenSentence)
        checkEmotion(spokenSentence)
        


print('Hey!')
checkState()
checkAge()