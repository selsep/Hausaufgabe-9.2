# FizzBuzz

print("Wilkommen zum FizzBuzz-Spiel.")

print("Und so geht FizzBuzz: Gib eine Nummer zwischen 1 und 100 ein und schau was passiert.")

number = int(input("Meine Nummer zwischen 1 und 100 lautet: "))

for number in range(1,number + 1):
    if number % 3 is 0 and number % 5 is 0:
        print("FizzBuzz")
    elif number % 3 is 0:
        print("Fizz")
    elif number % 5 is 0:
        print("Buzz")
    else:
        print(number)





