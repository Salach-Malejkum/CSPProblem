
class Futoshiki:
    def __init__(self):
        self.binary_matrix = {}

    def load_data4x4(self):
        counter = 0
        tmp = []
        with open("futoshiki/futoshiki_4x4") as f:
            for line in f:
                line_data = list(line.strip())
                tmp.append([int(x) if x != 'x' else -1 for row in line_data for x in row])
                counter += 1
        print(tmp)

    def load_data5x5(self):
        pass

    def load_data6x6(self):
        pass