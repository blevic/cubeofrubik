from rubikscube.RubiksCube import RubiksCube

if __name__ == '__main__':
    cube = RubiksCube()
    initial_scramble = cube.scramble()
    print("Initial scramble:", initial_scramble)
    cube.draw()
    lbl_solution_moves = cube.solve()
    print("Layer by layer solution:", lbl_solution_moves)
