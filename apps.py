#!/usr/bin/env python3

import json
from difflib import get_close_matches
from playsound import playsound
from gtts import gTTS
from speech_recognition import Microphone, Recognizer


data = json.load(open("data.json"))


def speak0(text):
	tts = gTTS(text=text, lang="en")
	filename = 'name.mp3'
	tts.save(filename)
	playsound(filename)


speak0("Hello, type your name below: ")
name = input("Enter your name: ")



def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = 'giveCommands.mp3'
	tts.save(filename)
	playsound(filename)


speak(f"{name}, feed me the word to get its meanings: ")


def speak1(text):
	tts = gTTS(text=text, lang="en")
	filename = 'answers.mp3'
	tts.save(filename)
	playsound(filename)


def get_audio():
	r = Recognizer()
	playsound("giveCommands.mp3")

	with Microphone() as source:
	    audio = r.listen(source)
	    said = ""

	    try:
	        said = r.recognize_google(audio)
	        print(said)

	        if said == 'start notepad':
	            playsound('voice.mp3')
	            os.startfile('Notepad.lnk')

	        elif said == 'start recycle bin':
	            playsound('recycleBin.mp3')
	            os.startfile('Recycle Bin.lnk')

	        else:
	            playsound("voice1.mp3")

	    except Exception as e:
	        print("Exception: " + str(e))

	return said


get_audio()


def translate(w):
	w = w.lower()
	if w in data:
		return data[w]

	elif w.title() in data: # If user entered 'texas' this will check for 'Texas' as well.
		return data[w.title()]

	elif w.upper() in data:
		return data[w.upper()]

	elif len(get_close_matches(w, data.keys())) > 0:

		yn1 = print(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? ")


		yn = speak1(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? "
			f"Enter y if yes, or n if no: ")

		yn = input(f"Enter y if yes, or n if no: ")
		

		if yn == "y":
			return data[get_close_matches(w, data.keys())[0]]

		elif yn == 'n':
			speak1("The word doesn't exist. Please double check it.")
			return "The word doesn't exist. Please double check it."

		else:
			speak1(f"Sorry {name}, We didn't understand your entry")
			return f"Sorry {name}, We didn't understand your entry."


	else:
		speak1(f"Sorry {name}, the word doesn't exist in our dictionary.")
		return f"Sorry {name}, the word doesn't exist in our dictionary."


word = input('Enter any word to find its meaning: ')


output = translate(word)
a = (list(enumerate(output, start=1)))

if type(output) == list:
	for item in a:
		print(item)
		print()
	speak1(f"Feel free to use me anytime, {name}, Take care.")

else:
	print(output)


