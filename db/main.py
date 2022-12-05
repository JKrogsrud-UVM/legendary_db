from db.data import clean_list

"""
main.py will be responsible for interface with command line
It will be responsible for informing the user of the types of commands they can make
"""


def main():
    stuff = clean_list(['Hero', 'team', 'Viriol/Fries', 'Burger/Fries', 'hello this is, fine', 'yup', 'CW'])
    print(stuff)

if __name__ == '__main__':
    main()