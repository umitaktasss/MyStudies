# I have a N given numbers of flowers whose colors are black white or purple and
#  I am supposed to organize them so that the flowers of the same color are adjacent, 
# in the order black, white and purple. In python



# a simple sorting- Python's built-in sorting functions
#
def sort_flowers(flower_colors):
    color_order = {'black':0, 'white':1, 'purple':2}
    sorted_flowers=sorted(flower_colors, key=lambda color: color_order[color])
    return sorted_flowers

flowers = ['purple', 'white', 'black', 'purple', 'white', 'black']
sorted_flowers = sort_flowers(flowers)
print(sorted_flowers)