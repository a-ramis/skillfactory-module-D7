from django import template

register = template.Library()

censor_list = ['редиска']

# фильтр censor, который заменяет буквы нежелательных слов в заголовках и текстах статей на символ «*»
@register.filter()
def censor(value):
    """
   value: значение, к которому нужно применить фильтр
   """
    if isinstance(value, str):
        for word in censor_list:
            value = value.replace(word[1:], '*' * len(word[1:]))
        return value
    else:
        return value
