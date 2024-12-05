def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
def get_sum(number1, number2):
    return number1 + number2

def main():
    first_name = "Tanvir"
    last_name = "Alam"
    full_name = get_full_name(first_name, last_name)
    print(f"Your full name is: {full_name}")
    num1 = 5
    num2 = 6
    total = get_sum(num1, num2)
    print(f"Total sum is : {total}")

if __name__ == "__main__":
    main()
