import module as m

while True:
    text = input('Enter text to reverse: ')
    result = m.reverse(text)
    print(f'Original: {text}')
    print(f'Reversed: {result}')