import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 1167847408 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    m=x.mean()
    d=len(x)
    #scale = np.sum(np.square(x))
    return (-m*np.sqrt(d))/(np.sqrt(13)*(norm.ppf(1 - alpha / 2))), \
           (m*np.sqrt(d)) / (np.sqrt(13)*(norm.ppf(1- alpha / 2)))
