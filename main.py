import module as m
import time

while True:
    print('---------------------------')
    print('What would you like to do?')
    print('---------------------------')
    print('1) Reverse a string')
    print('2) Check tolerance')
    print('3) Exit')
    selection = input()

    match selection:
        case '1':
            text = input('Enter text to reverse: ')
            result = m.reverse(text)
            print(f'Original: {text}')
            print(f'Reversed: {result}')
        case '2':
            try:
                user_input = float(input('Enter a value: '))
                result = m.tolerance_check(user_input)
                print(f'The value ({user_input}) entered is {'' if result else 'not'} within tolerance.')
            except Exception as Ex:
                print(f'Exception occured: {Ex}, enter a different value.')
        case '3':
            break
        case _:
            print(f'Invalid selection: {selection}')

    time.sleep(5)
    print('Returning to main menu in 5 seconds...')