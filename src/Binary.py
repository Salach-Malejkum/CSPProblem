
class Binary:
    def __init__(self):
        self.constant_matrix = []
        self.binary_matrix = []
        self.size_n = -1

    def load_data6x6(self):
        tmp = []
        with open("binary/binary_6x6") as f:
            for line in f:
                line_data = list(line.strip())
                tmp.append([int(x) if x != 'x' else -1 for row in line_data for x in row])
        self.constant_matrix = tmp
        self.binary_matrix = tmp
        self.size_n = len(tmp)

    def load_data8x8(self):
        tmp = []
        with open("binary/binary_8x8") as f:
            for line in f:
                line_data = list(line.strip())
                tmp.append([int(x) if x != 'x' else -1 for row in line_data for x in row])
        self.constant_matrix = tmp
        self.binary_matrix = tmp
        self.size_n = len(tmp)

    def load_data10x10(self):
        tmp = []
        with open("binary/binary_10x10") as f:
            for line in f:
                line_data = list(line.strip())
                tmp.append([int(x) if x != 'x' else -1 for row in line_data for x in row])
        self.constant_matrix = tmp
        self.binary_matrix = tmp
        self.size_n = len(tmp)

    def compute_matrix_backtracking(self):
        if self.binary_matrix != [] and self.size_n != -1:
            # for i in range(self.size_n):
            #     for j in range(self.size_n):
            #         self.check_rows_columns(i, j)
            if self.check_row_column(2, 4):
                pass

    def check_row_column(self, i, j):
        bool_row = False
        bool_column = False
        row = []
        column = []
        for x in range(self.size_n):
            row.append(self.binary_matrix[i][x])
            column.append(self.binary_matrix[x][j])
        print(row, column)
        return bool_column or bool_row

    def print_matrix(self):
        for row in self.binary_matrix:
            print(row)
            

