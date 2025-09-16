text = input("Enter your Text:")
words = text.split()      
word_count = len(words)
if word_count >1:
    print("this exercise is quite easy!")
elif word_count == 1:
    print(text.upper())
else:
    print("none")