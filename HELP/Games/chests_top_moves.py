def top_attack(x, y, p, q):
  """
  Определя дали поето с координати x,y  от шахматната дъска с размери n - реда и  n - колони n>=8 се бие от фигура разположена в поле с координати p,q  ако фигурата е ТОП.

  Args:
    x: Координата x на поета.
    y: Координата y на поета.
    p: Координата x на фигурата.
    q: Координата y на фигурата.

  Returns:
    True, ако поето се бие, False, ако не се бие.
  """

  if x < 0 or x > 8:
    raise ValueError("Невалидна координата x.")
  if y < 0 or y > 8:
    raise ValueError("Невалидна координата y.")
  if p < 0 or p > 8:
    raise ValueError("Невалидна координата p.")
  if q < 0 or q > 8:
    raise ValueError("Невалидна координата q.")

  if x == p and y == q:
    return True
  elif x == p or y == q:
    return True
  elif x - y == p - q or x + y == p + q:
    return True
  else:
    return False


if __name__ == "__main__":
  x = int(input("Въведете x: "))
  y = int(input("Въведете y: "))
  p = int(input("Въведете p: "))
  q = int(input("Въведете q: "))
  try:
    print(top_attack(x, y, p, q))
  except ValueError as e:
    print(e)
