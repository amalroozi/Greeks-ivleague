# Greeks-ivleague


A Black-Scholes options pricing engine built from scratch in Python.

[IV Smile](iv_smile.png)

## What it does

- Prices European call and put options using the Black-Scholes Merton model
- Computes all five Greeks: Delta, Gamma, Vega, Theta, Rho
- Solves for Implied Volatility from market prices using Newton-Raphson iteration
- Fetches live SPY options chain data and plots the IV smile across strikes

## The math:

Given inputs S (spot), K (strike), T (time to expiry), r (risk-free rate), σ (volatility):

## The math

$$d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$

$$C = S \cdot N(d_1) - Ke^{-rT} \cdot N(d_2)$$

$$P = Ke^{-rT} \cdot N(-d_2) - S \cdot N(-d_1)$$

##Structure:

black_scholes.py   # pricing + greeks
implied_vol.py     # Newton-Raphson IV solver
iv_smile.py        # live data + smile plot
notebooks/         # demo walkthrough


## Run 


pip install numpy scipy matplotlib yfinance
python black_scholes.py
python implied_vol.py
python iv_smile.py


## The IV smile

The plot shows implied volatility across strikes for SPY options. IV is highest for low strikes, the market prices in crash risk (left skew), departing from Black Scholes constant volatility assumption.