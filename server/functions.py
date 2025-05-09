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
        solution = f'С помощью расширенного алгоритма Евклида найдем НОД(a,b) и коэффициенты Безу. НОД(a,b)={g}, x={x}, y={_}'
        return x % m

def solve_congruence(elements, solution: str):
    a, b, m = elements[0], elements[1], elements[2]
    """Решает уравнение сравнения a*x ≡ b (mod m). """
    d = gcd(a, m)
    if b % d != 0:
        solution=f"Так как НОД({a},{m}=d, не делит {b}, то по теореме о существовании решений линейного сравнения по модулю, решения нет."
        return None  
    a_reduced = a // d
    b_reduced = b // d
    m_reduced = m // d

    inv = modular_inverse(a_reduced, m_reduced)
    if inv is None:
        return None  

    x0 = (inv * b_reduced) % m_reduced

    solutions = [(x0 + k * m_reduced) % m for k in range(d)]
    solution = f"Решим линейное сравнение по модулю {a}x<math xmlns='http://www.w3.org/1998/Math/MathML'><mo>&#x2261;</mo></math>{b}mod({m})\nНайдем НОД({a},{m})=d. d={d}. По теореме о существовании решений линейного сравнения по модулю, решение существует только если {d} делит {b}.\nПо свойству линейного сравнения по модулю, если d общий делитель a, b, m то можно переписать уравнение как: <math xmlns='http://www.w3.org/1998/Math/MathML'><mfrac><mi>a</mi><mi>d</mi></mfrac><mi>x</mi><mo>&#x2261;</mo><mfrac><mi>b</mi><mi>d</mi></mfrac><mi>m</mi><mi>o</mi><mi>d</mi><mo>&#xA0;</mo><mfrac><mi>m</mi><mi>d</mi></mfrac></math>.\nНайдем решение для {a_reduced}x<math xmlns='http://www.w3.org/1998/Math/MathML'><mo>&#x2261;</mo></math>{b_reduced}mod {m_reduced}.\nНайдем обратный элемент к {a_reduced}, он существует только если НОД({a_reduced},{m_reduced})=1. Обозначим обратный элемент как a'={inv}.\nНайдем частное решение путем умножения обеих частей сравнения на a'.\n<math xmlns='http://www.w3.org/1998/Math/MathML'><msub><mi>x</mi><mn>0</mn></msub><mo>&#x2261;</mo><mi>a</mi><mo>'</mo><mo>*</mo><mfrac><mi>b</mi><mi>d</mi></mfrac><mo>&#xA0;</mo><mi>m</mi><mi>o</mi><mi>d</mi><mo>&#xA0;</mo><mfrac><mi>m</mi><mi>d</mi></mfrac></math>\n<math xmlns='http://www.w3.org/1998/Math/MathML'><msub><mi>x</mi><mn>0</mn></msub></math>={x0}.\nОбщее решение имеет вид x =<math xmlns='http://www.w3.org/1998/Math/MathML'><msub><mi>x</mi><mn>0</mn></msub></math> + k * <math xmlns='http://www.w3.org/1998/Math/MathML'><mfrac><mi>m</mi><mi>d</mi></mfrac></math>, где k = 0, 1, 2,..., d - 1."
    
    return solutions, solution
