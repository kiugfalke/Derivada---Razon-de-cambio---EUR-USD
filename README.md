## 🇬🇧 README (British English)

### 📊 Forex Velocity Analysis: EUR/USD Rate of Change Model

Welcome to the **Forex Velocity Analysis** project, a quantitative approach to assessing the short-term momentum of the **EUR/USD** currency pair. This Python script employs differential calculus to transform daily price data into a measurable rate of change, providing clear insight into market direction and speed.

<img width="1536" height="754" alt="Grafica 1" src="https://github.com/user-attachments/assets/a9dfe8f1-4556-415a-a689-483cb8c709bc" />


### **Core Concept: Price as a Function of Time**

The methodology treats the **EUR/USD closing price, $P(t)$**, as a continuous function of time. The key analytical tool used is the **First Derivative ($\frac{dP}{dt}$)**, which is calculated numerically using the Finite Difference method:

$$\frac{dP}{dt} \approx \frac{P(t) - P(t-1)}{\Delta t}$$

  * **Financial Interpretation:** The derivative represents the **velocity** or **momentum** of the price.
      * $\mathbf{\frac{dP}{dt} > 0}$ indicates an **Uptrend** (Price is increasing).
      * $\mathbf{\frac{dP}{dt} < 0}$ indicates a **Downtrend** (Price is decreasing).

-----

### **🚀 Key Features of the Script (`Proyecto media movil derivada EUR-USD.py`)**

1.  **Robust Data Acquisition:** Uses the `yfinance` library to download **EUR/USD ($\text{EURUSD=X}$)** data over a 40-day window, including comprehensive error handling for data retrieval and column identification.
2.  **Rate of Change Calculation:** Calculates the daily rate of change (the first derivative) using the high-precision `numpy.gradient` function.
3.  **Momentum Smoothing:** Calculates a **5-day Simple Moving Average** of the derivative. This smoothed line acts as a clearer signal for sustained momentum shifts, helping filter out daily noise.
4.  **Statistical Insight:** Provides key statistics of the derivative (Mean, Std. Deviation, Max, Min) to quantify the historical volatility of the rate of change.
5.  **Comprehensive Visualisation (See `Grafica 1.png`):** Generates a two-panel chart focused on the last 30 trading days:
      * **Panel 1 (Top):** The EUR/USD Closing Price line chart.
      * **Panel 2 (Bottom):** The raw Derivative (Rate of Change) and its 5-day Moving Average. This panel is the core of the analysis, visually highlighting momentum reversals (where the derivative crosses zero).

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d842ee74-c13e-4a04-ad3d-f6b9b9a1a120" />


### **💡 Strategic Interpretation**

The **Moving Average of the Derivative** is the primary signal:

  * **Buying Signal:** When the Moving Average of the Derivative crosses **above zero** from below.
  * **Selling Signal:** When the Moving Average of the Derivative crosses **below zero** from above.

### **🛠️ How to Run the Analysis**

**Prerequisites:**

Ensure you have the necessary Python libraries installed:

```bash
pip install yfinance pandas numpy matplotlib
```

**Execution:**

1.  Save the code as `Proyecto media movil derivada EUR-USD.py`.
2.  Run the script from your terminal:
    ```bash
    python "Proyecto media movil derivada EUR-USD.py"
    ```
3.  The script will print a detailed status to the console (including the current price, derivative, and short-term trend) and display the generated chart.

-----

-----

## 🇩🇪 README (Deutsche Sprache)

### 📊 Forex-Geschwindigkeitsanalyse: EUR/USD-Veränderungsratenmodell

Willkommen beim Projekt **Forex-Geschwindigkeitsanalyse**, einem quantitativen Ansatz zur Bewertung des kurzfristigen Momentums des Währungspaares **EUR/USD**. Dieses Python-Skript verwendet Differentialrechnung, um tägliche Preisdaten in eine messbare Änderungsrate umzuwandeln, was klare Einblicke in die Marktrichtung und -geschwindigkeit liefert.

