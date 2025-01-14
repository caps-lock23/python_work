def addition():
    while True:
        try:
            num1 = input('Input the first number: ')
            if num1.lower() == 'q':
                break
            num1 = int(num1)
            num2 = input('Input the second number: ')
            if num2.lower() == 'q':
                break
            num2 = int(num2)
        except ValueError:
            print('Your input is not a number')
        else:
            num3 = num1 + num2
            print(f'Result: {num3}')

addition()

