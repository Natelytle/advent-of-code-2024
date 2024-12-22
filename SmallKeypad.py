
import itertools


class SmallKeypad:
    def __init__(self, aux_keypad, name="bruh"):
        self.aux_keypad = aux_keypad
        self.name = name

    total_combination = []

    move_left_position = (0, 0)
    move_right_position = (2, 0)
    move_up_position = (1, 1)
    move_down_position = (1, 0)
    activate_position = (2, 1)

    xPosition = 2
    yPosition = 1

    xPositionCache = 2
    yPositionCache = 1

    def find_shortest_path(self, target_x_position, target_y_position):
        if target_x_position < 0 or target_x_position > 2:
            raise ValueError(f"{target_x_position} outside of range 0, 2")
        if target_y_position < 0 or target_y_position > 1:
            raise ValueError(f"{target_y_position} outside of range 0, 1")
        if target_x_position == 0 and target_y_position == 1:
            return 999999999

        is_right = target_x_position > self.xPositionCache
        is_up = target_y_position > self.yPositionCache

        sideways_movement = abs(target_x_position - self.xPositionCache)
        vertical_movement = abs(target_y_position - self.yPositionCache)

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

        if self.aux_keypad is not None:
            moves_combinations = itertools.combinations(moves, len(moves))

            total_moves = 9999

            best_combination = ()

            for combination in moves_combinations:
                self.aux_keypad.reset_cache()

                combination += ("activate",)

                current_moves = 0

                if self.xPositionCache == 1 and self.yPositionCache == 1 and combination[0] == "left":
                    current_moves = 99999
                if self.xPositionCache == 2 and self.yPositionCache == 1 and combination[0] == "left" and combination[1] == "left":
                    current_moves = 99999
                if self.xPositionCache == 0 and self.yPositionCache == 0 and combination[0] == "up":
                    current_moves = 99999

                for combination_moves in combination:
                    current_moves += self.aux_keypad.find_shortest_path_relative(combination_moves)

                if current_moves < total_moves:
                    best_combination = combination

                total_moves = min(current_moves, total_moves)

            self.xPositionCache = target_x_position
            self.yPositionCache = target_y_position

            self.total_combination.extend(list(best_combination))

            return total_moves

        return 1

    def find_shortest_path_relative(self, direction):
        if direction == "left":
            return self.find_shortest_path(*self.move_left_position)
        elif direction == "right":
            return self.find_shortest_path(*self.move_right_position)
        elif direction == "up":
            return self.find_shortest_path(*self.move_up_position)
        elif direction == "down":
            return self.find_shortest_path(*self.move_down_position)
        elif direction == "activate":
            return self.find_shortest_path(*self.activate_position)

    def reset_cache(self):
        self.xPositionCache = self.xPosition
        self.yPositionCache = self.yPosition

