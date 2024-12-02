
# Resumenes de chats grupales - Informe Final

## Resumen

El proyecto tiene como objetivo realizar un resumen de los temas más significativos en un chat grupal propio, utilizando datos reales de conversaciones obtenidas de nuestras propias interacciones, en lugar de datasets externos. Para ello, se tendrán en cuenta la relevancia de los mensajes, los temas tratados, y la participación de los usuarios más activos en cada tema. El resumen se generará utilizando LLMs. Luego se buscara mejorar las respuestas utilizando técnicas de identificación de temas como LDA. Se comparran estos resutlados con otros modelos de lenguaje.
<!-- y fine-tunear el modelo con nuestras propias conversaciones. -->

## Hipótesis

<!-- El uso de modelos de LLM combinados con técnicas de detección de temas permite generar resúmenes comprensibles de chats grupales, capturando los temas principales, preservando las aportaciones más relevantes de la conversación -->

Utilizar técnicas de detección de temas como LDA, mejorará la calidad de las respuestas del LLM. Además, se espera que mejoré la calidad al entrenarla con nuestras conversaciones.  



## Relación entre objetivos iniciales y estado final alcanzado
<!-- ## Objetivos preliminares -->

Nuestros objetivos preliminares consistieron en:  
- **Análisis de contenido**: Identificar los temas principales discutidos en el chat grupal mediante técnicas de agrupamiento temático.
- **Compresión de la información**: Generar un resumen corto que conserve la esencia de las discusiones principales sin perder detalles críticos.
- **Resumenes de varios temas**: Actualmente, el programa no es preciso resumiendo muchos mensajes (mas de 15) por lo que se busca filtrar mensajes por tema y buscar resumir en grupos de tema. 

Estos tres primeros objetivos los logramos alcanzar implementando `LDA` para filtrado de temas y así que experimentando pudimos llegar a resultados satisfactorios.

Por otro lado, el objetivo de **Evaluación automática de resumen** no lo pudimos implementar como nos hubiera gustado. Nos tuvimos que limitar a evaluaciones cualitativas juzgadas por nosotros mismos y hacer comparaciones anedóticas sobre los diferentes resultados.

También nos hubiera gustado probar entrenar un modelo con nuestros mensajes, pues notamos que los únicos modelos que lograban resumir bien eran los que fueron entrenados para resumir chats en particular (mas sobre esto adelante).



## Técnicas relevantes exploradas
Para el resumen principal se utilizazó una LLM que busque resumir el chat. En un principio usamos un [modelo de resumenes finetuneado chats](https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary)  
Para el modelado de temas se utilizó análisis de frecuencia de palabras, Latent Dirichlet Allocation y clustering.
<!-- Para el fine-tuning, resumen y evaluación se utilizarán Google Colab y la librería Transformers de Hugging Face. -->  


## Avances en la metodología y evaluación del progreso
En un principio se habrían probado los siguientes modelos de lenguaje
- [Phi 3 - Microsoft](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct): muy pesado y lento para nuestros propósitos
- [RoBERTa2RoBERTa](https://huggingface.co/Narrativa/bsc_roberta2roberta_shared-spanish-finetuned-mlsum-summarization): no se pudo hacer andar
- [Bart](https://huggingface.co/facebook/bart-large-cnn?): Buena performance en general pero no óptima para conversaciones
- [Finetuned bart](https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary): Mejor resultado hasta el momento

<!-- Además, se están haciendo pruebas utilizando métodos como LDA para ayudar al LLM a elegir los temas correctos a resumir. -->

Los resultados base fueron medianamente satisfactorios. En algunos casos el modelo no hace hincapie en lo que consideramos el tema principal o sufría de muchas alucinasiones. 

Cuando implementamos `LDA` se notaba una mejora en el enfoque de los temas pero en algunos casos daba a resumenes muy alucinados y desvíados de cualquier tema.  

De todas maneras, este modelo lo pudimos apreciar por lo liviano que era. Todos los ejemplos que fuimos probando pudimos correrlos de manera local sin necesidad de esperar mucho en la ejecución.

### Pruebas en modelos mas pesados
Con acceso al Centro de Computo de Alto Desempeño (CCAD) de la UNC pudimos hacer pruebas con modelos de lenguajes mas pesados. Los modelos que probamos fueron:
- [SummLlama3.2-3B](https://huggingface.co/DISLab/SummLlama3.2-3B)
- [Pegasus-xsum](https://huggingface.co/google/pegasus-xsum)

Estos dos primeros modelos no estaban entrenados en conversaciones de dialogo (y si lo estaban, eran en formatos de dialogos muy específicos), por lo que los resultados que obtuvimos fueron ensalas de caracteres sin sentido.

Luego probamos con [flan-t5-3b-summarizer](https://huggingface.co/jordiclive/flan-t5-3b-summarizer) el cual esta especializado para hacer resumenes distintos tipos de documentos. La documentación aclara usar el prompt `"Briefly summarize in third person the following conversation:"` para resumir chats.

Los resultados fueron notablemente mejores. Este modelo no alucinó cuando se realizaban resumenes por tema, siempre utilizaba palabras cercanas a lo que se habló sin nunca inventar información.

## Planificación inicial y ejecución efectiva
Al ser la primera vez que trabajamos con un proyecto de esta área las estimaciones que realizamos no fueron de lo mas precisas.  
En un principio, planeamos distribuir el trabajo dentro de 5 semanas, pero solo pudimos implementar los objetivos que nos planteamos en las primeras tres semanas (preparar la LLM inicial, implementar LDA y conectarlo con la LLM). Nos quedó pendiente poder autimatizar las evaluaciones de resultados y entrenar un modelo con nuestros mensajes.  

## Futuro del trabajo
Respondiendo la pregunta: "¿cómo continuarían este proyecto con 5 personas a tiempo completo durante un año?".  
Lo primero que nos gustaría hacer sería fine-tunear un modelo. Por lo que observamos comparando los modelos, el principal factor entre si un modelo servía o no era si estaba entrenado con algún dataset de conversaciones o no. Además, no encontramos modelos especializados en español que anduvieran bien.  

Otra cosa que nos gustaría implementar serían tests automatizados. Aunque anduvimos bien con nuestra evaluación anedótica, nos hubiera gustado probar una mayor combinación de posibles casos (por ejemplo, conversación larga y un tema; conversación larga y varios temas; etc) para tener una mejor idea cuales eran los puntos débiles y fuertes de nuestra implementación.

## Referencias
https://huggingface.co/facebook/bart-large-cnn

https://huggingface.co/kabita-choudhary/finetuned-bart-for-conversation-summary

https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0

https://colab.research.google.com/github/dudaspm/LDA_Bias_Data/blob/main/Latent%20Dirichlet%20Allocation%20(LDA).ipynb

https://huggingface.co/jordiclive/flan-t5-3b-summarizer
