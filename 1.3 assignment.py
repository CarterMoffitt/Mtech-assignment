def main():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

def celciusby():
    nums = [0,10,20,30,40,50,60,70,80,90,100]
    print(nums)
    for index, num in enumerate(nums):
        fahrenheit = 9/5 * num + 32
        print("Celsius: " + str(nums[index]) + " Fahrenheit: " + str(fahrenheit))

celciusby()

def main():
    for i in range(1):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

def kilo():
    for i in range(1):
        mile = eval(input("How many miles are you traveling? "))
        kilo = 1.60934 * mile
        print("You will travel", kilo, "kilometers if you travel", mile, "miles.")

kilo()

def length():
    print("this program calculates the future value")
    print("of an investment time period of your choice.")

    time = eval(input("Enter the length of time: "))
    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(time):
        principal = principal * (1 +apr)

    print("the value in", time, "years is", principal)

length()_