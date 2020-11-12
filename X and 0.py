bord = list(range(1, 10))


def game_bord(bord):
    for i in range(3):
        print(bord[0 + i * 3], bord[1 + i * 3], bord[2 + i * 3])


def cross():
    # move_x = int(input('Введите число куда бы вы хотеи поставит Х:'))
    # if move_x in bord:
    #     bord[move_x - 1] = 'X'
    # else:
    #     print('клетка уже занята')
    validator = False
    while not validator:
        move_x = int(input('Введите число куда бы вы хотеи поставит Х: '))
        if move_x in bord:
            bord[move_x - 1] = 'X'
            validator = True
        else:
            print('клетка уже занята или вы ввели число меньше 1 или боольше 9')
            continue


def zero():
    # move_0 = int(input('Введите число куда бы вы хотеи поставит 0:'))
    # if move_0 in bord:
    #     bord[move_0 - 1] = '0'
    # else:
    #     print('клетка уже занята')
    validator = False
    while not validator:
        move_0 = int(input('Введите число куда бы вы хотеи поставит 0: '))
        if move_0 in bord:
            bord[move_0 - 1] = '0'
            validator = True
        else:
            print('клетка уже занята или вы ввели число меньше 1 или боольше 9')
            continue


def check_win(bord):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if bord[each[0]] == bord[each[1]] == bord[each[2]]:
            return bord[each[0]]
    return False


print("Это игровое поле")
game_bord(bord)
counter = 0
win = False
while not win:
    cross()
    counter += 1
    if counter > 4:
        tmp = check_win(bord)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            game_bord(bord)
            break
    if counter == 9:
        print('ничья')
        break
    game_bord(bord)
    zero()
    game_bord(bord)
    counter += 1
    if counter > 4:
        tmp = check_win(bord)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
