import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def call_price(S, K, T, r, sigma):
    return S * norm.cdf(d1(S, K, T, r, sigma)) - K * np.exp(-r * T) * norm.cdf(d2(S, K, T, r, sigma))

def put_price(S, K, T, r, sigma):
    return K * np.exp(-r * T) * norm.cdf(-d2(S, K, T, r, sigma)) - S * norm.cdf(-d1(S, K, T, r, sigma))

def delta(S, K, T, r, sigma, option_type='call'):
    if option_type == 'call':
        return norm.cdf(d1(S, K, T, r, sigma))
    else:
        return norm.cdf(d1(S, K, T, r, sigma)) - 1

def gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    return S * norm.pdf(d1(S, K, T, r, sigma)) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type='call'):
    d_1 = d1(S, K, T, r, sigma)
    d_2 = d2(S, K, T, r, sigma)
    if option_type == 'call':
        return (-S * norm.pdf(d_1) * sigma / (2 * np.sqrt(T))) - r * K * np.exp(-r * T) * norm.cdf(d_2)
    else:
        return (-S * norm.pdf(d_1) * sigma / (2 * np.sqrt(T))) + r * K * np.exp(-r * T) * norm.cdf(-d_2)

def rho(S, K, T, r, sigma, option_type='call'):
    if option_type == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(d2(S, K, T, r, sigma))
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2(S, K, T, r, sigma))


if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    print(f"Call Price: {call_price(S, K, T, r, sigma):.4f}")
    print(f"Put Price:  {put_price(S, K, T, r, sigma):.4f}")
    print(f"Delta (call): {delta(S, K, T, r, sigma, 'call'):.4f}")
    print(f"Gamma:        {gamma(S, K, T, r, sigma):.4f}")
    print(f"Vega:         {vega(S, K, T, r, sigma):.4f}")
    print(f"Theta (call): {theta(S, K, T, r, sigma, 'call'):.4f}")
    print(f"Rho (call):   {rho(S, K, T, r, sigma, 'call'):.4f}")