# Análisis de Estrategia de Momentum Residual en el Mercado de Valores

## Descripción del Proyecto

Este proyecto implementa y analiza una estrategia de inversión conocida como Momentum Residual en el mercado de valores de Nueva York (NYSE). La estrategia se basa en la premisa de que los rendimientos de las acciones muestran cierta "inercia", lo que resulta en el fenómeno conocido como "efecto momentum".

## Características Principales

- Implementación de la estrategia de Momentum Residual
- Análisis de acciones del NYSE para marzo de 2024
- Utilización del modelo de tres factores de Fama-French
- Construcción de un portafolio dólar-neutral

## Metodología

1. **Recopilación de Datos**: 
   - Precios de acciones del NYSE (ajustados por splits y dividendos)
   - Factores de Fama-French (MKT, SMB, HML)

2. **Preprocesamiento**:
   - Limpieza y ajuste de datos
   - Cálculo de rendimientos mensuales

3. **Implementación de la Estrategia**:
   - Regresión de rendimientos sobre factores de Fama-French (período de 36 meses)
   - Cálculo de residuos para el período de formación de 12 meses
   - Cálculo de rendimientos residuales ajustados por riesgo

4. **Construcción del Portafolio**:
   - Selección de acciones basada en deciles de rendimientos residuales
   - Formación de portafolio dólar-neutral

5. **Análisis y Visualización**:
   - Evaluación del desempeño de la estrategia
   - Visualizaciones de resultados clave

## Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib/Seaborn
- yfinance (para la descarga de datos de acciones)
- pandas-datareader (para datos de Fama-French)

## Estructura del Proyecto

```
momentum-residual-strategy/
│
├── data/
│   └── stocks.xlsx
│
├── notebooks/
│   └── momentum_residual_analysis.ipynb
│
├── src/
│   ├── data_collection.py
│   ├── preprocessing.py
│   ├── strategy.py
│   └── visualization.py
│
├── results/
│   ├── adjusted_residuals_histogram.png
│   └── portfolio_performance.csv
│
├── requirements.txt
└── README.md
```

## Cómo Usar

1. Clone el repositorio
2. Instale las dependencias: `pip install -r requirements.txt`
3. Ejecute el notebook `momentum_residual_analysis.ipynb` en la carpeta `notebooks/`

## Resultados

El proyecto proporciona insights sobre:
- El desempeño de la estrategia de Momentum Residual en el mercado de NYSE
- Comparación con estrategias de referencia
- Análisis de riesgo y rendimiento del portafolio construido

---

**Nota**: Este proyecto es solo para fines educativos y de investigación. No constituye asesoramiento financiero.