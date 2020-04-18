from matrix import Matrix
import unittest

class MatrixTest(unittest.TestCase):

    def test_rows(self):
<<<<<<< HEAD
        assert Matrix.row('9 8 7\n5 3 2\n6 6 7') == '987532667'
=======
        assert Matrix.row('9 8 7\n5 3 2\n6 6 7') == '987'
>>>>>>> d440df4fe75ea907e81af4ed3661e78de3f833cd

    def test_columns(self):
        assert Matrix.column('9 8 7\n5 3 2\n6 6 7') == '956836727'

if __name__ == '__main__':
    unittest.main()