import time

import speech_recognition as sr # type: ignore
import os
import playsound # type: ignore
import shutil

shutil.rmtree("D:\spoken")
os.mkdir("D:\spoken")

speeches = []


def callback(recognizer, audio):
    with open("D:\spoken" + str(len(speeches)) + ".wav", "wb") as file:
        file.write(audio.get_wav_data())

    playsound.playsound("D:\spoken" + str(len(speeches)) + ".wav")
    speeches.append(1)
    print("____")


r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)
print("Please say a word here:")
while True:
    time.sleep(0.1)
