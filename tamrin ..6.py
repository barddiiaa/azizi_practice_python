import numpy as np
from scipy import integrate

# تعریف تابعی که می‌خواهیم انتگرال آن را محاسبه کنیم
def integrand(x, y):
    return x**2 + y**2

# محاسبه انتگرال دوگانه
result, error = integrate.dblquad(integrand, 0, 1, lambda x: x**2, lambda x: x)

print(f'Result of the double integral: {result}')
print(f'Estimated error: {error}')
