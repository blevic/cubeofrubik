import unittest

from cubeofrubik import RubiksCube


class TestRubiksCube(unittest.TestCase):
    """Unit tests for the RubiksCube class."""

    def test_valid_moves(self):
        """Tests if some valid moves don't raise exceptions."""
        valid_moves = ["F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"]
        cube = RubiksCube()

        for moves in valid_moves:
            try:
                cube.move(moves)
            except ValueError:
                self.fail("move() raised ValueError unexpectedly!")

    def test_invalid_moves(self):
        """Tests if some invalid moves raise ValueError exceptions."""
        invalid_moves = ["F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"]
        cube = RubiksCube()

        for moves in invalid_moves:
            with self.assertRaises(ValueError):
                cube.move(moves)

    def test_is_solved(self):
        """Tests if the is_solved() method works as expected."""
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
        """Tests if the get_color() method works as expected."""
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
        """Tests if the find_position() method works as expected."""
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
        """Tests if the get_size() method returns the correct size."""
        cube = RubiksCube()
        self.assertEqual(cube.get_size(), 3)

    def test_solve_random_scramble(self):
        """Tests if some random scrambles can be solved."""
        for _ in range(10):
            cube = RubiksCube()
            cube.scramble()
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_solve_random_scramble_with_parameters(self):
        """Tests if some random scrambles (including special moves) can be solved."""
        for _ in range(10):
            cube = RubiksCube()
            cube.scramble(steps=50, wide_moves=True, slice_moves=True, cube_rotations=True)
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_initial_scramble_solution_concatenation(self):
        """Tests if an initial scramble concatenated with its solution add up to a solved cube state in a new cube."""
        for _ in range(10):
            cube_1 = RubiksCube()
            initial_scramble = cube_1.scramble(steps=40, wide_moves=True, slice_moves=True, cube_rotations=True)
            solution = cube_1.solve()

            cube_2 = RubiksCube()
            cube_2.move(initial_scramble + solution)
            self.assertTrue(cube_2.is_solved())

    def test_set_color(self):
        """Tests if the set_color() method works as expected."""
        colors = list('GROWBY')
        positions = list('FBUDRL') + [a + b for a in list('012345') for b in list('12346789')]
        for color in colors:
            for position in positions:
                cube = RubiksCube()
                cube.set_color(position, color)
                self.assertEqual(cube.get_color(position), color)

    def test_set_all_colors(self):
        """Tests if the set_all_colors() method works as expected."""
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
        """Tests if the is_solvable() method works as expected."""
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

    def test_solve_returns_none(self):
        """Tests if unsolvable cubes and nonexistent methods make the solve() method return None."""
        cube = RubiksCube()
        f_color = cube.get_color('F')
        b_color = cube.get_color('B')
        cube.set_color('F', b_color)
        cube.set_color('B', f_color)
        solution_lbl = cube.solve(method='lbl', change_state=False)
        solution_kociemba = cube.solve(method='kociemba')
        self.assertIsNone(solution_lbl)
        self.assertIsNone(solution_kociemba)

        cube = RubiksCube()
        cube.move("FBUDLRLLpL′L2fulxMMEyzSS′S2")
        cube.set_color('F', 'R')
        solution_kociemba = cube.solve(method='kociemba', change_state=False)
        solution_lbl = cube.solve(method='lbl')
        self.assertIsNone(solution_lbl)
        self.assertIsNone(solution_kociemba)

        cube = RubiksCube()
        cube.scramble()
        solution = cube.solve(method='some_nonexistent_method')
        self.assertIsNone(solution)

    def test_solve_solved_cube(self):
        """Tests if a solved cube can be solved, and returns an empty string."""
        cube = RubiksCube()
        solution = cube.solve(method='kociemba')
        self.assertEqual(solution, '')

        cube = RubiksCube()
        solution = cube.solve(method='lbl')
        self.assertEqual(solution, '')

        cube = RubiksCube()
        cube.move("xyz")
        solution = cube.solve(method='kociemba')
        self.assertEqual(solution, '')

        cube = RubiksCube()
        cube.move("xyz")
        solution = cube.solve(method='lbl')
        self.assertEqual(solution, '')

    def test_solve_change_state(self):
        """Tests if change_state argument from solve method works as expected."""
        cube = RubiksCube()
        cube.scramble()
        cube.solve(change_state=False)
        self.assertFalse(cube.is_solved())

        cube = RubiksCube()
        cube.scramble()
        cube.solve(change_state=True)
        self.assertTrue(cube.is_solved())


if __name__ == '__main__':
    unittest.main()
