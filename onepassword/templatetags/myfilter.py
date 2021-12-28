from django import template

register = template.Library()

def isdigit(value:str):

    return value.isdigit()


register.filter(isdigit)
