print("Welcome to the Hospital website")
n=input("What is your name? ")
print("Hello ", n)
choice = int(input("Enter your age: "))
if(choice <= 10  ):
    print(" You cannot book an appointment.")
if(choice >= 20):
    print("You cannot book an appointment.")
if(choice>=10 and choice<=20):
  t = input("When would you like to book an appointment? ")
  print("Your appointment is booked for ", t)