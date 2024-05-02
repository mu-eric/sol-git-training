import module as m

while True:
    print('---------------------------')
    print('What would you like to do?')
    print('---------------------------')
    print('1) Reverse a string')
    print('2) Check tolerance')
    print('3) Check asset type')
    print('4) Exit')
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
                print(f'The value ({user_input}) entered {'is' if result else 'is not'} within tolerance.')
            except Exception as Ex:
                print(f'Exception occured: {Ex}, enter a different value.')
        case '3':
            asset_type = input('Enter a asset type name: ')
            result = m.asset_type_check(asset_type)
            print(f'{asset_type} is {'a known' if result else 'not a known'} asset type')
        case '4':
            break
        case _:
            print(f'Invalid selection: {selection}')