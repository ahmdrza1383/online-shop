from django import template

register = template.Library()


@register.filter
def translate_num_to_persian(num):
    num = str(num)
    english = '0123456789'
    persian = '۰١٢٣٤٥٦٧٨٩'
    en_to_per_table = str.maketrans(english, persian)
    return num.translate(en_to_per_table)
