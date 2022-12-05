# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new1 = name1.lower()
new2 = name2.lower()
T = (new1.count('t')+new2.count('t')+new2.count('r')+new1.count('r')+new1.count('u')+new2.count('u')+new1.count('e')+new2.count('e'))
L =(new1.count('l')+new2.count('l')+new2.count('o')+new1.count('o')+new1.count('v')+new2.count('v')+new1.count('e')+new2.count('e'))
score = int(str(T)+str(L))
if score<10 or score > 90:
    print(f"Your score is {score}, you go together  like coke and mentos")
elif score > 40 and score < 50:
    print(f" your score is {score}, you are alright together")
else:
    print(f"your score is {score}")


