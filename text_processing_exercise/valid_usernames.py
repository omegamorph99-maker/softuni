def check_length(name: str) -> bool:
    if 3 <= len(name) <= 16:
        return True

def check_symbols(name: str) -> bool:
    if name.isalnum() or '-' in name or '_' in name:
        return True

def check_empty_space(name: str) -> bool:
    if len(name) == len(name.strip()):
        return True

def wrap(name: str) -> bool:
    if check_length(name) and check_symbols(name) and check_empty_space(name):
        return True


username = input().split(', ')

for user in username:
    if wrap(user):
        print(user)