import pyttsx3

print("-------------------------------------------------------")
print("    Welcome to roboSpeaker 2.0 Created by Sabgeer")
print("-------------------------------------------------------")
print("\n")
print("Enter q to to stop :) ")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    x = input("Enter what you want me to speak :) ")
    if(x.lower() == "q"):
        a = "Bye my Friend "
        engine.say(a)
        engine.runAndWait()
        break
    engine.say(x) # Speak the text
    engine.runAndWait() # Wait untill the speaking is finished 