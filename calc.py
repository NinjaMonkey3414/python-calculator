import time
import cmath
import math

def math_tool():
 try:
  num1 = float(input("1st number: "))
  num2 = float(input("2nd number: "))
  print(" ")
  print("Loading...")
  print(" ")
  time.sleep(3)
  print("Doing some very intense calculations...")
  print(" ")
  time.sleep(2)
  print("Done!")
  time.sleep(0.5)
 except ValueError:
    print("----- Please enter a number (any number) -----")
    return
 print("\n" + "=" * 30)
 print("----- Basic Arithmetic -----")
 print("=" * 30)
 print("\n")
 print(f"Addition: {num1 + num2}")
 print("-----")
 print(f"Subtraction ({num1} - {num2}): {num1 - num2}")
 print("-----")
 print(f"Subtraction ({num2} - {num1}): {num2 - num1}")
 print("-----")
 print(f"Multiplication: {num1 * num2}")
 print("-----")
 if num2 != 0:
    print(f"Division ({num1} / {num2}): {num1 / num2}")
 else:
    print("you can't divide by 0")
 print("-----")
 if num1 != 0:
    print(f"Division ({num2} / {num1}): {num2 / num1}")
 else:
    print("you can't divide by 0")
 print("\n" + "=" * 30)
 print("----- Algebra -----")
 print("=" * 30)
 print("\n")
 print(f"Square {num1}: {num1 ** 2}")
 print("-----")
 print(f"Square {num2}: {num2 ** 2}")
 print("-----")
 print(f"{num1} to the power of {num2}: {num1 ** num2}")
 print("-----")
 print(f"{num2} to the power of {num1}: {num2 ** num1}")
 print("-----")
 print(f"Cube {num1}: {num1 ** 3}")
 print("-----")
 print(f"Cube {num2}: {num2 ** 3}")
 print("-----")
 if num1 >= 0:
    print(f"Square root number 1: {math.sqrt(num1)}")
 else:
    print(f"Square root number 1: {cmath.sqrt(num1)}")
 print("-----")
 if num2 >=0:         
    print(f"Square root number 2: {math.sqrt(num2)}")
 else:
    print(f"Square root number 2: {cmath.sqrt(num2)}")
 print("\n" + "=" * 30)
 print("----- Geometry -----")
 print("=" * 30)
 print("\n")
 print("---- Square ----")
 if num1 >= 0:
    print(f"Area of a Square for {num1}: {num1 ** 2} ")
    print("-----")
    print(f"Perimeter of a square for {num1}: {num1 * 4}")
    print("-----")
    print(f"Diagonal of a square for {num1}: {math.sqrt(2) * num1}")
 else:
    print("!! YOU CANT HAVE NEGATIVE LENGTH !!")
 if num2 >= 0:
    print(f"Area of a Square for {num2}: {num2 ** 2} ")
    print("-----")
    print(f"Perimeter of a square for {num2}: {num2 * 4}")
    print("-----")
    print(f"Diagonal of a square for {num2}: {math.sqrt(2) * num2}")
 else:
    print("!! YOU CANT HAVE NEGATIVE LENGTH !!")
 print("\n")
 print("---- Rectangle ----")
 if num1 and num2 >= 0:
    print(f"Area of a rectangle: {num1 * num2}")
    print("-----")
    print(f"Perimeter of a rectangle: {2 * (num1 + num2)}")
    print("-----")
    print(f"Diagonal of a rectangle: {math.sqrt(num1 ** 2 + num2 ** 2)}")
 else:
    print("!! YOU CANT HAVE NEGATIVE LENGTH !!")
 print("\n")
 print("---- Equilateral triangle ----")
 if num1 >= 0:
    print(f"Area of an equilateral for {num1}: {num1 * num1 * math.sqrt(3)/4}")
    print("-----")
    print(f"Perimeter of an equilateral triangle for {num1}: {num1 * 3}")
 else:
    print("!! YOU CAN'T HAVE NEGATIVE LENGTH !!")
 if num2 >= 0:
    print(f"Area of an equilateral for triangle for {num2}: {num2 * num2 * math.sqrt(3)/4}")
    print("-----")
    print(f"Perimeter of an equilateral triangle for {num2}: {num2 * 3}")
 else:
    print("!! YOU CANT HAVE NEGATIVE LENGTH !!")
 print("\n")
 print("---- Circle ----")
 if num1 >= 0:
    print(f"Area of a circle of {num1}: {num1 ** 2 * math.pi}")
    print("-----")
    print(f"Diameter of a circle for {num1}: {num1 * 2}")
    print("-----")
    print(f"Circumference of a circle for {num1}: {2 * math.pi * num1}")
 else:
    print("you can't have negative lenght")
 if num2 >= 0:
   print(f"Area of a circle of {num2}: {num2 ** 2 * math.pi}")
   print("-----")
   print(f"Diameter of a circle for {num2}: {num2 * 2}")
   print("-----")
   print(f"Circumference of a circle for {num2}: {2 * math.pi * num2}")
 else:
    print("!! YOU CANT HAVE NEGATIVE LENGTH !!")

def main():
   print("Welcome to my calculator (hint: it's a calculator)")
   print("\n")
   running = True

   while running:
      math_tool()
      ask = input("Do another calculation? (y/n): ").strip().lower()
      if ask in ['no', 'NO', 'n', 'N']:
         running = False
         print("\n" + "Thank you for using my calculator!")

if __name__ == "__main__":
   math_tool()
