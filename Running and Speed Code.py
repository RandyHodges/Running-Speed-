miles = input("Enter miles ran: ")
speed = input("Enter how fast have you run: ")
mr = int(miles), float(miles)
sp = int(speed), float(speed)
if miles <= 40 :
    print("Great Job!")
elif miles <= 35 :
    print("Good work")
elif miles <= 25 :
    print("You Can do it")
elif miles <= 15 :
    print("Yaaaay you're on a start")
else:
    print("Let's Gooooooo!!!")
# Incentives for having a great speed
if speed < 5 :
    print("Wooow!!")
else:
    print("You keep it up")
