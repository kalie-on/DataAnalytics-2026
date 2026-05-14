import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

product_of_the_day = random.choice(products)
print("Product of the Day:")
print(product_of_the_day)

survey_products = random.sample(products, 3)
print("\nProducts selected for usability survey:")
print(survey_products)

random.shuffle(products)
print("\nShuffled product list:")
print(products)

transaction_count = random.randint(50, 300)
print("\nSimulated daily transaction count:")
print(transaction_count)