import webcolors 
from django import template

register = template.Library()

@register.simple_tag
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - (requested_colour[0])) ** 2
        gd = (g_c - (requested_colour[1])) ** 2
        bd = (b_c - (requested_colour[2])) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

@register.simple_tag
def get_colour_name(requested_colour):
    closest_name = closest_colour(requested_colour)
    return closest_name

print(get_colour_name((139,0,0)))