# Instalación

`python3 -m venv .venv`  
`source .venv/bin/activate`  
`pip install -q -r requirements.txt`  


# Resumenes de chats grupales

## Resumen

Dado un chat grupal poder realizar un resumen de los temas mas significantes, teniendo en cuenta que la relevacia del mensaje y que usuarios hablaron mas en cada tema. Este resumen se conseguirá utilizando técnicas de fine-tuning de LLMs

## Hipótesis
<!-- no se lo saqué de chatgpt jaja, esto se ve si ven el raw saludo-->
El uso de modelos de LLM combinados con técnicas de detección de temas permite generar resúmenes comprensibles de chats grupales, capturando los temas principales, preservando las aportaciones más relevantes de la conversación


## Objetivos preliminares
<!-- pseudo chatgpt -->
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

**Semana 2:** 
**Semana 3:** 

**Semana 4:** 

**Semana 5:** 

