import numpy as np
from black_scholes import call_price, put_price, vega

def implied_volatility(market_price, S, K, T, r, option_type='call', tol=1e-6, max_iter=100):
    sigma = 0.2  # initial guess
    
    for i in range(max_iter):
        if option_type == 'call':
            price = call_price(S, K, T, r, sigma)
        else:
            price = put_price(S, K, T, r, sigma)
        
        v = vega(S, K, T, r, sigma)
        
        if v < 1e-10:  # vega too small, can't converge
            return None
        
        sigma_new = sigma - (price - market_price) / v
        
        if abs(sigma_new - sigma) < tol:
            return sigma_new
        
        sigma = sigma_new
    
    return None  # did not converge

if __name__ == "__main__":
    # if BS gives 10.4506 for sigma=0.2, IV should recover 0.2
    S, K, T, r = 100, 100, 1, 0.05
    market_price = 10.4506

    iv = implied_volatility(market_price, S, K, T, r, option_type='call')
    print(f"Implied Volatility: {iv:.4f}")