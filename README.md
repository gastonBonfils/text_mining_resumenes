# Instalación

`python3 -m venv .venv`  
`source .venv/bin/activate`  
`pip install -q -r requirements.txt`  


# Resumenes de chats grupales

## Resumen

El proyecto tiene como objetivo realizar un resumen de los temas más significativos en un chat grupal propio, utilizando datos reales de conversaciones obtenidas de nuestras propias interacciones, en lugar de datasets externos. Para ello, se tendrán en cuenta la relevancia de los mensajes, los temas tratados, y la participación de los usuarios más activos en cada tema. El resumen se generará utilizando LLMs. Luego se buscara mejorar las respuestas utilizando técnicas de identificación de temas como LDA y fine-tunear el modelo con nuestras propias conversaciones.

## Hipótesis

<!-- El uso de modelos de LLM combinados con técnicas de detección de temas permite generar resúmenes comprensibles de chats grupales, capturando los temas principales, preservando las aportaciones más relevantes de la conversación -->

Utilizar técnicas de detección de temas como LDA, mejorará la calidad de las respuestas del LLM. Además, se espera que mejoré la calidad al entrenarla con nuestras conversaciones.  


## Objetivos preliminares

- **Análisis de contenido**: Identificar los temas principales discutidos en el chat grupal mediante técnicas de agrupamiento temático.
- **Compresión de la información**: Generar un resumen corto que conserve la esencia de las discusiones principales sin perder detalles críticos.
- **Evaluación de la calidad del resumen**: Implementar tests automáticos para evaluar la precisión y cobertura de los resúmenes generados.

### Revisión de objetivos
- **Evaluación automática**: No sabemos si podremos implementar tests automáticos de manera confiable. Por ahora evaluamos manualmente cada ejemplo que probamos.  
- **Resumenes de varios temas**: Actualmente, el programa no es preciso resumiendo muchos mensajes (mas de 15) por lo que se busca filtrar mensajes por tema y buscar resumir en grupos de tema. 


## Técnicas relevantes para aplicar
Para el resumen principal se utilizará una LLM que busque resumir el chat. Por el momento se usa un [modelo de resumenes finetuneado chats](https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary)  
Para el modelado de temas se utilizaran análisis de frecuencia de palabras, Latent Dirichlet Allocation y clustering.
Para el fine-tuning, resumen y evaluación se utilizarán Google Colab y la librería Transformers de Hugging Face.

## Avances en la metodología y evaluación del progreso
Hasta el momento se han probado los siguientes modelos de lenguaje
- [Phi 3 - Microsoft](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct): muy pesado y lento para nuestros propósitos
- [RoBERTa2RoBERTa](https://huggingface.co/Narrativa/bsc_roberta2roberta_shared-spanish-finetuned-mlsum-summarization): no se pudo hacer andar
- [Bart](https://huggingface.co/facebook/bart-large-cnn?): Buena performance en general pero no óptima para conversaciones
- [Finetuned bart](https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary): Mejor resultado hasta el momento

Además, se están haciendo pruebas utilizando métodos como LDA para ayudar al LLM a elegir los temas correctos a resumir.

Por ahora los resultados base son medianamente satisfactorios. En algunos casos el modelo no hace hincapie en lo que consideramos el tema principal pero esperamos poder optimizarlo.  

Lo que esperamos para el final del proyecto es poder resumir identificando temas.  
## Referencias
https://huggingface.co/facebook/bart-large-cnn

https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary

https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

https://colab.research.google.com/github/dudaspm/LDA_Bias_Data/blob/main/Latent%20Dirichlet%20Allocation%20(LDA).ipynb


## Planificación

**Semana 1:** 
- Revisión de las documentacion de referencia y probar dichas herramientas. 
- Configuración del entorno de trabajo y familiarización con el mismo.
<!-- - Carga de Datasets, modificación de los datos para mejorar su utilidad en el contexto del trabajo y procesamiento de datos. -->

**Semana 2:** 
- Implementar técnicas de modelado temático, tales como Latent Dirichlet Allocation (LDA), para identificar los temas principales discutidos en el chat grupal.


**Semana 3:**
- Afinar y mejorar el modelo para agrupar los mensajes de manera efectiva según el tema tratado.
- Identificación de los usuarios más activos en cada tema y generación de visualizaciones básicas para representar la distribución de temas y participantes.

**Semana 4:** 
- Preparar el conjunto de datos para entrenar modelos pre-entrenados (LLMs) utilizando la librería Transformers de Hugging Face.
- Aplicar técnicas de fine-tuning para personalizar un modelo LLM con el objetivo de generar resúmenes de los temas principales extraídos.
- Realizar pruebas iniciales de los resúmenes generados y ajustar los parámetros del modelo para mejorar la precisión.

**Semana 5:** 
<!-- - Implementar tests automáticos para evaluar la precisión y la cobertura de los resúmenes generados. -->
- Comparar la calidad de los resúmenes obtenidos con resúmenes manuales de las conversaciones, revisando posibilades de pruebas automáticaa.
<!-- - Refinar los modelos y evaluar la coherencia y relevancia de los resúmenes en función de los temas y usuarios más destacados. -->
- Realizar los ajustes finales en el modelo y optimizar la generación de resúmenes para maximizar su utilidad.
- Documentar todo el proceso realizado, incluyendo la preparación del entorno, análisis temático, fine-tuning, evaluación de resultados y conclusiones obtenidas.
- Preparación del informe y la presentación final del proyecto, mostrando ejemplos de resúmenes generados y la explicación de los métodos utilizados.
