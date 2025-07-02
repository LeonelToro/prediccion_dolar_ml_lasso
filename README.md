# 📈 Predicción del Dólar Oficial en Argentina

Este proyecto desarrolla un modelo predictivo del tipo de cambio oficial en Argentina utilizando un flujo completo en Python: descarga automatizada de datos desde la **API oficial del BCRA**, limpieza estructurada, análisis exploratorio y construcción de modelos de regresión, con énfasis en la interpretación económica de los resultados.

---

## 🧠 Objetivo

Explorar cómo ciertas variables macroeconómicas impactan en la evolución del dólar oficial en Argentina, combinando criterios estadísticos y fundamentos teóricos. El objetivo no es anticipar con precisión su valor futuro, sino construir un modelo transparente y robusto que permita interpretar relaciones estructurales de largo plazo.

---

## 📁 Archivos incluidos

| Archivo | Descripción |
|--------|-------------|
| [`descargar_endpoints.py`](./descargar_endpoints.py) | Descarga automática de datos económicos desde la API oficial del BCRA. |
| [`limpieza_preparacion.py`](./limpieza_preparacion.py) | Limpieza y estructuración de los datos descargados en un único DataFrame mensual. |
| [`EDA.ipynb`](./EDA.ipynb) | Análisis exploratorio de datos: correlaciones, tendencias y visualizaciones. |
| [`prediccion_usd.ipynb`](./prediccion_usd.ipynb) | Modelado predictivo y evaluación de regresiones (Lineal y Lasso). |
| [`base_monetaria.csv`](./base_monetaria.csv) | Serie histórica de la base monetaria (BCRA). |
| [`brecha_usd.csv`](./brecha_usd.csv) | Cálculo de la brecha entre dólar oficial y paralelo. |
| [`cer.csv`](./cer.csv) | Serie del Coeficiente de Estabilización de Referencia. |
| [`inflacion.csv`](./inflacion.csv) | Índice de inflación mensual (IPC). |
| [`leliq.csv`](./leliq.csv) | Datos sobre tasas de Leliq a 7 días. |
| [`reservas.csv`](./reservas.csv) | Reservas internacionales del BCRA. |
| [`tasa_depositos_30_dias.csv`](./tasa_depositos_30_dias.csv) | Tasa promedio de depósitos a plazo fijo a 30 días. |
| [`tasa_pase_pasivas_1_dia.csv`](./tasa_pase_pasivas_1_dia.csv) | Tasa de pases pasivos a un día. |
| [`usd_general.csv`](./usd_general.csv) | Dataset con diferentes cotizaciones históricas del dólar. |
| [`usd_minorista.csv`](./usd_minorista.csv) | Cotización minorista del dólar. |
| [`usd_oficial.csv`](./usd_oficial.csv) | Serie oficial del dólar BCRA (variable objetivo del modelo). |
| [`uva.csv`](./uva.csv) | Índice de Unidades de Valor Adquisitivo (UVA). |
| [`consolidado.csv`](./consolidado.csv) | Dataset final consolidado utilizado para el modelado. |

---

## 🧾 Dataset

- Datos descargados mediante la **API oficial del BCRA**.  
- Variables económicas mensuales desde **junio de 2010** en adelante.  
- Se seleccionó ese punto de corte por ser la fecha más antigua con cobertura completa y sin valores nulos.

---

## 🔍 Variables predictoras seleccionadas

La selección de variables se basó en una combinación de análisis de correlación y fundamentos económicos:

- **Inflación mensual oficial**  
  Alta correlación con el dólar; refleja deterioro del poder adquisitivo.

- **Base monetaria**  
  Mide la cantidad de dinero en circulación, clave en modelos ortodoxos.

- **CER (Coeficiente de Estabilización de Referencia)**  
  Índice indexado al IPC utilizado en contratos financieros.

- **Tasa de interés de depósitos a 30 días**  
  Indicador de política monetaria y expectativas del sistema financiero.

---

## 📊 Modelos implementados

Se probaron diferentes modelos de regresión:

- **Regresión Lineal Múltiple**  
- **Lasso (penalización L1)** ✅ modelo final elegido  
- **Ridge, ElasticNet y Random Forest** (descartados por menor desempeño o complejidad innecesaria)

### 📈 Resultados de evaluación (conjunto de test)

| Métrica       | Regresión Lineal | Lasso ✅ |
|---------------|------------------|----------|
| RMSE (Test)   | 89.334           | 86.124   |
| MAE (Test)    | 71.957           | 69.272   |
| R² (Test)     | 0.778            | 0.794    |
| R² (CV Prom.) | 0.938            | 0.938    |

- El modelo **Lasso** permite reducir la complejidad descartando variables con coeficientes cercanos a cero.  
- Mejora la interpretabilidad y reduce el riesgo de overfitting.

---

## 📉 Conclusiones

- El valor del dólar oficial puede ser explicado parcialmente por un conjunto reducido de variables macroeconómicas relevantes.  
- El modelo **predice con alta eficacia en la mayor parte del período analizado**, mostrando muy buen ajuste en contextos macroeconómicos relativamente estables.  
- Se observa una **mayor variación del error en momentos de cambios abruptos de política económica**, donde el comportamiento del tipo de cambio responde a múltiples factores no lineales o no cuantificados.  
- Lasso ofrece una herramienta simple pero potente para representar relaciones económicas estructurales.  
- El modelo es una primera aproximación interpretativa y no busca predecir valores con precisión en contextos de alta volatilidad.

---

## 🛠️ Herramientas utilizadas

