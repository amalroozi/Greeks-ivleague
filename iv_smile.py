import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from implied_vol import implied_volatility

def plot_iv_smile(ticker='SPY', expiry=None):
    stock = yf.Ticker(ticker)
    
    # get available expiries if none specified
    if expiry is None:
        expiry = stock.options[4]  # third expiry, enough time value
        print(f"Using expiry: {expiry}")
    
    chain = stock.option_chain(expiry)
    calls = chain.calls
    
    S = stock.history(period='1d')['Close'].iloc[-1]
    T = (np.datetime64(expiry) - np.datetime64('today')) / np.timedelta64(365, 'D')
    r = 0.05
    
    ivs = []
    strikes = []
    
    for _, row in calls.iterrows():
        K = row['strike']
        market_price = row['lastPrice']
        
        if market_price <= 0:
            continue
        
        iv = implied_volatility(market_price, S, K, T, r, option_type='call')
        
        if iv is not None and 0.01 < iv < 5:
            ivs.append(iv)
            strikes.append(K)
    
    plt.figure(figsize=(10, 6))
    plt.plot(strikes, ivs, 'b.-')
    plt.axvline(x=S, color='r', linestyle='--', label=f'Spot: {S:.2f}')
    plt.xlabel('Strike')
    plt.ylabel('Implied Volatility')
    plt.title(f'IV Smile — {ticker} options expiring {expiry}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('iv_smile.png', dpi=150)
    plt.show()
    print("Saved as iv_smile.png")

if __name__ == "__main__":
    plot_iv_smile('SPY', expiry='2026-09-18')