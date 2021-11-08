class TicTacToe:
    def __init__(self):
        self.field = ' ' * 9
        self.dashes = "---------"
        # self.coord = ''
        # self.row_list = []
        # self.colum_list = []
        # self.diagonal_list = []
        self.t_t_t = [[self.field[0], self.field[1], self.field[2]], [self.field[3], self.field[4], self.field[5]],
                      [self.field[6], self.field[7], self.field[8]]]
        self.moves = 0

    # def check(self, list_):
    #     for i in range(3):
    #         if list_[i][0] == list_[i][1] == list_[i][2]:
    #             if list_[i][0] != ' ':
    #                 self.row_list.append(list_[0][i])
    #             return self.row_list
    #         if list_[0][i] == list_[1][i] == list_[2][i]:
    #             if list_[0][i] != ' ':
    #                 self.colum_list.append(list_[0][i])
    #             return self.colum_list
    #     if list_[0][0] == list_[1][1] == list_[2][2] or list_[2][0] == list_[1][1] == list_[0][2]:
    #         if list_[1][1] != ' ':
    #             self.diagonal_list.append(list_[1][1])
    #         return self.diagonal_list
    def check_row(self, list_):
        new_list = []
        for i in range(3):
            if list_[i][0] == list_[i][1] == list_[i][2]:
                if list_[i][0] != ' ':
                    new_list.append(list_[0][i])
        return new_list

    def check_column(self, list_):
        new_list = []
        for i in range(3):
            if list_[0][i] == list_[1][i] == list_[2][i]:
                if list_[0][i] != ' ':
                    new_list.append(list_[0][i])
        return new_list

    def check_diagonal(self, list_):
        new_list = []
        if list_[0][0] == list_[1][1] == list_[2][2] or list_[2][0] == list_[1][1] == list_[0][2]:
            if list_[1][1] != ' ':
                new_list.append(list_[1][1])
        return new_list

    def menu(self):
        print(self.dashes)
        print('|', self.t_t_t[0][0], self.t_t_t[0][1], self.t_t_t[0][2], '|')
        print('|', self.t_t_t[1][0], self.t_t_t[1][1], self.t_t_t[1][2], '|')
        print('|', self.t_t_t[2][0], self.t_t_t[2][1], self.t_t_t[2][2], '|')
        print(self.dashes)

    def win_condition(self):

        self.winner = self.check_column(self.t_t_t) + self.check_row(self.t_t_t) + self.check_diagonal(self.t_t_t)
        self.menu()

        while True:
            self.winner = self.check_column(self.t_t_t) + self.check_row(self.t_t_t) + self.check_diagonal(self.t_t_t)

            coords = input('Enter the coordinates: ')
            x, y = coords.split()
            if not (x.isdigit() and y.isdigit()):
                print('You should enter numbers!')
                continue
            if int(x) not in range(1, 4) or int(y) not in range(1, 4):
                print('Coordinates should be from 1 to 3!')
                continue
            y = int(y) - 1
            x = int(x) - 1
            if self.t_t_t[x][y] == ' ' and self.moves % 2 == 0:
                self.t_t_t[x][y] = 'X'
                self.moves += 1
                self.menu()

                if abs(self.field.count('X') - self.field.count('O')) > 1:
                    print('Impossible')
                    break
                elif len(self.winner) > 1:
                    print('Impossible')
                    break

                elif len(self.winner) == 0 and ' ' not in self.field:
                    print('Draw')
                    break
                elif self.winner:
                    print(f'{self.winner[0]} wins')
                    break
            elif self.t_t_t[x][y] == ' ' and self.moves % 2 == 1:
                self.t_t_t[x][y] = 'O'
                self.moves += 1
                self.menu()

                if abs(self.field.count('X') - self.field.count('O')) > 1:
                    print('Impossible')
                    break
                elif len(self.winner) > 1:
                    print('Impossible')
                    break

                elif len(self.winner) == 0 and ' ' not in self.field:
                    print('Draw')
                    break
                elif self.winner:
                    print(f'{self.winner[0]} wins')
                    break
            else:
                print('This cell is occupied! Choose another one!')


    def main(self):

        self.win_condition()



TicTacToe().main()
