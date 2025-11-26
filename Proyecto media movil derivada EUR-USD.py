import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import traceback
import sys

def obtener_datos_forex_detallado():
    """
    Obtiene datos con mejor manejo de errores - VERSIÓN CORREGIDA
    """
    try:
        print("🔍 Intentando conectar con Yahoo Finance...")
        ticker = "EURUSD=X"
        fecha_fin = datetime.now()
        fecha_inicio = fecha_fin - timedelta(days=40)
        
        print(f"📅 Buscando datos desde {fecha_inicio.date()} hasta {fecha_fin.date()}")
        print(f"🎯 Ticker: {ticker}")
        
        datos = yf.download(ticker, start=fecha_inicio, end=fecha_fin, progress=False)
        
        print(f"✅ Datos descargados - Forma: {datos.shape}")
        
        if datos.empty:
            print("❌ No se encontraron datos")
            return None
        
        # CORRECIÓN: Aplanar las columnas MultiIndex
        if isinstance(datos.columns, pd.MultiIndex):
            print("📊 Detectado MultiIndex en columnas - Aplanando...")
            datos.columns = ['_'.join(col).strip() for col in datos.columns.values]
            print(f"📊 Columnas después de aplanar: {list(datos.columns)}")
        else:
            print(f"📊 Columnas disponibles: {list(datos.columns)}")
        
        # CORRECIÓN: Encontrar la columna correcta para Close
        columna_close = None
        for col in datos.columns:
            if 'Close' in col:
                columna_close = col
                break
        
        if columna_close is None:
            print("❌ No se encontró columna Close")
            return None
            
        print(f"🎯 Columna Close identificada: {columna_close}")
        print(f"💹 Primer precio: {datos[columna_close].iloc[0]:.5f}")
        print(f"💹 Último precio: {datos[columna_close].iloc[-1]:.5f}")
        
        return datos, columna_close
        
    except Exception as e:
        print(f"❌ ERROR CRÍTICO: {str(e)}")
        print("🔧 Traceback completo:")
        traceback.print_exc()
        return None, None

def calcular_derivada(precios_cierre):
    """
    Calcula la derivada (razón de cambio) usando diferencias finitas
    """
    # Calcular la derivada usando diferencias finitas
    derivada = np.gradient(precios_cierre)
    
    # Calcular media móvil de la derivada (5 periodos)
    media_movil_derivada = pd.Series(derivada).rolling(window=5).mean()
    
    return derivada, media_movil_derivada

