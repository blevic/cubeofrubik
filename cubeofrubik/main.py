from cubeofrubik import RubiksCube

if __name__ == '__main__':
    cube = RubiksCube()
    initial_scramble = cube.scramble()
    print("Initial scramble:", initial_scramble)
    cube.draw()
    kociemba_moves = cube.solve(method='kociemba', change_state=False)
    lbl_solution_moves = cube.solve(method='lbl')
    print("Kociemba solution:", kociemba_moves)
    print("Layer by Layer solution:", lbl_solution_moves)
