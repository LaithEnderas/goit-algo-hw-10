import numpy as np
import scipy.integrate as spi

# визначення функції
def f(x):
    return x ** 2

# межі інтегрування
a, b = 0, 2

# метод Монте-Карло
N = 1_000_000  # кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_mean = np.mean(f(x_rand))
integral_mc = (b - a) * y_mean

# метод quad (перевірка)
integral_quad, error = spi.quad(f, a, b)

# аналітичне значення
integral_analytic = (b ** 3) / 3 - (a ** 3) / 3

# вивід результатів
print("Інтеграл методом Монте-Карло:", integral_mc)
print("Інтеграл методом quad:", integral_quad)
print("Аналітичне значення:", integral_analytic)
print("Абсолютна різниця (MC - quad):", abs(integral_mc - integral_quad))
