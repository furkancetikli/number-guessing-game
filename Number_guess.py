import random
guess_time = 0

while True:
    while True:#Min ve maks Değerleri Alındı
        min = int(input("Enter the minimum value: "))
        maks = int(input("Enter the maximum value: "))

        if(maks < min):
            print("Attention! minimum value cannot be greater than maximum value! ")
        elif(min == maks):
            print("Attention minimum value cannot be equal to maximum value! ")
        else:
            break
    while True:#Guess Limit Alındı
        guess_time = 0
        guess_limit = int(input("Guess?: "))
        if guess_limit <=0:
            print("Attention! The prediction limit cannot be zero or less than zero! ")
        else:
            break
 
    number = random.randint(min,maks)  

    while True:
        if guess_time != guess_limit:
            guess = int(input(f"Guess between {min} and {maks}: "))

            if min < guess <maks:
                if guess > number:
                    print("Too High")
                    guess_time = guess_time+1
                elif guess < number:
                    print("Too Low")
                    guess_time = guess_time+1
                else :
                    print("Correct")
                    break
            else:
                print("Invalid Answer")
        else:
            print(f"Out of Luck The number was: {number}")
            break
    rematch = int(input("Wanna rematch? 0/1 "))
    if rematch == 0:
        break