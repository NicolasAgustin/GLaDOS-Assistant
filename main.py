#import library

import speech_recognition as sr
import pyttsx3
from threading import Thread 

from pydub import AudioSegment
from pydub.playback import play


def tokenize(command):
    if not command == "":
        return command.split()
    return []

def evaluate(command):
    t = Thread()
    tokens = tokenize(command)
    if tokens[0] == "sing":
        t = Thread(target=sing)
        t.start()
    elif tokens[0] == "hi":
        t = Thread(target=hi)
        t.start()
    return t

def sing():
    song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\want_you_gone.wav')
    play(song)

def hi():
    song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\greet.wav')
    play(song)

def main():
    try:
        # r = sr.Recognizer()
        engine = pyttsx3.init()
        engine.setProperty("rate", 130)

        voices = engine.getProperty('voices')
        print (voices)

        engine.setProperty('voice', voices[1].id)
        engine.setProperty('pitchshift', 5234)

        song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\glados_intro.wav')
        play(song)
        song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\tell_me_your_name.wav')
        play(song)
        name = input("Name: ")
        song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\im_not_even_repeat_it.wav')
        play(song)
        engine.say(name)
        engine.runAndWait()
        
        t1 = Thread()

        while True:
            cmd = input("GLaDOS $ ")
            song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\ok.wav')
            play(song)
            
            t1 = evaluate(cmd)
    except KeyboardInterrupt:
        song = AudioSegment.from_wav(r'GLaDOS_assistant\Audio\goodbye.wav')
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