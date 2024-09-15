import pandas as pd
import matplotlib.pyplot as plt

# Dane cen w PLN
prices = [
    (1, 2.12),
    (2, 2.56),
    (3, 3.10),
    (4, 3.16),
    (5, 3.58),
    (6, 5.12),
    (7, 5.16),
    (8, 5.20),
    (9, 4.12),
    (10, 4.10),
    (11, 3.65),
    (12, 4.25),
]

# Stworzenie DataFrame
df = pd.DataFrame(prices, columns=['Month', 'PricePLN'])

# Ustawienie indeksu na miesiąc
df.set_index('Month', inplace=True)

# Dodanie kolumny priceUSD
df['PriceUSD'] = df['PricePLN'] / 4

# Wyświetlenie DataFrame
print(df)

# Rysowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['PriceUSD'], 'r--', marker='o')  
plt.title('Price of goods (USD)')
plt.xlabel('Month')
plt.grid(True)
plt.show()
