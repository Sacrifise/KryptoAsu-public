from math import gcd

def extended_gcd(a, b):
    """Расширенный алгоритм Евклида для нахождения НОД и коэффициентов Безу."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modular_inverse(a, m):
    """Находит обратный элемент к a по модулю m, если он существует."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  
    else:
        return x % m

def solve_congruence(elements):
    a, b, m = elements[0], elements[1], elements[2]
    """Решает уравнение сравнения a*x ≡ b (mod m). """
    d = gcd(a, m)
    if b % d != 0:
        return None  
    a_reduced = a // d
    b_reduced = b // d
    m_reduced = m // d

    inv = modular_inverse(a_reduced, m_reduced)
    if inv is None:
        return None  

    x0 = (inv * b_reduced) % m_reduced

    solutions = [(x0 + k * m_reduced) % m for k in range(d)]
    return solutions
