def calculate_future_age(age):
    return int(age) + 5


if __name__ == "__main__":
    name = input("What is your name? ")
    age = input("How old are you? ")

    print(f"\nHello {name}!")
    print(f"You are {age} years old.")

    future_age = calculate_future_age(age)

    print(f"In 5 years, you will be {future_age} years old.")
    print("Welcome to your first GitHub project!")