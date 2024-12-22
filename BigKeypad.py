import itertools


class BigKeypad:
    def __init__(self, aux_keypad):
        self.aux_keypad = aux_keypad

    xPosition = 2
    yPosition = 0

    def find_shortest_path(self, target_x_position, target_y_position):
        if target_x_position < 0 or target_x_position > 2:
            raise ValueError(f"{target_x_position} outside of range 0, 2")
        if target_y_position < 0 or target_y_position > 3:
            raise ValueError(f"{target_y_position} outside of range 0, 3")
        if target_x_position == 0 and target_y_position == 0:
            return 999999999

        is_right = target_x_position > self.xPosition
        is_up = target_y_position > self.yPosition

        sideways_movement = abs(target_x_position - self.xPosition)
        vertical_movement = abs(target_y_position - self.yPosition)

        moves = []

        sideways_moves = 0
        vertical_moves = 0

        while sideways_moves < sideways_movement:
            if is_right:
                moves.append("right")
            else:
                moves.append("left")

            sideways_moves += 1

        while vertical_moves < vertical_movement:
            if is_up:
                moves.append("up")
            else:
                moves.append("down")

            vertical_moves += 1

        moves_combinations = itertools.combinations(moves, len(moves))
        total_moves = 9999

        if self.aux_keypad is not None:
            moves_combinations = itertools.combinations(moves, len(moves))
            total_moves = 9999

            for combination in moves_combinations:
                self.aux_keypad.reset_cache()

                combination += ("activate",)

                current_moves = 0

                for combination_moves in combination:
                    current_moves += self.aux_keypad.find_shortest_path_relative(combination_moves)

                total_moves = min(current_moves, total_moves)

            self.xPosition = target_x_position
            self.yPosition = target_y_position

            return total_moves

        # if human piloted each counts as one move
        self.xPosition = target_x_position
        self.yPosition = target_y_position

        # +1 for the button press
        return 1