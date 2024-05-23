import math

def title_screen():
    print("Welcome to the High School Calculator!")
    print("-------------------------------------")

def instructions():
    print("Instructions:")
    print("1. Choose a calculation option from the menu.")
    print("2. Follow the prompts to input the values.")
    print("3. View the result.")
    print("4. Choose to perform another calculation or quit.")

def volume():
    print("\nVolume Calculations:")
    shape = input("Choose shape (cube, sphere, cylinder): ").lower()
    if shape == "cube":
        side = float(input("Enter side length: "))
        vol = side ** 3
        print("Volume of the cube is:", vol)
    elif shape == "sphere":
        radius = float(input("Enter radius: "))
        vol = (4/3) * math.pi * (radius ** 3)
        print("Volume of the sphere is:", vol)
    elif shape == "cylinder":
        radius = float(input("Enter radius: "))
        height = float(input("Enter height: "))
        vol = math.pi * (radius ** 2) * height
        print("Volume of the cylinder is:", vol)
    else:
        print("Invalid shape!")

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

def derivative():
    print("\nDerivative Calculation:")
    a = float(input("Enter coefficient (a): "))
    n = float(input("Enter exponent (n): "))
    x = float(input("Enter value of x: "))
    der = a * n * (x ** (n - 1))
    print("Derivative at x =", x, "is:", der)

def interest():
    print("\nInterest Calculation:")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate (%): "))
    time = float(input("Enter time (years): "))
    interest = (principal * rate * time) / 100
    print("Interest earned is:", interest)

def tax():
    print("\nTax Calculation:")
    income = float(input("Enter income: "))
    tax_rate = float(input("Enter tax rate (%): "))
    tax_amount = (income * tax_rate) / 100
    print("Tax amount is:", tax_amount)

def earnings():
    print("\nEarnings Calculation:")
    hours = float(input("Enter hours worked: "))
    wage = float(input("Enter hourly wage: "))
    earnings = hours * wage
    print("Total earnings are:", earnings)

def bmi():
    print("\nBMI Calculation:")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height ** 2)
    print("Your BMI is:", bmi)

def main():
    title_screen()
    while True:
        print("\nMenu:")
        print("1. Volume Calculation")
        print("2. Surface Area Calculation")
        print("3. Area Calculation")
        print("4. Derivative Calculation")
        print("5. Interest Calculation")
        print("6. Tax Calculation")
        print("7. Earnings Calculation")
        print("8. BMI Calculation")
        print("9. Instructions")
        print("10. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            volume()
        elif choice == "2":
            surface_area()
        elif choice == "3":
            area()
        elif choice == "4":
            derivative()
        elif choice == "5":
            interest()
        elif choice == "6":
            tax()
        elif choice == "7":
            earnings()
        elif choice == "8":
            bmi()
        elif choice == "9":
            instructions()
        elif choice == "10":
            print("Thanks for using the High School Calculator!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
