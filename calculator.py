import math

def display_title_screen():
    print("Welcome to the High School Calculator!")
    print("-------------------------------------")

def display_instructions():
    print("Instructions:")
    print("1. Choose a calculation option from the menu.")
    print("2. Follow the prompts to input necessary values.")
    print("3. View the result.")
    print("4. Choose whether to perform another calculation or quit.")

def calculate_volume():
    print("\nVolume Calculations:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        side = float(input("Enter the side length of the cube: "))
        volume = side ** 3
        print("Volume of the cube:", volume)
    elif choice == 2:
        radius = float(input("Enter the radius of the sphere: "))
        volume = (4/3) * math.pi * (radius ** 3)
        print("Volume of the sphere:", volume)
    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = math.pi * (radius ** 2) * height
        print("Volume of the cylinder:", volume)
    else:
        print("Invalid choice!")

def calculate_surface_area():
    print("\nSurface Area Calculations:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        side = float(input("Enter the side length of the cube: "))
        surface_area = 6 * (side ** 2)
        print("Surface area of the cube:", surface_area)
    elif choice == 2:
        radius = float(input("Enter the radius of the sphere: "))
        surface_area = 4 * math.pi * (radius ** 2)
        print("Surface area of the sphere:", surface_area)
    elif choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        surface_area = 2 * math.pi * radius * (radius + height)
        print("Surface area of the cylinder:", surface_area)
    else:
        print("Invalid choice!")

def calculate_area():
    print("\nArea Calculations:")
    print("1. Square")
    print("2. Triangle")
    print("3. Circle")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        print("Area of the square:", area)
    elif choice == 2:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area of the triangle:", area)
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * (radius ** 2)
        print("Area of the circle:", area)
    else:
        print("Invalid choice!")

# You can add more calculation functions here (derivatives, interest, tax, earnings)

def main():
    display_title_screen()
    while True:
        print("\nMain Menu:")
        print("1. Volume Calculations")
        print("2. Surface Area Calculations")
        print("3. Area Calculations")
        print("4. Instructions")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            calculate_volume()
        elif choice == 2:
            calculate_surface_area()
        elif choice == 3:
            calculate_area()
        elif choice == 4:
            display_instructions()
        elif choice == 5:
            print("Thank you for using the High School Calculator!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

