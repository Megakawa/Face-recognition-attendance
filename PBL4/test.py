import pyttsx3
import time
engine = pyttsx3.init()
voices = engine.getProperty("voices")

lb = "102190356"

vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
engine.setProperty("voice",vi_voice_id)
engine.say(lb)
engine.runAndWait()