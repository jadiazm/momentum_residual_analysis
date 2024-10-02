import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_prices(stocks, prices):
    """
    Plot the adjusted closing prices of some stocks.
    """
    plt.figure(figsize=(12, 6))
    for stock in stocks:
        plt.plot(prices.index, prices[stock], label=stock)

    plt.xlabel('Fecha')
    plt.ylabel('Precio mensual de cierre ajustado')
    plt.title('Precio mensual de cierre ajustado de algunas acciones')
    plt.legend()
    plt.show()

def plot_adjusted_residuals(risk_adjusted_residuals):
    # Calcular los deciles 1 y 9
    decile_1 = np.percentile(risk_adjusted_residuals, 10)
    decile_9 = np.percentile(risk_adjusted_residuals, 90)

    # Histograma de los residuos ajustados por riesgo
    plt.figure(figsize=(8, 6))
    sns.histplot(risk_adjusted_residuals, bins=20, kde=True)
    plt.xlabel('Residuos ajustados por riesgo')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de los residuos ajustados por riesgo')

    # Añadir líneas verticales para los deciles 1 y 9
    plt.axvline(decile_1, color='red', linestyle='--', label='Decil 1')
    plt.axvline(decile_9, color='blue', linestyle='--', label='Decil 9')
    plt.legend()

    plt.show()