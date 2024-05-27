def main():
    title_screen()
    while True:
        print("\nMenu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divide")
        print("5. Area Calculation")
        print("6. Surface Area Calculation")
        print("7. Interest Calculation")
        print("8. BMI Calculation")
        print("9. Instructions")
        print("10. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            Addition()
        elif choice == "2":
            Subtraction()
        elif choice == "3":
            Multiplication()
        elif choice == "4":
            Divide()
        elif choice == "5":
            area()
        elif choice == "6":
            surface_area()
        elif choice == "7":
            interest()
        elif choice == "8":
            bmi()
        elif choice == "9":
            instructions()
        elif choice == "10":
            print("Thanks for using the Blyat69 Calculator!")
            break
        else:
            print("Invalid choice! Try again.")

def instructions():
    print("Instructions:")
    print("1. Choose a calculation option from the menu.")
    print("2. Follow the prompts to input the values.")
    print("3. View the result.")
    print("4. Choose to perform another calculation or quit.")

def title_screen():
    print("Welcome to Blyat69's Calculator!")
    print("-------------------------------------")
            

def Addition():
    print("\nAddition Calculations:")
    num1=float (input("Number #1: "))
    num2=float (input("Number #2: "))
    sum = float(num1) + float(num2)
    print(num1, "+", num2, "=", (sum))

def Subtraction():
    print("\nSubtractiom Calculations:")
    num1=float (input("Number #1: "))
    num2=float (input("Number #2: "))
    sum = float(num1) - float(num2)
    print(num1, "-", num2, "=",(sum))



def Multiplication():
    print("\nMultiplication Calculations:")
    num1=float (input("Number #1: "))
    num2=float (input("Number #2: "))
    sum = float(num1) * float(num2)
    print(num1, "*", num2, "=", (sum))

    
    
    
def Divide():
    print("\nDivide Calculations:")
    num1=float (input("Number #1: "))
    num2=float (input("Number #2: "))
    sum = float(num1) / float(num2)
    print(num1, "/", num2, "=", (sum))




def surface_area():
    print("\nSurface Area Calculations:")
    shape = input("Choose shape (cube, sphere, cylinder): ").lower()
    if shape == "cube":
        side = float(input("Enter side length: "))
        sa = 6 * (side ** 2)
        print("Surface area of the cube is:", sa)
    elif shape == "sphere":
        radius = float(input("Enter radius: "))
        sa = 4 * math.pi * (radius ** 2)
        print("Surface area of the sphere is:", sa)
    elif shape == "cylinder":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        sa = 2 * math.pi * radius * (radius + height)
        print("Surface area of the cylinder is:", sa)
    else:
        print("Invalid shape!")

def area():
    print("\nArea Calculations:")
    shape = input("Choose shape (square, triangle, circle): ").lower()
    if shape == "square":
        side = float(input("Enter side length: "))
        a = side ** 2
        print("Area of the square is:", a)
    elif shape == "triangle":
        base = float(input("Enter base length: "))
        height = float(input("Enter height: "))
        a = 0.5 * base * height
        print("Area of the triangle is:", a)
    elif shape == "circle":
        radius = float(input("Enter radius: "))
        a = math.pi * (radius ** 2)
        print("Area of the circle is:", a)
    else:
        print("Invalid shape!")



def interest():
    print("\nInterest Calculation:")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate (%): "))
    time = float(input("Enter time (years): "))
    interest = (principal * rate * time) / 100
    print("Interest earned is:", interest)





def bmi():
    print("\nBMI Calculation:")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", bmi)


if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               


