def sorted_flowers(flower_colors):
    color_order={'black':0,'white':1,'purple':2}
    sorted_flowers=sorted(flower_colors, key=lambda color: color_order[color])
    return sorted_flowers

