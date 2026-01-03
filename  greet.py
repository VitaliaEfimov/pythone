def greet(name, greeting="Hello"):
    """Выведите приветствие пользователю 'name'.
    
    Дополнительный параметр 'greeting' может изменить то с чем они будут поздравлены"""
    print(f"{greeting}{name}")
print(greet.__doc__)
help(greet)
def greet2(name, greeting="Hello"):
    # Выведите приветствие пользователю 'name'.
    # Дополнительный параметр 'greeting' может изменить то с чем они будут поздравлены
    print(f"{greeting}{name}")
print(greet2.__doc__)
help(greet2)