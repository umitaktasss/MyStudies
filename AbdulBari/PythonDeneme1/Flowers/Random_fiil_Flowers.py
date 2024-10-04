import random

def generate_random_flowers(num_flowers):
    colors = ['black', 'white', 'purple']
    flowers = [random.choice(colors) for _ in range(num_flowers)]
    r_flowers=flowers
    return r_flowers
