def func():
    """Все буквы заглавные"""
    text = input('Введите слово')
    return text.upper()


print(func())

def func2(text):
    """Принимает текст,
    возвращает с большой буквы"""
    return text.title()