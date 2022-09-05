import string
import random


def get_true_false(enter):
    if enter == 'T':
        return True
    elif enter == 'F':
        return False
    else:
        return None


def create_password(length=8, upper=False, lower=False, digits=False, punctuation=False):
    try:
        length = int(input('enter pass_length: '))
    except ValueError:
        length = 8

    upper = input('do you want upper?(enter T for True or F for False) : ')
    lower = input('do you want lower?(enter T for True or F for False) : ')
    digits = input('do you want digits?(enter T for True or F for False) : ')
    punctuation = input('do you want punctuation?(enter T for True or F for False) : ')

    choices_list = []
    if get_true_false(upper):
        choices_list.append('u')
    if get_true_false(lower):
        choices_list.append('l')
    if get_true_false(digits):
        choices_list.append('d')
    if get_true_false(punctuation):
        choices_list.append('c')

    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    password = list()
    try:
        for i in range(length):
            choice_ = random.choice(choices_list)
            if choice_ == 'u':
                chosen = random.choice(upper)
                password.append(chosen)
            elif choice_ == 'l':
                chosen = random.choice(lower)
                password.append(chosen)
            elif choice_ == 'd':
                chosen = random.choice(digits)
                password.append(chosen)
            else:
                chosen = random.choice(punctuation)
                password.append(chosen)
    except (ValueError, IndexError):
        for i in range(length):
            chosen = random.choice(list(string.ascii_letters))
            password.append(chosen)

    password = ''.join(password)
    return password


if __name__ == '__main__':
    print(create_password())
