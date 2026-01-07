import math

def quadratic_roots_real(a, b, c):
    if a == 0:
        raise ValueError("ضریب a نباید صفر باشد")

    delta = b**2 - 4*a*c

    if delta < 0:
        return None  # ریشه حقیقی ندارد

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

print(quadratic_roots_real(1, -3, 2))