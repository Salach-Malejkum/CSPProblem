import Binary
import Futoshiki

if __name__ == '__main__':
    bin = Binary.Binary()
    bin.load_data6x6()
    bin.compute_matrix_backtracking()
    bin.print_matrix()

    # fut = Futoshiki.Futoshiki()
    # fut.load_data4x4()
