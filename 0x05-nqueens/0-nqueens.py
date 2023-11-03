import sys

def nqueens(n):
  """
  Solves the N queens problem.

  Args:
    n: The number of queens to place.

  Returns:
    A list of lists, where each sublist represents a solution to the problem.
  """

  def is_safe(row, col, queens):
    """
    Checks if placing a queen at (row, col) is safe.

    Args:
      row: The row to place the queen at.
      col: The column to place the queen at.
      queens: A list of lists, where each sublist represents a solution to the problem so far.

    Returns:
      True if placing a queen at (row, col) is safe, False otherwise.
    """

    for i in range(len(queens)):
      if queens[i][0] == row or queens[i][1] == col or abs(queens[i][0] - row) == abs(queens[i][1] - col):
        return False
    return True

  def solve(n, queens):
    """
    Solves the N queens problem recursively.

    Args:
      n: The number of queens to place.
      queens: A list of lists, where each sublist represents a solution to the problem so far.

    Returns:
      A list of lists, where each sublist represents a solution to the problem.
    """

    if n == len(queens):
      return [queens]

    solutions = []
    for col in range(n):
      if is_safe(len(queens), col, queens):
        solutions.extend(solve(n, queens + [[len(queens), col]]))

    return solutions

  return solve(n, [])

def main():
  """
  The main function.
  """

  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

  n = sys.argv[1]
  try:
    n = int(n)
  except ValueError:
    print("N must be a number")
    sys.exit(1)

  if n < 4:
    print("N must be at least 4")
    sys.exit(1)

  solutions = nqueens(n)
  for solution in solutions:
    print(" ".join([str(i) for i in solution]))

if __name__ == "__main__":
  main()
