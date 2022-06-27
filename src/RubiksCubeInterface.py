class RubiksCubeInterface:
    """Interface of Rubik's Cube Model"""

    def draw(self) -> None:
        """Draw the cube"""
        pass

    def move(self, turns: str) -> None:
        """
        Make a sequence of moves

            Args:
                turns: sequence of letters denoting the movements/turns to be executed, according to Singmaster notation
                    Allowed letters:
                        F: Front;  B: Back;  U: Up;  D: Down;  L: Left;  R: Right;
                        f: Front 2 layers;  b: Back 2 layers;
                        u: Up 2 layers;  d: Down 2 layers;
                        l: Left 2 layers;  r: Right 2 layers;
                        x: rotation;  y: rotation;  z: rotation;
                        M: Middle;  E: Equator;  S: Standing

                    If followed by a p or a prime symbol (′), turn it anticlockwise; otherwise, turn it clockwise.
                    If followed by a 2, execute the operation twice.

                    Examples:
                        Valid:   "F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"
                        Invalid: "F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"

            Raises:
                ValueError: Unrecognized move is requested
        """
        pass

    def scramble(self, steps: int, wide_moves: bool, slice_moves: bool, cube_rotations: bool) -> str:
        """
        Scramble the cube

            Args:
                steps: number of random moves to be executed on the cube
                wide_moves: allow moves f-b-u-d-l-r to be executed
                slice_moves: allow moves M-E-S to be executed
                cube_rotations: allow rotations x-y-z to be executed

            Return:
                Sequence of scrambles executed on the cube
        """
        pass

    def is_solved(self) -> bool:
        """Respond whether the cube is solved"""
        pass

    def get_color(self, position: str) -> str:
        """
        Get color in a given position, according to Singmaster notation:

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

            Return:
                color contained in the position:
                    'G', 'R', 'O', 'W', 'B', 'Y'
        """
        pass

    def find_position(self, *colors: str) -> str:
        """
        Find position of a piece in the cube

        Args:
            *colors: 1 to 3 elements, with the colors representing piece to be found:
                     'G', 'R', 'O', 'W', 'B', 'Y'

        Return:
            position of that piece:
                1 -> F, B, U, D, R, L
                2 -> FU, FD, FR, FL, UF, DF, RF, LF, BU, BD, BR, BL, UB, DB, RB, LB, RU, UR, UL, LU, LD, DL, DR, RD
                3 -> FUR, FRU, URF, UFR, RUF, RFU, FUL, FLU, LUF, LFU, ULF, UFL,
                     BUR, BRU, URB, UBR, RBU, RUB, BUL, BLU, LUB, LBU, UBL, ULB,
                     FDL, FLD, LDF, LFD, DFL, DLF, FDR, FRD, RDF, RFD, DFR, DRF,
                     BDL, BLD, LDB, LBD, DBL, DLB, BDR, BRD, RBD, RDB, DBR, DRB

        Raise:
            ValueError if colors not found
        """
        pass

    def solve(self) -> str:
        """Return list of steps to solve the cube"""
        pass

    def get_size(self) -> int:
        """Return the cube's size"""
        pass

    def set_color(self, position: str, color: str) -> None:
        """
        Sets a color on the cube

        Args:
            position: position on the cube according to Singmaster notation:
                      'F', 'B', 'U', 'D', 'L', 'R', '01', ..., '04', '06', ..., '09','11', ..., '59'
            color: one of the 6 standard colors on the cube:
                      'G', 'R', 'O', 'W', 'B', 'Y'
        """
        pass

    def set_all_colors(self, color_dict: dict) -> None:
        """
        Sets the colors on the cube

        Args:
            color_dict: dictionary that sets colors on all 54 cube positions;
                         keys: 54 (6 + 6*8) positions, according to Singmaster notation:
                               'F', 'B', 'U', 'D', 'L', 'R', '01', ..., '04', '06', ..., '09','11', ..., '59'
                         values: one of the 6 standard colors on the cube:
                                 'G', 'R', 'O', 'W', 'B', 'Y'
        """
        pass

    def is_solvable(self) -> bool:
        """
        Check if the cube is solvable

        Return:
            True if the cube is solvable, False otherwise
        """
        pass
