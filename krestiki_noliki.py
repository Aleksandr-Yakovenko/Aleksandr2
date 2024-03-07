print("*" * 10, "Крестики нолики", "*" * 10)

board = list(range(1, 10))
you_win = [(1, 2, 3),(4, 5, 6),(7, 8, 9),(1, 4, 7),(2, 5, 8),(3, 6, 9),(1, 5, 9),(3, 5, 7)]

def game_board():
    """рисуем игровое поле"""
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("-------------")

def XO_inrut(token):
    """'Делаем ход"""
    while True:
        value = input("Куда поставить : " + token + ' ?')
        if not (value in "123456789"):
            print("Ошибочный ввод.")
            continue
        value = int(value)
        if str(board[value - 1]) in "XO":
            print("Эта клетка уже занята")
            continue
        board[value - 1] = token
        break

def chek_win():
    """проверка на выигрыш"""
    for each in you_win:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False

def main():
    """игра"""
    symbol = 0
    while True:
        game_board()
        if symbol % 2 == 0:
            XO_inrut("X")
        else:
            XO_inrut("O")
        if symbol > 3:
            winner = chek_win()
            if winner:
                game_board()
                print(winner, "Выиграл!")
                break
        symbol += 1
        if symbol > 8:
            game_board()
            print('Ничья')
            break

main()


