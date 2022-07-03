class RubiksCubeInterface:
    """Interface of Rubik's Cube Model."""

    def draw(self, print_emojis: bool) -> None:
        """Draws the cube.

        Args:
            print_emojis: if True, prints emojis; otherwise, prints letters representing colors
        """
        pass

    def move(self, turns: str) -> None:
        """Makes a sequence of turns.

        .. code-block:: text

            Allowed turns:
                 F: Front;  B: Back;  U: Up;  D: Down;  L: Left;  R: Right;
                 f: Front 2 layers;  b: Back 2 layers;
                 u: Up 2 layers;  d: Down 2 layers;
                 l: Left 2 layers;  r: Right 2 layers;
                 x: rotation;  y: rotation;  z: rotation;
                 M: Middle;  E: Equator;  S: Standing
            Allowed modifiers:
                 p: counterclockwise; ′: counterclockwise; 2: make 2 turns

        Args:
            turns: sequence of letters denoting the movements/turns to be executed, according to Singmaster notation.
                If followed by a 'p' or a prime symbol (′), turn it anticlockwise; otherwise, turn it clockwise.
                If followed by a '2', execute the operation twice.

        Raises:
            ValueError: Unrecognized move is requested

        Examples:
            >>> valid_turns = ["F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"]
            >>> invalid_turns = ["F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"]
            >>> for turn in valid_turns:
            ...     cube.move(turn)
        """
        pass

    def scramble(self, steps: int, wide_moves: bool, slice_moves: bool, cube_rotations: bool) -> str:
        """Scrambles the cube.

        Args:
            steps: number of random moves to be executed on the cube.
            wide_moves: allow moves f-b-u-d-l-r to be executed.
            slice_moves: allow moves M-E-S to be executed.
            cube_rotations: allow rotations x-y-z to be executed.

        Return:
            Sequence of scrambles executed on the cube
        """
        pass

    def is_solved(self) -> bool:
        """Checks if the cube is solved."""
        pass

    def get_color(self, position: str) -> str:
        """Gets the color in a given position, according to Singmaster notation.

        .. code-block:: text

            Positions, according to Singmaster notation:

                      11 12 13
                      14 U  16
                      17 18 19
            21 22 23  01 02 03 41 42 43  51 52 53
            24 L  26  04 F  06 44 R  46  54 B  56
            27 28 29  07 08 09 47 48 49  57 58 59
                      31 32 33
                      34 D  36
                      37 38 39

        Args:
            position: any valid position; all valid positions are listed above

        Returns:
            Color contained in the position. It can be 'G', 'R', 'O', 'W', 'B' or 'Y'
        """
        pass

    def find_position(self, *colors: str) -> str:
        """Finds position of a piece in the cube.

        Args:
            *colors: 1 to 3 elements, with the colors representing piece to be found: 'G', 'R', 'O', 'W', 'B', 'Y'

        Returns:
            Position of that piece. It can be (center) F, B, U, D, R, L; (edge) FU, FD, FR, FL, UF, DF, RF, LF, BU,
            BD, BR, BL, UB, DB, RB, LB, RU, UR, UL, LU, LD, DL, DR, RD; (corner) FUR, FRU, URF, UFR, RUF, RFU, FUL,
            FLU, LUF, LFU, ULF, UFL, BUR, BRU, URB, UBR, RBU, RUB, BUL, BLU, LUB, LBU, UBL, ULB, FDL, FLD, LDF, LFD,
            DFL, DLF, FDR, FRD, RDF, RFD, DFR, DRF, BDL, BLD, LDB, LBD, DBL, DLB, BDR, BRD, RBD, RDB, DBR, DRB.

        Raise:
            ValueError: if colors not found
        """
        pass

    def solve(self, method: str, change_state: bool) -> str:
        """Solves the cube.

        Args:
            method: method to be used to solve the cube. It can be 'lbl' or 'kociemba'
            change_state: if True, changes the cube state to the solved state. Otherwise, just returns the solution.

        Returns:
            list of moves that solve the cube; None if the cube is not solvable
        """
        pass

    def get_size(self) -> int:
        """Returns the size of the cube."""
        pass

    def set_color(self, position: str, color: str) -> None:
        """Sets a color on the cube.

        Args:
            position: position on the cube according to Singmaster notation. The position can be  'F', 'B', 'U', 'D',
                'L', 'R', '01', ..., '04', '06', ..., '09','11', ..., or '59'
            color: one of the 6 standard colors on the cube. The color can be 'G', 'R', 'O', 'W', 'B', or 'Y'
        """
        pass

    def set_all_colors(self, color_dict: dict) -> None:
        """Sets all colors on the cube.

        Args:
            color_dict: dictionary that sets colors on all 54 cube positions;

                         keys: 54 (6 + 6*8) positions, according to Singmaster notation:
                               'F', 'B', 'U', 'D', 'L', 'R', '01', ..., '04', '06', ..., '09','11', ..., '59'
                         values: one of the 6 standard colors on the cube:
                                 'G', 'R', 'O', 'W', 'B', 'Y'
        """
        pass

    def is_solvable(self) -> bool:
        """Checks if the cube is solvable."""
        pass
