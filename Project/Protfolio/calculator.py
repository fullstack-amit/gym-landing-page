import math

class SmartCalculator:
    def __init__(self):
        self.memory = 0
    
    # Basic Operations
    def basic_calculator(self):
        print("\n" + "="*50)
        print("     BASIC CALCULATOR MODE")
        print("="*50)
        
        while True:
            try:
                num1 = float(input("\nEnter first number: "))
                
                print("\nSelect operation:")
                print("1. + (Addition)")
                print("2. - (Subtraction)")
                print("3. × (Multiplication)")
                print("4. ÷ (Division)")
                print("5. % (Percentage)")
                print("6. Back to Main Menu")
                
                choice = input("\nEnter choice (1-6): ")
                
                if choice == '6':
                    break
                
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = num1 + num2
                    print(f"\n✓ Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"\n✓ Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"\n✓ Result: {num1} × {num2} = {result}")
                elif choice == '4':
                    if num2 == 0:
                        print("\n✗ Error: Cannot divide by zero!")
                    else:
                        result = num1 / num2
                        print(f"\n✓ Result: {num1} ÷ {num2} = {result}")
                elif choice == '5':
                    result = (num1 / 100) * num2
                    print(f"\n✓ Result: {num1}% of {num2} = {result}")
                else:
                    print("\n✗ Invalid choice!")
                
                cont = input("\nContinue calculation? (y/n): ")
                if cont.lower() != 'y':
                    break
                    
            except ValueError:
                print("\n✗ Invalid input! Please enter numbers only.")
    
    
    # Scientific Operations
    def scientific_calculator(self):
        print("\n" + "="*50)
        print("   SCIENTIFIC CALCULATOR MODE")
        print("="*50)
        
        while True:
            try:
                print("\nSelect operation:")
                print("1. √ (Square Root)")
                print("2. x² (Square)")
                print("3. ± (Sign Flip)")
                print("4. Back to Main Menu")
                
                choice = input("\nEnter choice (1-4): ")
                
                if choice == '4':
                    break
                
                num = float(input("\nEnter number: "))
                
                if choice == '1':
                    if num < 0:
                        print("\n✗ Error: Cannot calculate square root of negative number!")
                    else:
                        result = math.sqrt(num)
                        print(f"\n✓ Result: √{num} = {result}")
                elif choice == '2':
                    result = num ** 2
                    print(f"\n✓ Result: {num}² = {result}")
                elif choice == '3':
                    result = -num
                    print(f"\n✓ Result: ±{num} = {result}")
                else:
                    print("\n✗ Invalid choice!")
                
                cont = input("\nContinue? (y/n): ")
                if cont.lower() != 'y':
                    break
                    
            except ValueError:
                print("\n✗ Invalid input!")
    
    
    # Memory Operations
    def memory_calculator(self):
        print("\n" + "="*50)
        print("    MEMORY CALCULATOR MODE")
        print("="*50)
        print(f"Current Memory: {self.memory}")
        
        while True:
            try:
                print("\nSelect operation:")
                print("1. M+ (Add to Memory)")
                print("2. M- (Subtract from Memory)")
                print("3. MR (Recall Memory)")
                print("4. MC (Clear Memory)")
                print("5. Back to Main Menu")
                
                choice = input("\nEnter choice (1-5): ")
                
                if choice == '5':
                    break
                
                if choice == '1':
                    value = float(input("Enter value to add: "))
                    self.memory += value
                    print(f"\n✓ Memory updated: {self.memory}")
                    
                elif choice == '2':
                    value = float(input("Enter value to subtract: "))
                    self.memory -= value
                    print(f"\n✓ Memory updated: {self.memory}")
                    
                elif choice == '3':
                    print(f"\n✓ Memory Value: {self.memory}")
                    
                elif choice == '4':
                    self.memory = 0
                    print("\n✓ Memory cleared!")
                    
                else:
                    print("\n✗ Invalid choice!")
                    
            except ValueError:
                print("\n✗ Invalid input!")



def main():
    calc = SmartCalculator()
    
    print("="*50)
    print("    SMART CALCULATOR v2.0")
    print("    by Amit Mondal")
    print("="*50)
    
    while True:
        print("\n" + "="*50)
        print("       MAIN MENU")
        print("="*50)
        print("\nChoose Calculator Mode:")
        print("1. Basic Calculator (+ - × ÷ %)")
        print("2. Scientific Calculator (√ x² ±)")
        print("3. Memory Calculator (M+ M- MR MC)")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            calc.basic_calculator()
        elif choice == '2':
            calc.scientific_calculator()
        elif choice == '3':
            calc.memory_calculator()
        elif choice == '4':
            print("\n" + "="*50)
            print("Thank you for using Smart Calculator!")
            print("="*50)
            break
        else:
            print("\n✗ Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()
