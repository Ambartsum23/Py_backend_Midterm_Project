#კალკულატორი
import time

#კალკულატორის კლასი, რომელიც ინახავს ორ რიცხვს
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    #კონსტრუქტორი: ობიექტის შექმნისას ვინახავთ მომხმარებლის მიერ შეყვანილ 2 რიცხვს

    #ჯამი
    def add(self):
        return self.num1 + self.num2

    #სხვაობა
    def substract(self):
        return self.num1 - self.num2

    #გამრავლება
    def multiply(self):
        return self.num1 * self.num2

    #გაყოფა
    def divide(self):
        if self.num2 == 0:
            return "Error: Can't divide by zero."
        return self.num1 / self.num2


#მოცემული loop საშუალებას აძლევს მომხმარებელს, რამდენჯერმე გააკეთოს გამოთვლა

while True:
    print("\n--- Calculator ---")
    print("Enter 'exit' to exit")

    #პირველი რიცხვის მოთხოვნა
    first_number = input("Enter first number:\n")

    #თუ მომხმარებელი ჩაწერს exit, პროგრამა ასრულებს მუშაობას
    if first_number.lower() == "exit":
        print("Exiting...")
        time.sleep(1) #იცდის 1 წამი შემდეგ პრინტამდე
        print("Calculator is closed")
        break

    #მეორე რიცხვის მოთხოვნა
    second_number = input("Enter second number:\n")
    if second_number.lower() == "exit":
        print("Exiting...")
        time.sleep(1) #იცდის 1 წამი შემდეგ პრინტამდე
        print("Calculator is closed")
        break

    #ვალიდაცია: ინფუთს გარდავქმნით რიცხვად
    try:
        num1 = float(first_number)
        num2 = float(second_number)
    except ValueError:
        #თუ მომხმარებელი რიცხვის მაგივრად ტექსტს ჩაწერს, პროგრამა გამოიტანს შემდეგ შეტყობინებას
        print("Invalid input. Please try again.")
        continue #ლუპში თავიდან დაბრუნება

    #ვქმნით კალკულატორის ობიექტს და ვინახავთ ორ რიცხვს
    calc = Calculator(num1, num2)

    #სასურველი ოპერაციის არჩევა
    operation = input("Enter operation: +, -, *, /\n")

    #ვამოწმებთ მომხმარებლის მიერ არჩეულ ოპერაციას და ვასრულებთ შესაბამის მოქმედებას
    if operation == "+":
        print("Result: ", calc.add())
    elif operation == "-":
        print("Result: ", calc.substract())
    elif operation == "*":
        print("Result: ", calc.multiply())
    elif operation == "/":
        print("Result: ", calc.divide())
    else:
        #თუ სხვა რამეს ჩაწერს
        print("Invalid input. Please try again.")
