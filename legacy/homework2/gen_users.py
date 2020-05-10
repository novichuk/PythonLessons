from faker import Faker


def generate_users(amount):
    fake = Faker()
    result = {}
    for i in range(1, amount + 1):
        result[i] = f'{fake.name()}, {fake.email()}'
    return result
