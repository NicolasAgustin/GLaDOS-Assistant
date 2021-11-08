#import library

import speech_recognition as sr
import pyttsx3
import simpleaudio
import random
import time
import datetime as dt
import traceback
import pickle
import sys, os

from threading import Thread
from pydub import AudioSegment
from pydub.playback import play
from datetime import datetime


# Dependencias
#   pip install SpeechRecognition
#   pip install pyttsx3
#   pip install pydub
#   pip install simpleaudio

# Funciones de proposito general #

def print_line(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
##################################

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
    def show(self):
        print('{} {}'.format(self.name, self.reminders))


class GLaDOS():
    def __init__(self):
        self.songs = ['want_you_gone.wav', 'still_alive.wav']
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.engineVoices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.engineVoices[1].id)
        self.engine.setProperty('pitchshift', 100)
        self.user = User()
        self.firstTime = 1
    
    def loadState(self):
        with open('logs/log.txt', 'a') as log:
            try:
                with open('bin/data', 'rb') as data:
                    self.firstTime = pickle.load(data)
                    self.user = pickle.load(data)
                    print('DEBUG: info recuperada del archivo de datos')
                    self.user.show()
                    print(str(self.firstTime))

                    data.close()
            except: 
                traceback.print_exc(file=log)
                log.close()
                pass
                

    def saveState(self):
        with open('logs/log.txt', 'a') as log:
            try:
                with open('bin/data', 'wb') as data:
                    pickle.dump(self.firstTime, data)
                    pickle.dump(self.user, data)
                    data.close()
            except:
                traceback.print_exc(file=log)
            finally:
                log.close()

    def tokenize(self, command):
        if not command == "":
            return command.split()
        return []

    def evaluate(self, command):
        t = None
        tokens = self.tokenize(command)
        if tokens[0] == "sing":
            return self.sing()
        elif tokens[0] == "hi":
            return self.hi()
        elif tokens[0] == "who":
            return self.who(tokens[1:])
        elif tokens[0] == "set":
            return self.set(tokens[1:])

        return t


    def make_audio_obj(self, file_name):
        file_name = 'Audio/{}'.format(file_name)
        waveObj = simpleaudio.WaveObject.from_wave_file(file_name)
        playObj = waveObj.play()
        return playObj

    # Hacer una funcion para sumar fechas
    def calculate_date(self, time_ammount):
        # Obtenemos la fecha y el tiempo actual
        date, time = datetime.now().strftime("%d/%m/%Y %H:%M:%S").split(' ')
        
        #Separamos en cantidad y unidad el target time
        n, unit = time_ammount.split(' ')
        n = int(n)
        unit = unit[0:len(unit)-1] if unit[len(unit)-1] == 's' else unit[0:len(unit)]

        #print('DEBUG: parsed info {} {}'.format, n, unit)
        
        day, month, year = date.split('/')
        hour, minute, second = time.split(':')
        day, month, year, hour, minute, second = int(day), int(month), int(year), int(hour), int(minute), int(second) 
        
        if unit == 'day':
            day = int(day) + n
        elif unit == 'month':
            month = int(month) + n
        elif unit == 'year':
            year = int(year) + n
        elif unit == 'hour':
            hour = int(hour) + n
        elif unit == 'minute':
            minute = int(minute) + n
        elif unit == 'second':
            second = int(second) + n

        calculated_date = dt.datetime(year, month, day, hour, minute, second).strftime("%d/%m/%Y %H:%M:%S")
        
        # print('DEBUG: {}'.format(calculated_date))

        return calculated_date

    def set(self, tokens):
        # El set reminder va a funcionar sumando n (dias, horas, minutos) a la fecha actual
        # luego de calcular ser va a iniciar el thread demonio
        try:
            phrase, target_time = "", ""
            if tokens[0] == "reminder":
                phrase_joined = ' '.join(tokens)
                phrase, target_time = phrase_joined.split('for')
                phrase = phrase.strip()
                target_time = target_time.strip()
                time = self.calculate_date(target_time)
                self.user.addReminder(Reminder(phrase, time))
            return self.make_audio_obj('reminder.wav')
        except:
            traceback.print_exc()
            return self.make_audio_obj('reminder_error.wav')

    def who(self, tokens):
        if tokens[0] == "are":
            return self.make_audio_obj('who_are.wav')
        # Aca se van a seguir agregando comandos

    def sing(self):
        pos = random.randint(1,10) % 2
        return self.make_audio_obj(self.songs[pos])

    def hi(self):
        return self.make_audio_obj('greet.wav')

    def run(self):
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
            print_line("Starting... ")
            # time.sleep(1)
            print("Done")
            # time.sleep(0.5)
            print_line("Loading test chambers... ")
            self.loadState()
            # time.sleep(1)
            print("Done")
            # time.sleep(0.5)
            print_line("Waking up test subjects... ")
            # time.sleep(1)
            print("Done")
            # time.sleep(0.5)
            print_line("Making cake... ")
            # time.sleep(1)
            print("Done")
            # time.sleep(0.5)
            
            playObj = None
            t1 = None
            
            if self.firstTime:
                playObj = self.make_audio_obj('glados_intro.wav')
                playObj.wait_done()
                playObj = self.make_audio_obj('tell_me_your_name.wav')
                playObj.wait_done()

                # waveObj = simpleaudio.WaveObject.from_wave_file('Audio/tell_me_your_name.wav')
                # playObj = waveObj.play()
                # playObj.wait_done()

                self.user.setName(input("Name: "))

                playObj = self.make_audio_obj('what_kind_of_name.wav')
                playObj.wait_done()

                self.firstTime = 0

            #self.engine.say(self.user.getName())
            #self.engine.runAndWait()

            while True:
                cmd = input("GLaDOS $ ")
                if not t1 is None:
                    t1.stop()
                audio = AudioSegment.from_wav('Audio/ok.wav')
                play(audio)
                #waveObj = simpleaudio.WaveObject.from_wave_file('Audio/ok.wav')
                #playObj = waveObj.play()
                #playObj.wait_done()

                t1 = self.evaluate(cmd)

        except KeyboardInterrupt:
            if not playObj is None:
                playObj.stop()
            self.saveState()
            song = AudioSegment.from_wav('Audio/goodbye.wav')
            play(song)



def main():
    glados = GLaDOS()
    glados.run()


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
