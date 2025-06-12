# recognizer.py
import speech_recognition as sr

class Recognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize(self, audio_data):
        try:
            return self.recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print("Speech API unavailable:", e)
            return ""
