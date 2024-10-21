# Instalación

`python3 -m venv .venv`  
`source .venv/bin/activate`  
`pip install -q -r requirements.txt`  


# Resumenes de chats grupales

## Resumen

El proyecto tiene como objetivo realizar un resumen de los temas más significativos en un chat grupal propio, utilizando datos reales de conversaciones obtenidas de nuestras propias interacciones, en lugar de datasets externos. Para ello, se tendrán en cuenta la relevancia de los mensajes, los temas tratados, y la participación de los usuarios más activos en cada tema. El resumen se generará utilizando técnicas avanzadas de fine-tuning aplicadas a modelos de lenguaje de gran tamaño (LLMs).

## Hipótesis

El uso de modelos de LLM combinados con técnicas de detección de temas permite generar resúmenes comprensibles de chats grupales, capturando los temas principales, preservando las aportaciones más relevantes de la conversación


## Objetivos preliminares

- **Análisis de contenido**: Identificar los temas principales discutidos en el chat grupal mediante técnicas de agrupamiento temático.
- **Compresión de la información**: Generar un resumen corto que conserve la esencia de las discusiones principales sin perder detalles críticos.
- **Evaluación de la calidad del resumen**: Implementar tests automáticos para evaluar la precisión y cobertura de los resúmenes generados.

## Técnicas relevantes para aplicar
Para el modelado de temas se utilizaran análisis de frecuencia de palabras, Latent Dirichlet Allocation y clustering.
Para el fine-tuning, resumen y evaluación se utilizarán Google Colab y la librería Transformers de Hugging Face.

## Referencias
https://huggingface.co/facebook/bart-large-cnn

https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

https://colab.research.google.com/github/dudaspm/LDA_Bias_Data/blob/main/Latent%20Dirichlet%20Allocation%20(LDA).ipynb


## Planificación

**Semana 1:** 
- Revisión de las documentacion de referencia y probar dichas herramientas. 
- Configuración del entorno de trabajo y familiarización con el mismo.
- Carga de Datasets, modificación de los datos para mejorar su utilidad en el contexto del trabajo y procesamiento de datos.

**Semana 2:** 
- Implementar técnicas de modelado temático, tales como Latent Dirichlet Allocation (LDA), para identificar los temas principales discutidos en el chat grupal.
- Afinar y mejorar el modelo para agrupar los mensajes de manera efectiva según el tema tratado.
- Identificación de los usuarios más activos en cada tema y generación de visualizaciones básicas para representar la distribución de temas y participantes.

**Semana 3:** 
- Preparar el conjunto de datos para entrenar modelos pre-entrenados (LLMs) utilizando la librería Transformers de Hugging Face.
- Aplicar técnicas de fine-tuning para personalizar un modelo LLM con el objetivo de generar resúmenes de los temas principales extraídos.
- Realizar pruebas iniciales de los resúmenes generados y ajustar los parámetros del modelo para mejorar la precisión.

**Semana 4:** 
- Implementar tests automáticos para evaluar la precisión y la cobertura de los resúmenes generados.
- Comparar la calidad de los resúmenes obtenidos con resúmenes manuales de las conversaciones, revisando posibles mejoras en la generación automática.
- Refinar los modelos y evaluar la coherencia y relevancia de los resúmenes en función de los temas y usuarios más destacados.

**Semana 5:** 
- Realizar los ajustes finales en el modelo y optimizar la generación de resúmenes para maximizar su utilidad.
- Documentar todo el proceso realizado, incluyendo la preparación del entorno, análisis temático, fine-tuning, evaluación de resultados y conclusiones obtenidas.
- Preparación del informe y la presentación final del proyecto, mostrando ejemplos de resúmenes generados y la explicación de los métodos utilizados.
