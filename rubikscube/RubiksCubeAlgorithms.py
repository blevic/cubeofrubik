from .RubiksCubeInterface import RubiksCubeInterface


def base_layer(cube: RubiksCubeInterface) -> str:
    f_color = cube.get_color('F')
    r_color = cube.get_color('R')
    b_color = cube.get_color('B')
    l_color = cube.get_color('L')
    d_color = cube.get_color('D')

    def base_cross(cube: RubiksCubeInterface) -> str:
        base_moves = ""

        f_map = {
            'FU': "FR′D′",
            'FD': "FLD",
            'FR': "R′D′",
            'FL': "LD",
            'UF': "F2",
            'DF': "",
            'RF': "F",
            'LF': "F′",
            'BU': "UR′F",
            'BD': "DL′F′",
            'BR': "RD′",
            'BL': "L′D",
            'UB': "U2F2",
            'DB': "D2",
            'RB': "R2F",
            'LB': "L2F′",
            'RU': "R′F",
            'UR': "UF2",
            'UL': "U′F2",
            'LU': "LF′",
            'LD': "L′F′",
            'DL': "D",
            'DR': "D′",
            'RD': "RF"
        }
        piece = cube.find_position(d_color, f_color)
        moves = f_map[piece]
        cube.move(moves)
        base_moves += moves

        r_map = {
            'FU': "FR′F′",
            'FR': "R′",
            'FL': "F2R′F2",
            'UF': "U′R2",
            'RF': "F′U′FR2",
            'LF': "F′DF",
            'BU': "B′R",
            'BD': "BR",
            'BR': "R",
            'BL': "B2R",
            'UB': "UR2",
            'DB': "BDB′D′",
            'RB': "DB′D′",
            'LB': "DBD′",
            'RU': "U′B′R",
            'UR': "R2",
            'UL': "U2R2",
            'LU': "U′FR′F′",
            'LD': "L′F′DF",
            'DL': "FD2F′",
            'DR': "",
            'RD': "RFDF′"
        }
        piece = cube.find_position(d_color, r_color)
        moves = r_map[piece]
        cube.move(moves)
        base_moves += moves

        b_map = {
            'FU': "UL′B",
            'FR': "D′R′D",
            'FL': "DLD′",
            'UF': "U2B2",
            'RF': "R2B′R2",
            'LF': "D2F′D2",
            'BU': "B′D′RD",
            'BD': "BD′RD",
            'BR': "D′RD",
            'BL': "DL′D′",
            'UB': "B2",
            'DB': "",
            'RB': "B′",
            'LB': "B",
            'RU': "RB′R′",
            'UR': "U′B2",
            'UL': "UB2",
            'LU': "L′B",
            'LD': "LB",
            'DL': "L′DLD′"
        }
        piece = cube.find_position(d_color, b_color)
        moves = b_map[piece]
        cube.move(moves)
        base_moves += moves

        l_map = {
            'FU': "F′LF",
            'FR': "D2R′D2",
            'FL': "L",
            'UF': "UL2",
            'RF': "DFD′",
            'LF': "DF′D′",
            'BU': "U2F′LF",
            'BR': "D2RD2",
            'BL': "L′",
            'UB': "U′L2",
            'RB': "D′B′D",
            'LB': "D′BD",
            'RU': "UF′LF",
            'UR': "U2L2",
            'UL': "L2",
            'LU': "U′F′LF",
            'LD': "L′DF′D′",
            'DL': ""
        }
        piece = cube.find_position(d_color, l_color)
        moves = l_map[piece]
        cube.move(moves)
        base_moves += moves

        return base_moves

    def base_corners(cube: RubiksCubeInterface) -> str:
        corners_moves = ""

        dfr_map = {
            'BDL': "LU2L′",
            'BDR': "BUB′",
            'BLU': "U2",
            'BRU': "U",
            'DFL': "FU′F′U′",
            'DFR': "",
            'FLU': "U′",
            'FRU': ""
        }
        piece = cube.find_position(d_color, f_color, r_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dfr_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        dfr_elevator_map = {
            'DFR': "",
            'FRD': "F′U′FUF′U′F",
            'RDF': "RUR′U′RUR′",
            'URF': "RU2R′U′RUR′",
            'RFU': "RUR′",
            'FUR': "F′U′F"
        }

        position = cube.find_position(d_color, f_color, r_color)
        moves = dfr_elevator_map[position]
        cube.move(moves)
        corners_moves += moves

        drb_map = {
            'BDL': "LUL′",
            'BDR': "",
            'BLU': "U",
            'BRU': "",
            'DFL': "FU2F′",
            'FLU': "U2",
            'FRU': "U′"
        }
        piece = cube.find_position(d_color, r_color, b_color)
        sorted_piece = ''.join(sorted(piece))
        moves = drb_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        if cube.find_position(d_color, r_color, b_color) != 'DRB':
            cube.move("y")
            corners_moves += "y"
            position = cube.find_position(d_color, r_color, b_color)
            moves = dfr_elevator_map[position] + "y′"
            cube.move(moves)
            corners_moves += moves

        dbl_map = {
            'BDL': "",
            'BLU': "",
            'BRU': "U′",
            'DFL': "FUF′",
            'FLU': "U",
            'FRU': "U2"
        }
        piece = cube.find_position(d_color, b_color, l_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dbl_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        if cube.find_position(d_color, b_color, l_color) != 'DBL':
            cube.move("y2")
            corners_moves += "y2"
            position = cube.find_position(d_color, b_color, l_color)
            moves = dfr_elevator_map[position] + "y2"
            cube.move(moves)
            corners_moves += moves

        dlf_map = {
            'BLU': "U′",
            'BRU': "U2",
            'DFL': "",
            'FLU': "",
            'FRU': "U"
        }
        piece = cube.find_position(d_color, l_color, f_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dlf_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        if cube.find_position(d_color, l_color, f_color) != 'DLF':
            cube.move("y′")
            corners_moves += "y′"
            position = cube.find_position(d_color, l_color, f_color)
            moves = dfr_elevator_map[position] + "y"
            cube.move(moves)
            corners_moves += moves

        return corners_moves

    moves_sequence = base_cross(cube)
    moves_sequence += base_corners(cube)

    return moves_sequence


def second_layer(cube: RubiksCubeInterface) -> str:
    R_INSERT = "RUR′U′F′U′F"
    L_INSERT = "F′U′FURUR′"
    f_color = cube.get_color('F')
    r_color = cube.get_color('R')
    b_color = cube.get_color('B')
    l_color = cube.get_color('L')

    second_layer_moves = ""

    fr_map = {
        'UF': "U2" + L_INSERT,
        'UR': "U′" + L_INSERT,
        'UB': L_INSERT,
        'UL': "U" + L_INSERT,
        'FU': "U" + R_INSERT,
        'RU': "U2" + R_INSERT,
        'BU': "U′" + R_INSERT,
        'LU': R_INSERT,
        'FR': "",
        'RF': R_INSERT,
        'RB': "y" + R_INSERT + "y′",
        'BR': "y" + R_INSERT + "y′",
        'BL': "y2" + R_INSERT + "y2",
        'LB': "y2" + R_INSERT + "y2",
        'LF': "y′" + R_INSERT + "y",
        'FL': "y′" + R_INSERT + "y"
    }

    for _ in range(2):
        position = cube.find_position(f_color, r_color)
        moves = fr_map[position]
        cube.move(moves)
        second_layer_moves += moves

    rb_map = {
        'UF': "yU" + L_INSERT + "y′",
        'UR': "yU2" + L_INSERT + "y′",
        'UB': "yU′" + L_INSERT + "y′",
        'UL': "y" + L_INSERT + "y′",
        'FU': "y" + R_INSERT + "y′",
        'RU': "yU" + R_INSERT + "y′",
        'BU': "yU2" + R_INSERT + "y′",
        'LU': "yU′" + R_INSERT + "y′",
        'RB': "",
        'BR': "y" + R_INSERT + "y′",
        'BL': "y2" + R_INSERT + "y2",
        'LB': "y2" + R_INSERT + "y2",
        'LF': "y′" + R_INSERT + "y",
        'FL': "y′" + R_INSERT + "y"
    }

    for _ in range(2):
        position = cube.find_position(r_color, b_color)
        moves = rb_map[position]
        cube.move(moves)
        second_layer_moves += moves

    bl_map = {
        'UF': "y2" + L_INSERT + "y2",
        'UR': "y2U" + L_INSERT + "y2",
        'UB': "y2U2" + L_INSERT + "y2",
        'UL': "y2U′" + L_INSERT + "y2",
        'FU': "y2U′" + R_INSERT + "y2",
        'RU': "y2" + R_INSERT + "y2",
        'BU': "y2U" + R_INSERT + "y2",
        'LU': "y2U2" + R_INSERT + "y2",
        'BL': "",
        'LB': "y2" + R_INSERT + "y2",
        'LF': "y′" + R_INSERT + "y",
        'FL': "y′" + R_INSERT + "y"
    }

    for _ in range(2):
        position = cube.find_position(b_color, l_color)
        moves = bl_map[position]
        cube.move(moves)
        second_layer_moves += moves

    lf_map = {
        'UF': "y′U′" + L_INSERT + "y",
        'UR': "y′" + L_INSERT + "y",
        'UB': "y′U" + L_INSERT + "y",
        'UL': "y′U2" + L_INSERT + "y",
        'FU': "y′U2" + R_INSERT + "y",
        'RU': "y′U′" + R_INSERT + "y",
        'BU': "y′" + R_INSERT + "y",
        'LU': "y′U" + R_INSERT + "y",
        'LF': "",
        'FL': "y′" + R_INSERT + "y"
    }

    for _ in range(2):
        position = cube.find_position(l_color, f_color)
        moves = lf_map[position]
        cube.move(moves)
        second_layer_moves += moves

    return second_layer_moves


def top_layer(cube: RubiksCubeInterface) -> str:
    def top_cross(cube: RubiksCubeInterface) -> str:
        top_cross_moves = ""
        F_SWITCH = "FRUR′U′F′"

        def top_cross_done(c):
            return c.get_color('U') == c.get_color('12') == c.get_color('14') == c.get_color('16') == c.get_color('18')

        def just_top(c):
            return c.get_color('U') == c.get_color('02') == c.get_color('22') == c.get_color('42') == c.get_color('52')

        def horizontal_line(c):
            return not top_cross_done(c) and (
                        c.get_color('12') == c.get_color('18') or c.get_color('14') == c.get_color('16'))

        def l_shape(c):
            return not top_cross_done(c) and not just_top(c) and not horizontal_line(c)

        for _ in range(2):
            if top_cross_done(cube):
                break

            if just_top(cube):
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if l_shape(cube):
                for i in range(4):
                    if cube.get_color('12') == cube.get_color('14'):
                        break
                    cube.move("U")
                    top_cross_moves += "U"
                else:
                    raise ValueError("Expected l shape to be found")
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if horizontal_line(cube):
                if cube.get_color('12') == cube.get_color('18'):
                    cube.move("U")
                    top_cross_moves += "U"
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH
        else:
            raise ValueError("Expected top cross to be done")

        return top_cross_moves

    def cross_color_matching(cube: RubiksCubeInterface) -> str:
        cross_color_matching_moves = ""

        def f_match(c):
            return c.get_color('F') == c.get_color('02')

        def r_match(c):
            return c.get_color('R') == c.get_color('42')

        def b_match(c):
            return c.get_color('B') == c.get_color('52')

        def l_match(c):
            return c.get_color('L') == c.get_color('22')

        def count_matched(c):
            return sum([f_match(c), r_match(c), b_match(c), l_match(c)])

        def match_across(c):
            return count_matched(c) == 2 and (f_match(c) and b_match(c)) or (r_match(c) and l_match(c))

        def match_l(c):
            return count_matched(c) == 2 and not match_across(c)

        def matched_l_position(c):
            if not match_l(c):
                raise ValueError("Incorrect use of matched_l_position: no l matched")
            if f_match(c) and r_match(c):
                return 'FR'
            if r_match(c) and b_match(c):
                return 'RB'
            if b_match(c) and l_match(c):
                return 'BL'
            if l_match(c) and f_match(c):
                return 'LF'
            raise ValueError("No L match found")

        if count_matched(cube) == 4:
            return ""

        candidate_moves = ""
        for _ in range(4):
            candidate_moves += "U"
            cube.move("U")
            if count_matched(cube) == 4:
                return candidate_moves

        CROSS_COLOR_MATCH_SEQ = "RUR′URU2R′"

        # two colors are matchable
        for _ in range(4):
            if count_matched(cube) == 2:
                break
            cross_color_matching_moves += "U"
            cube.move("U")
        else:
            ValueError("Expected two colors to match")

        if match_across(cube):
            cross_color_matching_moves += CROSS_COLOR_MATCH_SEQ
            cube.move(CROSS_COLOR_MATCH_SEQ)

        for _ in range(4):
            if count_matched(cube) == 2:
                break
            cross_color_matching_moves += "U"
            cube.move("U")
        else:
            ValueError("Expected two colors to match")

        matched_l_position_map = {
            'FR': "y′" + CROSS_COLOR_MATCH_SEQ + "y",
            'RB': CROSS_COLOR_MATCH_SEQ,
            'BL': "y" + CROSS_COLOR_MATCH_SEQ + "y′",
            'LF': "y2" + CROSS_COLOR_MATCH_SEQ + "y2"
        }

        if not match_l(cube):
            raise ValueError("Expected L matched by here")

        moves = matched_l_position_map[matched_l_position(cube)]
        cross_color_matching_moves += moves
        cube.move(moves)

        if count_matched(cube) == 4:
            return ""

        for _ in range(4):
            cross_color_matching_moves += "U"
            cube.move("U")
            if count_matched(cube) == 4:
                return cross_color_matching_moves

        raise ValueError("Expected top cross to be color matched by here")

    def corner_matching(cube: RubiksCubeInterface) -> str:
        corner_matching_moves = ""
        SWAP_CORNERS = "URU′L′UR′U′L"

        def number_matching_corners(c):
            return sum([
                ''.join(sorted(c.find_position(c.get_color('B'), c.get_color('L'), c.get_color('U')))) == 'BLU',
                ''.join(sorted(c.find_position(c.get_color('B'), c.get_color('R'), c.get_color('U')))) == 'BRU',
                ''.join(sorted(c.find_position(c.get_color('F'), c.get_color('L'), c.get_color('U')))) == 'FLU',
                ''.join(sorted(c.find_position(c.get_color('F'), c.get_color('R'), c.get_color('U')))) == 'FRU'
            ])

        def matching_up_corner_position(c):
            if number_matching_corners(c) != 1:
                raise ValueError("Function matching_up_corner_position is valid only for 1 matching top corner")
            if ''.join(sorted(c.find_position(c.get_color('B'), c.get_color('L'), c.get_color('U')))) == 'BLU':
                return 'BL'
            if ''.join(sorted(c.find_position(c.get_color('B'), c.get_color('R'), c.get_color('U')))) == 'BRU':
                return 'BR'
            if ''.join(sorted(c.find_position(c.get_color('F'), c.get_color('L'), c.get_color('U')))) == 'FLU':
                return 'FL'
            if ''.join(sorted(c.find_position(c.get_color('F'), c.get_color('R'), c.get_color('U')))) == 'FRU':
                return 'FR'
            raise ValueError("Expected any top position to be found")

        if number_matching_corners(cube) == 4:
            return ""

        if number_matching_corners(cube) == 0:
            corner_matching_moves += SWAP_CORNERS
            cube.move(SWAP_CORNERS)

        if number_matching_corners(cube) != 1:
            raise ValueError("Expected 1 matching top corner")

        matching_up_corner = matching_up_corner_position(cube)

        rotation_map = {
            'BL': ("y2", "y2"),
            'BR': ("y", "y′"),
            'FL': ("y′", "y"),
            'FR': ("", "")
        }

        pre_rotation, post_rotation = rotation_map[matching_up_corner]

        corner_matching_moves += pre_rotation
        cube.move(pre_rotation)
        for _ in range(2):
            corner_matching_moves += SWAP_CORNERS
            cube.move(SWAP_CORNERS)

            if number_matching_corners(cube) == 4:
                corner_matching_moves += post_rotation
                cube.move(post_rotation)
                return corner_matching_moves

        raise ValueError("Expected corners to be matched by here")

    def final_round(cube: RubiksCubeInterface) -> str:
        final_round_moves = ""
        R_MOVES = "RUR′U′"

        if cube.is_solved():
            return ""

        final_round_moves += "x2"
        cube.move("x2")

        for _ in range(5):
            if cube.is_solved():
                break
            for i in range(6):
                if cube.get_color('33') == cube.get_color('D'):
                    break
                final_round_moves += R_MOVES
                cube.move(R_MOVES)
            else:
                raise ValueError("Expected bottom piece to be solved")
            final_round_moves += "D"
            cube.move("D")
        else:
            raise ValueError("Expected cube to be solved")

        return final_round_moves

    moves = top_cross(cube)
    moves += cross_color_matching(cube)
    moves += corner_matching(cube)
    moves += final_round(cube)

    return moves


def layer_by_layer(cube: RubiksCubeInterface) -> str:
    if cube.is_solved():
        return ""

    if cube.get_size() != 3:
        raise ValueError("LBL algorithm is valid for cube size 3 only.")

    moves = base_layer(cube)
    moves += second_layer(cube)
    moves += top_layer(cube)

    return moves