-----

### **Kernkonzept: Preis als Funktion der Zeit**

Die Methodik behandelt den **EUR/USD-Schlusskurs, $P(t)$**, als eine stetige Funktion der Zeit. Das zentrale Analysewerkzeug ist die **Erste Ableitung ($\frac{dP}{dt}$)**, die numerisch mittels der Finite-Differenzen-Methode berechnet wird:

$$\frac{dP}{dt} \approx \frac{P(t) - P(t-1)}{\Delta t}$$

  * **Finanzielle Interpretation:** Die Ableitung repräsentiert die **Geschwindigkeit** oder das **Momentum** des Preises.
      * $\mathbf{\frac{dP}{dt} > 0}$ signalisiert einen **Aufwärtstrend** (Preis steigt).
      * $\mathbf{\frac{dP}{dt} < 0}$ signalisiert einen **Abwärtstrend** (Preis sinkt).

-----

### **🚀 Hauptfunktionen des Skripts (`Proyecto media movil derivada EUR-USD.py`)**

1.  **Robuste Datenerfassung:** Verwendet die `yfinance`-Bibliothek, um **EUR/USD ($\text{EURUSD=X}$)**-Daten über ein 40-Tage-Fenster herunterzuladen, einschließlich umfassender Fehlerbehandlung für die Datenabfrage und Spaltenidentifizierung.
2.  **Berechnung der Änderungsrate:** Berechnet die tägliche Änderungsrate (die erste Ableitung) unter Verwendung der hochpräzisen Funktion `numpy.gradient`.
3.  **Momentum-Glättung:** Berechnet einen **Gleitenden Durchschnitt der Ableitung über 5 Tage**. Diese geglättete Linie dient als klareres Signal für nachhaltige Momentum-Verschiebungen und hilft, das tägliche Marktrauschen herauszufiltern.
4.  **Statistische Einblicke:** Liefert Schlüsselstatistiken der Ableitung (Mittelwert, Standardabweichung, Maximum, Minimum), um die historische Volatilität der Änderungsrate zu quantifizieren.
5.  **Umfassende Visualisierung (Siehe `Grafica 1.png`):** Erzeugt ein Zwei-Panel-Diagramm, das sich auf die letzten 30 Handelstage konzentriert:
      * **Panel 1 (Oben):** Der Linienchart des EUR/USD-Schlusskurses.
      * **Panel 2 (Unten):** Die rohe Ableitung (Änderungsrate) und ihr 5-Tage-Gleitender Durchschnitt. Dieses Panel ist der Kern der Analyse und hebt visuell Momentum-Umkehrungen hervor (wo die Ableitung die Nulllinie kreuzt).

### **💡 Strategische Interpretation**

Der **Gleitende Durchschnitt der Ableitung** ist das primäre Signal:

  * **Kaufsignal:** Wenn der Gleitende Durchschnitt der Ableitung von unten nach **über Null** kreuzt.
  * **Verkaufssignal:** Wenn der Gleitende Durchschnitt der Ableitung von oben nach **unter Null** kreuzt.

### **🛠️ Wie man die Analyse ausführt**

**Voraussetzungen:**

Stellen Sie sicher, dass Sie die notwendigen Python-Bibliotheken installiert haben:

```bash
pip install yfinance pandas numpy matplotlib
```

**Ausführung:**

1.  Speichern Sie den Code als `Proyecto media movil derivada EUR-USD.py`.
2.  Führen Sie das Skript in Ihrem Terminal aus:
    ```bash
    python "Proyecto media movil derivada EUR-USD.py"
    ```
3.  Das Skript gibt einen detaillierten Status in der Konsole aus (einschließlich des aktuellen Preises, der Ableitung und des kurzfristigen Trends) und zeigt das generierte Diagramm an.

Would you like me to analyze the specific data presented in `Grafica 1.png` based on the script's methodology?
