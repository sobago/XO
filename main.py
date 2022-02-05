print('==========================================\n'
      '            КРЕСТИКИ-НОЛИКИ\n'
      '==========================================\n'
      'Формат ввода: x y (два числа через пробел)\n'
      'x - номер строки, y - номер столбца\n'
      '==========================================')

field = [[['-', 0], ['-', 0], ['-', 0]],
        [['-', 0], ['-', 0], ['-', 0]],
        [['-', 0], ['-', 0], ['-', 0]],
        ]
player_x = input('Введите имя игрока x: ')
player_o = input('Введите имя игрока o: ')

step_count = player_x
counter = 0

def print_field():
    print(f'\t0\t1\t2')
    for i in range(3):
        print(f'{i}\t{field[i][0][0]}\t{field[i][1][0]}\t{field[i][2][0]}')
    print(f'x - {player_x}, o - {player_o}\n')

def step():
    while True:
        coordinates = input(f"Ваш ход, {step_count}: ").split()
        if len(coordinates) != 2:
            print('Необходимо ввести 2 координаты через пробел (сначала строка, затем столбец)')
            continue
        x, y = coordinates

        if not x.isdigit() or not y.isdigit():
            print('Можно вводить только числа!')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y <0 or y > 2:
            print('Координаты могут быть от 0 до 2!')
            continue

        if field[x][y][0] != '-':
            print('Клетка уже занята, попробуйте другую!')
            continue
        return x, y

def check_win(field):
    if field[0][0][1] != 0 and field[0][0] == field[0][1] and field[0][1] == field[0][2]:
        print_field()
        print(f'Выигрыш за {field[0][0][1]}! Поздравляем!')
        return True
    elif field[1][0][1] != 0 and field[1][0] == field[1][1] and field[1][1] == field[1][2]:
        print_field()
        print(f'Выигрыш за {field[1][0][1]}! Поздравляем!')
        return True
    elif field[2][0][1] != 0 and field[2][0] == field[2][1] and field[2][1] == field[2][2]:
        print_field()
        print(f'Выигрыш за {field[2][0][1]}! Поздравляем!')
        return True
    elif field[0][0][1] != 0 and field[0][0] == field[1][0] and field[1][0] == field[2][0]:
        print_field()
        print(f'Выигрыш за {field[0][0][1]}! Поздравляем!')
        return True
    elif field[0][1][1] != 0 and field[0][1] == field[1][1] and field[1][1] == field[1][2]:
        print_field()
        print(f'Выигрыш за {field[0][1][1]}! Поздравляем!')
        return True
    elif field[0][2][1] != 0 and field[0][2] == field[1][2] and field[1][2] == field[2][2]:
        print_field()
        print(f'Выигрыш за {field[0][2][1]}! Поздравляем!')
        return True
    elif field[0][0][1] != 0 and field[0][0] == field[1][1] and field[1][1] == field[2][2]:
        print_field()
        print(f'Выигрыш за {field[0][0][1]}! Поздравляем!')
        return True
    elif field[0][2][1] != 0 and field[0][2] == field[1][1] and field[1][1] == field[2][0]:
        print_field()
        print(f'Выигрыш за {field[0][2][1]}! Поздравляем!')
        return True
    else:
        return False

while True:
    counter += 1
    print_field()
    x, y = step()
    field[x][y][1] = step_count

    if step_count == player_x:
        field[x][y][0] = 'x'
        step_count = player_o
    else:
        field[x][y][0] = 'o'
        step_count = player_x

    if check_win(field):
        break

    if counter == 9:
        print_field()
        print('Победила дружба! :)\nНичья.')
        break