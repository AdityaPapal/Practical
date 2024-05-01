class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0]*n for _ in range(n)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check if there is any queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_backtracking(self, row):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_backtracking(row + 1):
                    self.board[row][col] = 0
                else:
                    self.board[row][col] = 0

        return False

    def solve_branch_and_bound(self, row):
        if row == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True

        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_branch_and_bound(row + 1):
                    return True
                self.board[row][col] = 0

        return False

# Example usage:
n = 4
queens = NQueens(n)

# Backtracking
queens.solve_backtracking(0)
print("Solutions using Backtracking:")
for solution in queens.solutions:
    print(solution)
queens.solutions = []

# Branch and Bound
queens.solve_branch_and_bound(0)
print("\nSolutions using Branch and Bound:")
for solution in queens.solutions:
    print(solution)
