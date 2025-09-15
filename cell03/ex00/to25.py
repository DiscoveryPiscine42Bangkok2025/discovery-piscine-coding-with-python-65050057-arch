num = int(input("Input your number:"))
if num < 25 :
    for num in range(num,26):
        print("Enter a number less than 25")
        print("Inside the loop, my variable is",num)         
else:
    print("Erorr")