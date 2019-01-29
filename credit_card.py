import re
import argparse

PATTERN='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

def is_valid_card_number(sequence):
    """Returns `True' if the sequence is a valid credit card number.

    A valid credit card number
    - must contain exactly 16 digits,
    - must start with a 4, 5 or 6 
    - must only consist of digits (0-9),
    - may have digits in groups of 4, separated by one hyphen "-". 
    - must NOT use any other separator like ' ' , '_',
    - must NOT have 4 or more consecutive repeated digits.
    """

    match = re.match(PATTERN,sequence)

    if match == None:
        return False

    for group in match.groups():
        if group[0] * 4 == group:
            return False
    return True


if __name__ == '__main__':
    # defined parser to parse
    parser = argparse.ArgumentParser(description='Credit Card validator')
    parser.add_argument('--cardno','-c',help='16 digit card number',required=True )
    args = parser.parse_args()
    result = is_valid_card_number(args.cardno)
    if result :
        print(args.cardno + " Valid")
    else:
        print(args.cardno + " Invalid")