def crear_grafica(datos, columna_close):
    """
    Crea la gráfica con precio de cierre y su derivada - VERSIÓN CORREGIDA
    """
    if datos is None or datos.empty:
        print("No hay datos para graficar")
        return
    
    # Obtener los últimos 30 días
    datos_30_dias = datos.tail(30)
    fechas = datos_30_dias.index
    precios_cierre = datos_30_dias[columna_close].values
    
    # Calcular derivada
    derivada, media_movil_derivada = calcular_derivada(precios_cierre)
    
    # Crear figura con dos subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
    
    # Gráfica 1: Precio de cierre
    ax1.plot(fechas, precios_cierre, 'b-', linewidth=2, label='Precio de Cierre EUR/USD')
    ax1.set_title('EUR/USD - Precio de Cierre (Últimos 30 días)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Precio (USD)', fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Formatear ejes
    ax1.tick_params(axis='x', rotation=45)
    
    # Gráfica 2: Derivada y media móvil
    ax2.plot(fechas, derivada, 'r-', alpha=0.7, linewidth=1, label='Derivada (Razón de Cambio)')
    ax2.plot(fechas, media_movil_derivada, 'g-', linewidth=2, label='Media Móvil de la Derivada (5 días)')
    ax2.set_title('Derivada del Precio - Razón de Cambio', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Razón de Cambio', fontsize=12)
    ax2.set_xlabel('Fecha', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Formatear ejes
    ax2.tick_params(axis='x', rotation=45)
    
    # Añadir fórmula de la derivada
    formula_text = r'$\frac{dP}{dt} \approx \frac{P(t) - P(t-1)}{\Delta t}$'
    ax2.text(0.02, 0.98, f'Fórmula: {formula_text}', 
             transform=ax2.transAxes, fontsize=12, 
             verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Añadir estadísticas
    stats_text = f'''Estadísticas de la Derivada:
Media: {derivada.mean():.6f}
Desv. Estándar: {derivada.std():.6f}
Máximo: {derivada.max():.6f}
Mínimo: {derivada.min():.6f}'''
    
    ax2.text(0.02, 0.02, stats_text, transform=ax2.transAxes, fontsize=10,
             verticalalignment='bottom', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
    
    # Ajustar layout
    plt.tight_layout()
    
    # Mostrar gráfica
    plt.show()
    
    # Imprimir información adicional en consola
    print("\n" + "="*60)
    print("INFORMACIÓN DEL ANÁLISIS EUR/USD")
    print("="*60)
    print(f"Período analizado: {fechas[0].strftime('%Y-%m-%d')} a {fechas[-1].strftime('%Y-%m-%d')}")
    print(f"Precio actual: {precios_cierre[-1]:.5f}")
    print(f"Derivada actual: {derivada[-1]:.6f}")
    print(f"Tendencia actual: {'ALCISTA' if derivada[-1] > 0 else 'BAJISTA'}")
    print("="*60)

def main():
    """
    Función principal con mejor logging - VERSIÓN CORREGIDA
    """
    print("🚀 INICIANDO ANÁLISIS EUR/USD")
    print("=" * 50)
    
    # Obtener datos
    datos, columna_close = obtener_datos_forex_detallado()
    
    if datos is not None and columna_close is not None:
        print("\n" + "=" * 50)
        print("📈 DATOS OBTENIDOS EXITOSAMENTE")
        print("=" * 50)
        
        # Mostrar resumen en terminal
        datos_30_dias = datos.tail(30)
        print(f"📅 Período analizado: {datos_30_dias.index[0].strftime('%Y-%m-%d')} a {datos_30_dias.index[-1].strftime('%Y-%m-%d')}")
        print(f"🔢 Número de días: {len(datos_30_dias)}")
        print(f"💰 Precio actual EUR/USD: {datos_30_dias[columna_close].iloc[-1]:.5f}")
        print(f"📊 Rango de precios: {datos_30_dias[columna_close].min():.5f} - {datos_30_dias[columna_close].max():.5f}")
        
        # Calcular y mostrar tendencia
        derivada = np.gradient(datos_30_dias[columna_close].values)
        tendencia = "ALCISTA 📈" if derivada[-1] > 0 else "BAJISTA 📉"
        print(f"🎯 Tendencia actual: {tendencia}")
        print(f"🔍 Derivada actual: {derivada[-1]:.6f}")
        
        print("\n" + "=" * 50)
        print("ÚLTIMOS 5 DÍAS:")
        print("=" * 50)
        for i in range(1, 6):
            if i <= len(datos_30_dias):
                fecha = datos_30_dias.index[-i]
                precio = datos_30_dias[columna_close].iloc[-i]
                cambio = derivada[-i]
                print(f"{fecha.strftime('%Y-%m-%d')}: {precio:.5f} (cambio: {cambio:+.6f})")
        
        # Crear gráfica
        crear_grafica(datos, columna_close)
        
    else:
        print("\n❌ NO SE PUDIERON OBTENER LOS DATOS")
        print("Posibles soluciones:")
        print("1. ✅ Verifica tu conexión a internet")
        print("2. ✅ Verifica que yfinance esté instalado: pip install yfinance")
        print("3. ✅ Intenta ejecutar nuevamente")
        print("4. 🔄 Si persiste, el servicio puede estar temporalmente no disponible")

if __name__ == "__main__":
    main()