import random


# get Random integer
def get_random_int(min_number, max_number):
    return random.randint(min_number, max_number)


# get Random math operator
def get_random_math_operator():
    return random.choice(['+', '-', '*'])


# get result
def get_result(number1, number2, operator):
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem, answer


def math_quiz():
    s = 0
    stop = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(stop):
        number1 = get_random_int(1, 10)  # get 1st int number
        number2 = get_random_int(1, int(5.5))  # get 2nd int number
        operator = get_random_math_operator()  # get math operator

        problem, answer = get_result(number1, number2, operator)  # get result
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
        except Exception as e:
            print("Exception is ", e)
        else:
            if user_answer == answer:
                print("Correct! You earned a point.")
                s += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {s}/{stop}")


if __name__ == "__main__":
    math_quiz()
