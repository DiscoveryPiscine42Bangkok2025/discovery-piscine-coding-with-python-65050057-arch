first_text = input("What you gotta say?")
print(first_text)
while True:
    Text = input("Enter your Text: ")
    if Text.lower() == "stop":  
        break
    print("I got that! Anything else?:", Text)
