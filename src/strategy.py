import numpy as np
import pandas as pd
import statsmodels.api as sm


def fit_ff_models(returns_df, ff_data, stocks):
    # Añadir una constante a los factores de Fama-French para la regresión
    ff_factors = sm.add_constant(ff_data[["Mkt-RF", "SMB", "HML"]])

    # Iniciar un diccionario para almacenar los modelos de regresión para cada acción útil
    ff_models = {}

    # Iterar sobre cada acción y realizar la regresión de Fama-French
    for stock in stocks:
        # Crear un DataFrame para la regresión con los rendimientos de la acción y los factores de Fama-French
        df = pd.DataFrame(
            {
                "Return": returns_df[stock],
                "alpha": ff_factors["const"],
                "Mkt-RF": ff_factors["Mkt-RF"],
                "SMB": ff_factors["SMB"],
                "HML": ff_factors["HML"],
            }
        )
        # Eliminar filas con valores faltantes (esto eliminará únicamente la primera columna ya que para
        # calcular los rendimientos mensuales se usaron los precios el último día del mes anterior)
        df = df.dropna()
        # Realizar la regresión de mínimos cuadrados ordinarios (OLS) y almacenar el modelo en el diccionario
        ff_models[stock] = sm.OLS(
            df["Return"], df[["alpha", "Mkt-RF", "SMB", "HML"]]
        ).fit()

    return ff_models


def calculate_residuals(returns_df, ff_models, ff_factors, stocks):
    """
    Calculate the residuals of Fama-French regression for the given stocks.
    """
    # Seleccionar los últimos 12 meses de datos de rendimientos y factores
    last_returns = returns_df.iloc[-12:, :]
    last_factors = ff_factors.iloc[-12:, :]

    # Crear un DataFrame para almacenar los residuos
    residual_df = pd.DataFrame(index=last_returns.index)

    # Inicializar una lista para almacenar los nombres de las columnas de los residuos
    residual_columns = []

    # Iterar sobre las acciones disponibles y calcular los residuos de la regresión de Fama-French
    for stock in stocks:
        # Obtener los coeficientes de la regresión de Fama-French para la acción
        coef = ff_models[stock].params
        # Calcular los residuos
        residuals = (
            last_returns[stock]
            - coef["Mkt-RF"] * last_factors["Mkt-RF"]
            - coef["SMB"] * last_factors["SMB"]
            - coef["HML"] * last_factors["HML"]
        )
        residual_columns.append(residuals)

    residual_df = pd.concat(residual_columns, axis=1)
    residual_df.columns = stocks

    # DataFrame con los residuos de la regresión de Fama-French
    return residual_df


def calculate_adjusted_residuals(residual_df):
    # Calcular los residuos ajustados por riesgo para las acciones disponibles # y ordenar de menor a mayor
    risk_adjusted_residuals = (residual_df.mean() / residual_df.var()).sort_values()
    return risk_adjusted_residuals


def create_portfolio(risk_adjusted_residuals, top_pct=10, bottom_pct=10):
    """
    Create long-short portfolio based on momentum scores.
    """
    # Filtrar los residuos ajustados por riesgo que están por encima del percentil (100 - top_pct)
    buy = risk_adjusted_residuals[
        risk_adjusted_residuals > np.percentile(risk_adjusted_residuals, 100 - top_pct)
    ]

    # Filtrar los residuos ajustados por riesgo  que están por debajo del decil bottom_pct
    sell = risk_adjusted_residuals[
        risk_adjusted_residuals < np.percentile(risk_adjusted_residuals, bottom_pct)
    ]

    return buy, sell
