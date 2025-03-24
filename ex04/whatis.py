# main, exceptions and sys argv
import sys as sys


def ft_even_or_odd():
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(sys.argv) < 2:
        return
    num = sys.argv[1].lstrip('+-')
    if not num.isdigit():
        raise AssertionError("argument is not an integer")
    n = int(num)
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    try:
        ft_even_or_odd()
    except AssertionError as e:
        print(f"AssertionError: {e}")
