import random
target=random.randint(0,10)
count=0
while True:
    try:
        count+=1  #Even if user enter something other than integer, count will still increase
        guess=eval(input("Please enter an integer:"))
        if guess>target:
            print("Too large.")
        elif guess<target:
            print("Too small.")
        else:
            print("You are right!")
            break
    except:
        print("Something went wrong. You wasted a guess!")
print("You totally have {} times of guesses.".format(count))
