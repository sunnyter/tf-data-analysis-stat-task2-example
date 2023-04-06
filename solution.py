import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 1167847408 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    scale = np.sum(np.square(x))
    return np.sqrt(scale / (13*chi2.ppf(1 - alpha / 2, df=len(x)))), \
           np.sqrt(scale / (13*chi2.ppf(alpha / 2, df=len(x))))
