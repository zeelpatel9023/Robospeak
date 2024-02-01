

import win32com.client as wincom

if __name__ == "__main__":
    speak = wincom.Dispatch("SAPI.SpVoice")
    while True:
        text = input("enter what you want to me speak : ")
        if text == "Exit":
            speak.Speak("bye bye friend")
            break

        speak.Speak(text)