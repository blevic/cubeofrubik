import unittest

from RubiksCube import RubiksCube


class TestRubikCube(unittest.TestCase):

    def test_valid_moves(self):
        valid_moves = ["F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"]
        cube = RubiksCube()

        for moves in valid_moves:
            try:
                cube.move(moves)
            except ValueError:
                self.fail("move() raised ValueError unexpectedly!")

    def test_invalid_moves(self):
        invalid_moves = ["F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"]
        cube = RubiksCube()

        for moves in invalid_moves:
            with self.assertRaises(ValueError):
                cube.move(moves)

    def test_is_solved(self):
        cube = RubiksCube()
        self.assertTrue(cube.is_solved())

        cube = RubiksCube()
        cube.move("xyzxpypzpx2xy2z2")
        self.assertTrue(cube.is_solved())

        cube = RubiksCube()
        for i in range(6):
            cube.move("RURpUp")
            if i == 5:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        cube = RubiksCube()
        for i in range(1260):
            cube.move("DRpU2M")
            if i == 1259:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        cube = RubiksCube()
        cube.move("FFpBBpUUpDDpLLpRRpffpbbpuupddpllprrpxxpyypzzpMMpEEpSSp")
        self.assertTrue(cube.is_solved())

    def test_get_color(self):
        cube = RubiksCube()
        self.assertEqual(cube.get_color('F'), 'G')
        self.assertEqual(cube.get_color('U'), 'W')
        self.assertEqual(cube.get_color('D'), 'Y')

        self.assertEqual(cube.get_color('01'), 'G')
        self.assertEqual(cube.get_color('11'), 'W')
        self.assertEqual(cube.get_color('31'), 'Y')

        cube.move("F")
        self.assertEqual(cube.get_color('32'), 'R')

        cube = RubiksCube()
        for invalid_piece in ['', 'FF', 'FUY', 'Y', 'f', 'FURB', 'FB', 'UR', '15', '5', '6', '66']:
            with self.assertRaises(ValueError):
                cube.get_color(invalid_piece)

    def test_find_position(self):

        cube = RubiksCube()
        self.assertEqual(cube.find_position('G'), 'F')
        self.assertEqual(cube.find_position('W'), 'U')
        self.assertEqual(cube.find_position('R'), 'R')

        self.assertEqual(cube.find_position('G', 'W'), 'FU')
        self.assertEqual(cube.find_position('W', 'G'), 'UF')
        self.assertEqual(cube.find_position('G', 'R'), 'FR')
        self.assertEqual(cube.find_position('R', 'G'), 'RF')

        self.assertEqual(cube.find_position('G', 'W', 'R'), 'FUR')
        self.assertEqual(cube.find_position('G', 'R', 'W'), 'FRU')
        self.assertEqual(cube.find_position('W', 'G', 'R'), 'UFR')
        self.assertEqual(cube.find_position('W', 'R', 'G'), 'URF')
        self.assertEqual(cube.find_position('R', 'G', 'W'), 'RFU')
        self.assertEqual(cube.find_position('R', 'W', 'G'), 'RUF')

        cube = RubiksCube()
        cube.move('F')
        self.assertEqual(cube.find_position('R', 'G'), 'DF')

        cube = RubiksCube()
        invalid_pieces = {
            (),
            ('W', 'Y'),
            (0, 1),
            ('W', 'G', 'R', 'Y'),
            (('W',),)
        }

        for invalid_piece in invalid_pieces:
            with self.assertRaises(ValueError):
                cube.find_position(invalid_piece)

    def test_get_size(self):
        cube = RubiksCube()
        self.assertEqual(cube.get_size(), 3)

    def test_solve_random_scramble(self):
        for _ in range(10):
            cube = RubiksCube()
            cube.scramble()
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_solve_random_scramble_with_parameters(self):
        for _ in range(10):
            cube = RubiksCube()
            cube.scramble(steps=50, wide_moves=True, slice_moves=True, cube_rotations=True)
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_initial_scramble_solution_concatenation(self):
        for _ in range(10):
            cube_1 = RubiksCube()
            initial_scramble = cube_1.scramble(steps=40, wide_moves=True, slice_moves=True, cube_rotations=True)
            solution = cube_1.solve()

            cube_2 = RubiksCube()
            cube_2.move(initial_scramble.replace(" ", "") + solution)
            self.assertTrue(cube_2.is_solved())

    def test_set_color(self):
        colors = list('GROWBY')
        positions = list('FBUDRL') + [a + b for a in list('012345') for b in list('12346789')]
        for color in colors:
            for position in positions:
                cube = RubiksCube()
                cube.set_color(position, color)
                self.assertEqual(cube.get_color(position), color)

    def test_set_all_colors(self):
        colors = list('GROWBY')
        positions = list('FBUDRL') + [a + b for a in list('012345') for b in list('12346789')]

        colors_dict = {}

        for idx, position in enumerate(positions):
            colors_dict[position] = colors[idx % len(colors)]

        cube = RubiksCube()
        cube.set_all_colors(colors_dict)

        for position in positions:
            self.assertEqual(cube.get_color(position), colors_dict[position])

    def test_is_solvable(self):
        cube = RubiksCube()
        self.assertTrue(cube.is_solvable())

        cube = RubiksCube()
        cube.move("FBUDLRLLpL′L2fulxMMEyzSS′S2")
        self.assertTrue(cube.is_solvable())

        cube = RubiksCube()
        f_color = cube.get_color('F')
        b_color = cube.get_color('B')
        cube.set_color('F', b_color)
        cube.set_color('B', f_color)
        self.assertFalse(cube.is_solvable())

        cube = RubiksCube()
        cube.move("FBUDLRLLpL′L2fulxMMEyzSS′S2")
        cube.set_color('F', 'R')
        self.assertFalse(cube.is_solvable())


if __name__ == '__main__':
    unittest.main()
