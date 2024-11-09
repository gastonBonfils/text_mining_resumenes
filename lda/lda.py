from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

nltk.download("stopwords")
nltk.download("wordnet")

from chat_parser import fragmentar_chat_telegram


def model_lda(lista_mensajes, num_topics=6):
    """
    CAMBIO
    Paso una lista de mensajes de la forma [AUTOR: CONTENIDO]
    y devuelvo el modelito lda

    la lda se va a quedar solo con el contenido, ignorando al atuor
    se asume que no traen fecha
    """
    # limpiamos las stop swords
    stop_words = set(stopwords.words("spanish"))
    lemmatizer = WordNetLemmatizer()

    # procesamiento
    texts = []
    for msj in lista_mensajes:
        # Extraer solo el contenido del mensaje
        match = re.search(
            r"^.*?:\s*(.+)", msj
        )  # Buscar el contenido después del nombre del autor
        if match:
            contenido = match.group(1)
        else:
            contenido = ""

        # filtro la puntuación y los paso a minuscula
        contenido_sin_puntuacion = re.sub(r"[,\.!?]", "", contenido.lower())
        texts.append(
            [
                lemmatizer.lemmatize(palabra)
                for palabra in re.findall(r"\b\w+\b", contenido_sin_puntuacion)
                if palabra not in stop_words and len(palabra) > 2
            ]
        )

        # diccionario
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]

        # entrenar
        lda_model = LdaModel(
            corpus, num_topics=num_topics, id2word=dictionary, passes=15
        )

        # rta_lda = {
        #     "lda_model": lda_model,
        #     "corpus": corpus,
        #     "dictionary": dictionary,
        #     "topics": lda_model.print_topics(),
        # }
        rta_lda = lda_model
    return rta_lda


def message_list_per_topic(rta_lda, message_list):
    ...
    # return list_per_topic


if __name__ == "__main__":
    with open("ejemplo.txt", "r") as file:
        chat_telegram = file.read()

        # print(fragmentar_chat_telegram(chat_telegram))
        lista_mensajes = fragmentar_chat_telegram(chat_telegram)
        lda_model = model_lda(lista_mensajes, 3)

        topicos = lda_model.show_topics(formatted=False)
        print(topicos)
