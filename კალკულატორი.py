print("ფინალური დავალება 1")

# 2.1 კალკულატორი

def calculator():
    print("კალკულატორი — შეიყვანეთ ორი რიცხვი")

    #strip შლის ტექსტიდან ზედმეტ სიმბოლოებს

    while True:
        try:
            raw1 = input("შეიყვანეთ პირველი რიცხვი: ").strip()
            raw2 = input("შეიყვანეთ მეორე რიცხვი: ").strip()

            # ანაცვლებს ,-ს . ით, რადგან სწორად აღიქვას რიცხვი
            raw1 = raw1.replace(",", ".")
            raw2 = raw2.replace(",", ".")

            num1 = float(raw1)
            num2 = float(raw2)

            operation = input("აირჩიეთ ოპერაცია (+, -, *, /): ").strip()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("ნულზე გაყოფა არ შეიძლება!")
                    continue
                result = num1 / num2
            else:
                print("არასწორი ოპერაცია — გამოიყენეთ მხოლოდ +, -, * ან /.")
                continue

            print(f"შედეგი: {result}")

            again = input("გაგრძელება? (y/n): ").strip().lower()
            if again != "y":
                print("კალკულატორი დასრულდა.")
                break
            
# გამორიცხავს პროგრამის გაჩერებას

        except ValueError:
            print("რიცხვი არასწორია — დარწმუნდით, რომ შეიყვანეთ სწორი ციფრები")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nპროგრამა შეაჩერა მომხმარებელმა.")
            break

# უზრუნველყოფს, რომ კოდი გაეშვება,

if __name__ == "__main__":
    calculator()
