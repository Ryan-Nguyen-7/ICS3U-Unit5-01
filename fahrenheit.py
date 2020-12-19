# Created by Ryan Nguyen
# Created on December 2020
# This program uses a function to convert celsius to fahrenheit


def fahrenheit():
    # This function converts temperature in
    #   degrees to celsius

    # input
    Tc_as_string = input("Enter temperature in degrees celsius: ")
    try:
        Tc_as_number = int(Tc_as_string)
        Tf = (9/5) * Tc_as_number + 32
    except Exception:
        print("Invalid integer")
    print("{}°C is equal to {}°F".format(Tc_as_number, Tf))


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
