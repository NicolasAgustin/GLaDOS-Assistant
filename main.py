#import library

import speech_recognition as sr
import pyttsx3
import simpleaudio
import random
import time

from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime

# Dependencias
#   pip install SpeechRecognition
#   pip install pyttsx3
#   pip install pydub
#   pip install simpleaudio

class Reminder():
    def __init__(self, description, time):
        self.description = description
        self.time = time
    def start_daemon(self):
        # Aca va a iniciar el demonio para
        #  chequear cuando se cumpla el tiempo
        #  para un recordatorio
        pass


class User():
    def __init__(self):
        self.name = ""
        self.reminders = []
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getReminders(self):
        return self.reminders
    def addReminder(self, reminder):
        print("DEBUG: {} {}".format(reminder.description,reminder.time))
        self.reminders.append(reminder)

# Esto deberia estar en una clase que englobe todas las funciones
# Crear clase VoiceAssistant
songs = ['Audio/want_you_gone.wav', 'Audio/still_alive.wav']
engine = pyttsx3.init()
engine.setProperty("rate", 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('pitchshift', 5234)
user = User()
###################################################################

def tokenize(command):
    if not command == "":
        return command.split()
    return []

def evaluate(command):
    t = None
    tokens = tokenize(command)
    if tokens[0] == "sing":
        return sing()
    elif tokens[0] == "hi":
        return hi()
    elif tokens[0] == "who":
        return who(tokens[1:])
    elif tokens[0] == "set":
        return set(tokens[1:])

    return t


def make_audio_obj(file_name):
    waveObj = simpleaudio.WaveObject.from_wave_file(file_name)
    playObj = waveObj.play()
    return playObj


# Hacer una funcion para sumar fechas


def set(tokens):
    # El set reminder va a funcionar sumando n (dias, horas, minutos) a la fecha actual
    # luego de calcular ser va a iniciar el thread demonio
    phrase, target_time = "", ""
    if tokens[0] == "reminder":
        for word in tokens[1:]:
            phrase = "{} {}".format(phrase, word)
        target_time = phrase.split('for')[1]
        time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        user.addReminder(Reminder(phrase, time))
    return make_audio_obj('Audio/reminder.wav')

def who(tokens):
    if tokens[0] == "are":
        return make_audio_obj('Audio/who_are.wav')
    # Aca se van a seguir agregando comandos

def sing():
    pos = random.randint(1,10) % 2
    return make_audio_obj(songs[pos])

def hi():
    return make_audio_obj('Audio/greet.wav')

def main():
    try:
        print("              .,-:;//;:=,")
        print("          . :H@@@MM@M#H/.,+%;,")
        print("       ,/X+ +M@@M@MM%=,-%HMMM@X/,")
        print("     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-")
        print("    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.")
        print("  ,%MM@@MH ,@%=             .---=-=:=,.")
        print("  =@#@@@MX.,                -%HX$$%%%:;")
        print(" =-./@M@M$                   .;@MMMM@MM:")
        print(" X@/ -$MM/                    . +MM@@@M$")
        print(",@M@H: :@:                    . =X#@@@@-")
        print(",@@@MMX, .                    /H- ;@M@M=")
        print(".H@@@@M@+,                    %MM+..%#$.")
        print(" /MMMM@MMH/.                  XM@MH; =;")
        print("  /%+%$XHH@$=              , .H@@@@MX,")
        print("   .=--------.           -%H.,@@@@@MX,")
        print("   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.")
        print("     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=")
        print("       =%@M@M#@$-.=$@MM@@@M; %M%=")
        print("         ,:+$+-,/H#MMMMMMM@= =,")
        print("               =++%%%%+/:-.")
        print("")
        print("GLaDOS Genetic Lifeform and Disk Operating System v1.0")
        print("Starting... ", end="")
        time.sleep(1)
        print("Done")
        time.sleep(0.5)
        print("Loading test chambers... ", end="")
        time.sleep(1)
        print("Done")
        time.sleep(0.5)
        print("Waking up test subjects... ", end="")
        time.sleep(1)
        print("Done")
        time.sleep(0.5)
        print("Making cake... ", end="")
        time.sleep(1)
        print("Done")
        time.sleep(0.5)
        
        playObj = None
        t1 = None
        
        #playObj = make_audio_obj('Audio/glados_intro.wav')
        #playObj.wait_done()
        #playObj = make_audio_obj('Audio/tell_me_your_name.wav').wait_done()
        #playObj.wait_done()

        #waveObj = simpleaudio.WaveObject.from_wave_file('Audio/tell_me_your_name.wav')
        #playObj = waveObj.play()
        #playObj.wait_done()

        user.setName(input("Name: "))

        #playObj = make_audio_obj('Audio/im_not_even_repeat_it.wav').wait_done()
        #playObj.wait_done()
        
        #engine.say(user.getName())
        #engine.runAndWait()

        while True:
            cmd = input("GLaDOS $ ")
            if not t1 is None:
                t1.stop()
            audio = AudioSegment.from_wav('Audio/ok.wav')
            play(audio)
            #waveObj = simpleaudio.WaveObject.from_wave_file('Audio/ok.wav')
            #playObj = waveObj.play()
            #playObj.wait_done()

            t1 = evaluate(cmd)

    except KeyboardInterrupt:
        if not playObj is None:
            playObj.stop()
            song = AudioSegment.from_wav('Audio/goodbye.wav')
            play(song)

if __name__ == '__main__':
    main()


# # Reading Microphone as source
# # listening the speech and store in audio_text variable

# with sr.Microphone() as source:
#     print("Talk")
#     r.adjust_for_ambient_noise(source, duration = 1)
#     audio_text = r.listen(source)
#     print("Time over, thanks")

# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

#     try:
#         translation = r.recognize_google(audio_text)
#         # using google speech recognition
#         engine.say("I been really busy being dead")
#         # play the speech
#         engine.runAndWait()
#         print("Text: "+ translation)
#     except:
#          print("Sorry, I did not get that")
