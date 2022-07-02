import pyttsx3
import wikipedia

engine = pyttsx3.init()

#voices
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


def talk_function(text):
	engine.say(text)
	engine.runAndWait()


while True:
	user_input = input("User: ")
	user_input = user_input.lower()

	if user_input == "hello":
		talk_function("hey, hello");

	elif user_input == "how are you":
		talk_function("Iam fine Thank You,");

	elif user_input == "what is your name":
		talk_function("my name is DD");

	elif user_input == "your favourite colour":
		talk_function("my favourite colour is black");

	elif user_input == "how old are you":
		talk_function("Iam 780,");

	elif user_input == "how can you speak":
		talk_function("I have been programmed to talk,");

	elif user_input == "what are your hobbies":
		talk_function("reading books, researching, designing,");

	elif user_input == "what is your favourite book":
		talk_function("the eve, damian, feyre, ");

	elif user_input == "where do you live":
		talk_function("i live in batticaloa");

	elif user_input == "do you have friends":
		talk_function("yes, i have many friends");

	elif user_input == "how is your day":
		talk_function("so far its good");

	elif user_input == "can you please open whatsapp":
		talk_function("yes,please wait");

	elif user_input == "what is my schedule today":
		talk_function("your schedule for today is to going to your classes");

	elif "who" in user_input:
		data = wikipedia.summary(user_input)
		print(data)
		talk_function(data)

	elif "what" in user_input:
		data = wikipedia.summary(user_input)
		print(data)
		talk_function(data)

	else: 
		talk_function("i dont understand");