- **Python**  
  - pandas  
  - matplotlib  
  - seaborn  
  - numpy  
  - sklearn  
  - requests  
  - os  
  - functools  
- **API oficial del BCRA** para recolección automatizada  
- **Jupyter Notebook**  
- **Visual Studio Code**  
- **Git y GitHub**

---

## 📬 Contacto

📧 leonel.toro93@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/leoneltoro/)  
🌐 [Portfolio Web](https://leoneltoro.github.io)

---

# 📈 Official USD Exchange Rate Prediction – Argentina

This project builds a predictive model for the official USD/ARS exchange rate in Argentina using a full data pipeline in Python: automated data collection from the **official BCRA API**, structured data cleaning, exploratory analysis, and regression modeling – with a strong focus on economic interpretation.

---

## 🧠 Objective

To explore how key macroeconomic variables impact the official exchange rate in Argentina, combining statistical analysis with theoretical economic reasoning.  
The goal is not to precisely forecast the future value of the exchange rate, but to construct a transparent and robust model that explains long-term structural relationships.

---

## 📁 Included Files

| File | Description |
|------|-------------|
| [`descargar_endpoints.py`](./descargar_endpoints.py) | Automatically downloads economic data from the official BCRA API. |
| [`limpieza_preparacion.py`](./limpieza_preparacion.py) | Cleans and structures all raw datasets into a unified monthly DataFrame. |
| [`EDA.ipynb`](./EDA.ipynb) | Exploratory data analysis: correlations, trends, and visual insights. |
| [`prediccion_usd.ipynb`](./prediccion_usd.ipynb) | Regression modeling and evaluation (Linear and Lasso). |
| [`base_monetaria.csv`](./base_monetaria.csv) | Historical series for Argentina’s monetary base. |
| [`brecha_usd.csv`](./brecha_usd.csv) | Spread between official and parallel USD rates. |
| [`cer.csv`](./cer.csv) | CPI-indexed adjustment coefficient (CER). |
| [`inflacion.csv`](./inflacion.csv) | Monthly inflation index (CPI). |
| [`leliq.csv`](./leliq.csv) | Leliq 7-day interest rates. |
| [`reservas.csv`](./reservas.csv) | Central Bank’s international reserves. |
| [`tasa_depositos_30_dias.csv`](./tasa_depositos_30_dias.csv) | Fixed-term deposit rate (30 days). |
| [`tasa_pase_pasivas_1_dia.csv`](./tasa_pase_pasivas_1_dia.csv) | Passive repo rate (overnight). |
| [`usd_general.csv`](./usd_general.csv) | General dataset of various exchange rates. |
| [`usd_minorista.csv`](./usd_minorista.csv) | Retail USD exchange rate. |
| [`usd_oficial.csv`](./usd_oficial.csv) | Official USD exchange rate from the BCRA – target variable. |
| [`uva.csv`](./uva.csv) | CPI-adjusted unit of value (UVA). |
| [`consolidado.csv`](./consolidado.csv) | Final cleaned dataset used for modeling. |

---

## 🧾 Dataset

- Data was collected using the **official API provided by BCRA (Central Bank of Argentina)**.  
- The dataset covers **monthly economic indicators from June 2010 onward**.  
- That cutoff was chosen to ensure complete and consistent data without missing values.

---

## 🔍 Selected Predictors

Predictor selection was based on both correlation analysis and macroeconomic theory:

- **Official monthly inflation (IPC)**  
  Strong correlation with USD; reflects internal currency depreciation.

- **Monetary base**  
  Key indicator in monetary theories explaining inflation and FX behavior.

- **CER (Stabilization Reference Coefficient)**  
  An indexation tool adjusted by the CPI, commonly used in contracts.

- **30-day deposit interest rate**  
  Reflects BCRA’s monetary policy and market expectations.

---

## 📊 Models Tested

The following regression models were tested:

- **Multiple Linear Regression**  
- **Lasso Regression (L1 regularization)** ✅ Final model selected  
- **Ridge, ElasticNet and Random Forest** (discarded due to poor performance or unnecessary complexity)

### 📈 Evaluation Results (Test Set)

| Metric        | Linear Regression | Lasso ✅ |
|---------------|-------------------|----------|
| RMSE (Test)   | 89.334            | 86.124   |
| MAE (Test)    | 71.957            | 69.272   |
| R² (Test)     | 0.778             | 0.794    |
| R² (CV Avg.)  | 0.938             | 0.938    |

- **Lasso** improved performance by reducing overfitting and automatically excluding variables with near-zero coefficients.  
- The result is a more interpretable and stable model structure.

---

## 📉 Conclusions

- The official USD exchange rate can be partially explained by a reduced set of meaningful macroeconomic indicators.  
- The model **performs with high accuracy across most of the analyzed time period**, especially under relatively stable macroeconomic conditions.  
- It shows **greater variation in prediction error during policy shifts or external shocks**, where exchange rate dynamics become less linear and more volatile.  
- Lasso proved to be a powerful yet simple tool to capture structural relationships.  
- This model serves as a transparent, interpretable baseline rather than a precise forecasting tool in highly volatile scenarios.

---

## 🛠️ Tools Used

- **Python**  
  - pandas  
  - matplotlib  
  - seaborn  
  - numpy  
  - scikit-learn  
  - requests  
  - os  
  - functools  
- **Official BCRA API** for data collection  
- **Jupyter Notebook**  
- **Visual Studio Code**  
- **Git & GitHub**

---

## 📬 Contact

📧 leonel.toro93@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/leoneltoro/)  
🌐 [Portfolio Website](https://leoneltoro.github.io)

---

