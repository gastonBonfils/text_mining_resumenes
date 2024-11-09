from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

nltk.download("stopwords")
nltk.download("wordnet")


def fragmentar_chat_telegram(chat):
    """toma un pedazo de chat de telegram y
    devuelve los mensajes en forma de lista

    los chats de telegram son de la forma
    NOMBRE APELLIDO, [MM/DD/AA H:MM AM]
    CONTENIDO
    <espacio vacio>
    NOMBRE APELLIDO....


    Buscamos conservar contenido y nombre
    """
    # patron de mensajes en telegram, regex ♥
    pattern = (
        r"([A-Za-z\s]+), \[\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{2}\s?[APM]{2}\]\n(.+?)\n"
    )

    # Encontrar todas las coincidencias
    matches = re.findall(pattern, chat, re.DOTALL)

    result = [f"{name.strip()}: {content.strip()}" for name, content in matches]

    return result


def lda(lista_mensajes, num_topics=6):
    """
    ORIGINAL
    fragmentos de mensajes (i.e. documentos)
    fragmentos es dictcionario de la forma
    {mes/año : [lista mensajes]}
    busco pasarlo a [lista mensjaes] nomas

    y devuelve un dict de la forma
    {mes/año : modelo_lda_correspodiente}

    CAMBIO
    Paso una lista de mensajes
    y devuelvo el modelito lda
    """
    # limpiamos las stop swords
    stop_words = set(stopwords.words("spanish"))
    lemmatizer = WordNetLemmatizer()

    # rta_lda = {}
    # for m, msjs in fragmentos.items():
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

        rta_lda = {
            "lda_model": lda_model,
            "corpus": corpus,
            "dictionary": dictionary,
            "topics": lda_model.print_topics(),
        }
    return rta_lda


if __name__ == "__main__":
    # fragmentos = [
    #     "Gaston: hola tomi jugamos al futbol??",
    #     "Tomi: hola, dale tengo muchas ganas de jugar",
    #     "Gaston: unas ganas de hacer girar la redonda",
    # ]

    # resultado = lda(fragmentos)
    # for topic in resultado["topics"]:
    #     print(topic)
    with open("ejemplo.txt", "r") as file:
        chat_telegram = file.read()

        # print(fragmentar_chat_telegram(chat_telegram))
        lista_mensajes = fragmentar_chat_telegram(chat_telegram)
        resultado = lda(lista_mensajes, 3)
        for topic in resultado["topics"]:
            print(topic)
        # print(resultado["topics"])
