import sys as sys


def count_chars(user_input: str):
    print(f"The text contains {len(user_input)} characters:")
    print(f"{sum(c.isupper() for c in user_input)} upper letters")
    print(f"{sum(c.islower() for c in user_input)} lower letters")
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    punct_sum = sum(1 for c in user_input if c in punctuation)
    print(f"{punct_sum} punctuation marks")
    print(f"{user_input.count(' ')} spaces")
    print(f"{sum(c.isdigit() for c in user_input)} digits")


def ft_building():
    user_input = None
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument provided")
    if len(sys.argv) < 2 or sys.argv[1] == "None":
        user_input = input("What is the text to count?\n").strip()
    else:
        user_input = sys.argv[1].strip()
    count_chars(user_input)


if __name__ == "__main__":
    try:
        ft_building()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
