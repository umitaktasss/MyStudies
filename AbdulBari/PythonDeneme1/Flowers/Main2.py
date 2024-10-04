import random

def generate_random_flowers(num_flowers):
    colors = ['black', 'white', 'purple']
    flowers = [random.choice(colors) for _ in range(num_flowers)]
    return flowers

def sorted_flowers(flower_colors):
    color_order = {'black': 0, 'white': 1, 'purple': 2}
    sorted_flowers = sorted(flower_colors, key=lambda color: color_order[color])
    return sorted_flowers

num_flowers = 10
flowers = generate_random_flowers(num_flowers)
print("Unsorted flowers:", flowers)

sorted_flower_list = sorted_flowers(flowers)
print("Sorted flowers:", sorted_flower_list)