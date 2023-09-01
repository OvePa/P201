import re
import itertools


common_words = ["password", "123456", "qwerty", "abc123"]
common_patterns = ["abcd", "1234", "qwer", "asdf"]


def password_strength_checker(password):
    # Use regular expressions to check the password for length, complexity, and
    # dictionary words
    if len(password) < 8:
        # Password is too short
        print("Password is too short!")
        return 0
    elif not re.search(r"[A-Z]", password):
        # Password does not contain an uppercase letter
        print("Password does not contain an uppercase letter!")
        return 0
    elif not re.search(r"[a-z]", password):
        # Password does not contain a lowercase letter
        print("Password does not contain a lowercase letter!")
        return 0
    elif not re.search(r"[0-9]", password):
        # Password does not contain a digit
        print("Password does not contain a digit!")
        return 0
    elif not re.search(r"[^A-Za-z0-9]", password):
        # Password does not contain a special character
        print("Password does not contain a special character!")
        return 0
    else:
        # Password meets all the above criteria
        print("Password meets all the above criteria!")
        score = 100
    return score


def calculate_score(password):
    score = password_strength_checker(password)
    for word in itertools.chain(common_words, common_patterns):
        if word in password.lower():
            score -= 25
            break

    return score


if __name__ == "__main__":
    # print(calculate_score("asd34"))
    print(password_strength_checker("asdA$daKk34"))
    # print(password_strength_checker("asdA$daKk"))

    password = "asd34"
    score = password_strength_checker(password)

    print(password_strength_checker("Abc123!@"))
    # abc common pattern - 75
    print(password_strength_checker("abc123"))
    # 0 (too short)
    print(password_strength_checker("ABC123!"))
    # 0 (no lowercase letter)
    print(password_strength_checker("Qazxsw23@#!"))
    # 100 (no digits or special characters)
    print(password_strength_checker("Abcd1234!"))
    # 75 (common word)
    print(password_strength_checker("aB34567!"))
    # 100
