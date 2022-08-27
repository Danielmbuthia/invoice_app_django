import random

available_numbers = [x for x in range(10)]
size = 26


def generate_account_number():
    number_list = [str(random.choice(available_numbers)) for _ in range(26)]
    return "".join(number_list)
