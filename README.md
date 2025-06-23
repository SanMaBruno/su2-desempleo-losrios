# 📊 Análisis de la Tasa Combinada de Desocupación y Tiempo Parcial Involuntario (SU2)
**Región de Los Ríos, Chile**

Este proyecto realiza un análisis exploratorio y visualización de la tasa combinada de desocupación y subempleo (SU2) en la Región de Los Ríos utilizando datos extraídos del portal INE.Stat. El objetivo es identificar tendencias, segmentaciones relevantes y patrones por grupo etario y sexo, contribuyendo a una mejor comprensión del fenómeno laboral regional.

---

## 🧠 Metodología

El análisis está estructurado bajo buenas prácticas de *Clean Code* y principios de reproducibilidad. La metodología utilizada incluye:

- Extracción y limpieza de datos
- Análisis exploratorio por grupo etario, sexo y total
- Visualizaciones con Seaborn y Matplotlib
- Organización modular mediante notebooks

---

## 📁 Estructura del proyecto

```
su2-desempleo-losrios/
│
├── data/
│   ├── raw/                               # Datos originales descargados del portal INE
│   └── processed/                         # Datos limpios y combinados para análisis
│       ├── poblacion_desocupada_sexo_limpio.csv
│       ├── poblacion_desocupada_tramo_edad_limpio.csv
│       └── poblacion_desocupada_combinado.csv
│
├── notebooks/
│   ├── 01_eda_desempleo.ipynb             # Análisis por tramo etario
│   ├── 02_eda_desempleo_por_sexo.ipynb    # Análisis por sexo
│   └── 03_eda_desempleo_total.ipynb       # Evolución general del desempleo
│
├── scripts/
│   ├── load_clean_edad.py                 # Limpieza y carga de datos por edad
│   ├── load_clean_sexo.py                 # Limpieza y carga de datos por sexo
│   ├── merge_edad_sexo.py                 # Unificación de datasets limpios
│   ├── validate_data.py                   # Validaciones básicas de integridad
│   └── __init__.py
│
├── utils/
│   ├── plot_helpers.py                    # Funciones auxiliares para visualización
│   └── __init__.py
│
├── tests/
│   ├── test_cleaning.py                   # Test unitarios para funciones de limpieza
│   └── __pycache__/
│
├── config.py                              # Configuración general del proyecto
├── requirements.txt                       # Dependencias del entorno
└── README.md
```

---

## 🧪 Requisitos

Este proyecto fue desarrollado en Python 3.10+ y utiliza:

- `pandas`
- `matplotlib`
- `seaborn`
- `jupyterlab`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Uso

1. Clonar el repositorio
2. Activar entorno virtual
3. Ejecutar los notebooks en el orden recomendado
4. Revisar las visualizaciones generadas

---

## 📈 Ejemplo de visualizaciones

Las siguientes gráficas muestran la evolución del desempleo por grupo etario y sexo:

- ![Desempleo por edad]([notebooks/img/desempleo_edad.png](https://github.com/SanMaBruno/su2-desempleo-losrios/blob/main/notebooks/01_eda_desempleo.ipynb))
- ![Desempleo por sexo](notebooks/img/desempleo_sexo.png)

---

## 👨‍💻 Autor

**Bruno San Martín Navarro**  
Ingeniero en informática & Científico de DatosEspecialista en ciencia de datos y desarrollo de soluciones escalables
[LinkedIn](https://www.linkedin.com/in/SanMaBruno/) · [GitHub](https://github.com/SanMaBruno)

---

## 📄 Licencia

Este proyecto se distribuye bajo licencia MIT. Consulta el archivo `LICENSE` para más detalles.
