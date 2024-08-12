import math

def sum_of_square_roots(k, n):

  """
  Пресмята сумата на квадратните корени от числата от k до n.

  Args:
    k: Начално число.
    n: Крайно число.

  Returns:
    Сумата на квадратните корени от числата от k до n.
  """

  return sum(math.sqrt(i) for i in range(k, n + 1))

if __name__ == "__main__":
  k = int(input("Въведете начално число: "))
  n = int(input("Въведете крайно число: "))
  sum = sum_of_square_roots(k, n)
  print(f"Сумата на квадратните корени от числата от {k} до {n} е {sum:.2f}")
