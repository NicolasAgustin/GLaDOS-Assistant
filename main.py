#import library

import speech_recognition as sr
import pyttsx3
from threading import Thread 

from pydub import AudioSegment
from pydub.playback import play

import simpleaudio

import time

# Dependencias
#   pip install SpeechRecognition
#   pip install pyttsx3
#   pip install pydub
#   pip install simpleaudio

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
    
    return t

def who(tokens):
    if tokens[0] == "are":
        waveObj = simpleaudio.WaveObject.from_wave_file('Audio/who_are.wav')
        playObj = waveObj.play()
        return playObj

def sing():
    waveObj = simpleaudio.WaveObject.from_wave_file('Audio/want_you_gone.wav')
    playObj = waveObj.play()
    return playObj

def hi():
    waveObj = simpleaudio.WaveObject.from_wave_file('Audio/greet.wav')
    playObj = waveObj.play()
    return playObj
    
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
        # r = sr.Recognizer()
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[1].id)
        engine.setProperty('pitchshift', 5234)

        waveObj = simpleaudio.WaveObject.from_wave_file('Audio/glados_intro.wav')
        playObj = waveObj.play()
        playObj.wait_done()


        #song = AudioSegment.from_wav('Audio/glados_intro.wav')
        #play(song)
        waveObj = simpleaudio.WaveObject.from_wave_file('Audio/tell_me_your_name.wav')
        playObj = waveObj.play()
        playObj.wait_done()
        
        name = input("Name: ")
        
        
        waveObj = simpleaudio.WaveObject.from_wave_file('Audio/im_not_even_repeat_it.wav')
        playObj = waveObj.play()
        playObj.wait_done()
        
        engine.say(name)
        engine.runAndWait()
        
        t1 = None
        
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