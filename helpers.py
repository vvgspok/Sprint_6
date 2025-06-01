import random
from data import addresses, metro, names, surnames, phones, rental_period, color_scooter, comment_for_courier
from datetime import datetime, timedelta


def random_address():
    return random.choice(addresses)


def random_metro():
    return random.choice(metro)


def random_name():
    return random.choice(names)


def random_surname():
    return random.choice(surnames)


def random_phone():
    return random.choice(phones)


def generation_random_data():
    start_year = 2000
    end_year = 2025
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%d.%m.%Y")


def random_rental_period():
    return random.choice(rental_period)


def random_color_scooter():
    return random.choice(color_scooter)


def random_comment_for_courier():
    return random.choice(comment_for_courier)
