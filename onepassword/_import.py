import string


lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

symbols = symbols.replace(r'"', r'')
symbols = symbols.replace(r"'", r'')
symbols = symbols.replace(r',', r'')
symbols = symbols.replace(r'.', r'')
symbols = symbols.replace(r':', r'')
symbols = symbols.replace(r'`', r'')
symbols = symbols.replace(r';', r'')
symbols = symbols.replace("\\", r'')
symbols = symbols.replace(r'/', r'')
symbols = symbols.replace(r'(', r'')
symbols = symbols.replace(r')', r'')
symbols = symbols.replace(r'_', r'')
