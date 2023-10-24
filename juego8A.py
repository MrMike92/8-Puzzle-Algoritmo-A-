import heapq

class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def print_board(self, board):
        for row in board:
            print(" ".join(map(str, row)))
        print()

    def swap_position(self, board, number):
        for i in range(3):
            for j in range(3):
                if board[i][j] == number:
                    for k in range(3):
                        for l in range(3):
                            if board[k][l] == 0:
                                board[i][j], board[k][l] = board[k][l], board[i][j]
                                return

    def get_valid_moves_in_order(self, board):
        valid_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    if j > 0:
                        valid_moves.append((i, j - 1, "Izquierda "))
                    if i > 0:
                        valid_moves.append((i - 1, j, "Arriba "))
                    if j < 2:
                        valid_moves.append((i, j + 1, "Derecha "))
                    if i < 2:
                        valid_moves.append((i + 1, j, "Abajo "))

        valid_moves.sort(key=lambda x: ("Arriba ", "Abajo ", "Izquierda ", "Derecha ").index(x[2]))

        return valid_moves

    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    value = state[i][j]
                    goal_position = [(x, y) for x in range(3) for y in range(3) if self.goal_state[x][y] == value][0]
                    distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
        return distance

    def solve(self):
        f_n_queue = [(self.manhattan_distance(self.goal_state), self.initial_state, 1, 0, "")]
        move_number = 2
        last_board = None  # Variable para rastrear el último tablero visitado
        visited = set()

        while f_n_queue:
            _, state, padre, depth, move = heapq.heappop(f_n_queue)
            visited.add(tuple(map(tuple, state)))

            if state == self.goal_state:
                return (g_n, padre, move, h_n, f_n)

            valid_moves = self.get_valid_moves_in_order(state)

            for i, j, move_str in valid_moves:
                new_state = [row[:] for row in state]
                self.swap_position(new_state, state[i][j])
                new_move = move + move_str
                new_depth = depth + 1
                g_n = new_depth
                if new_state != self.goal_state:
                    h_n = self.manhattan_distance(new_state)
                else:
                    h_n = 0
                f_n = g_n + h_n
                new_node = (f_n, new_state, move_number, new_depth, new_move)
                if tuple(map(tuple, new_state)) not in visited:
                    heapq.heappush(f_n_queue, new_node)
                    visited.add(tuple(map(tuple, new_state)))
                    print(f"({move_number}, {padre}, g(n)={g_n}, h(n)={h_n}, f(n)={f_n}, {move_str})")
                    self.print_board(new_state)
                    last_board = new_state  # Actualiza el último tablero visitado
                    move_number += 1

        if last_board is not None:
            print("\nÚltimo tablero visitado:")
            self.print_board(last_board)

        return None

if __name__ == "__main__":
    initial_board = [[2, 8, 3], [0, 1, 4], [7, 6, 5]]
    goal_board = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    puzzle = Puzzle(initial_board, goal_board)
    result = puzzle.solve()

    if result:
        g_n, move_number, moves, h_n, f_n = result[0], result[1], result[2], result[3], result[4]
        print("¡Solución encontrada!\n")
        print(f"Movimientos realizados: {moves}")
        print("Número de movimiento realizado:", move_number)
        print("g(n) = ", g_n)
        print("h(n) = ", h_n)
        print("f(n) = ", f_n)
        print("Tablero inicial:")
        puzzle.print_board(initial_board)
        print("Tablero objetivo:")
        puzzle.print_board(goal_board)
    else:
        print("No se encontró una solución.\n")