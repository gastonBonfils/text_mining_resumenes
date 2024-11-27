from gensim import corpora
from gensim.models import LdaModel
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re
import unicodedata

nltk.download("stopwords")
nltk.download("wordnet")

from lda.chat_parser import fragmentar_chat_cualquiera


def normalizar_texto(texto):
    """
    quita tildes y lo pasa a miniscula
    """
    # Normalizamos el texto para separar las letras acentuadas
    texto_normalizado = unicodedata.normalize("NFD", texto)

    # Filtramos las letras acentuadas (que tienen una "combinación" de caracteres como la tilde)
    # y las transformamos a su versión sin tilde.
    texto_sin_tildes = "".join(
        [c for c in texto_normalizado if unicodedata.category(c) != "Mn"]
    )

    # Devolvemos el texto sin tildes
    texto_minus = re.sub(r"[,\.!?]", "", texto_sin_tildes.lower())
    return texto_minus


def model_lda(lista_mensajes, caso_normal, num_topics=6):
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
        contenido = msj
        # si es un caso normal, entonces matchea, sacando el autor
        # sino, el contenido es el mensaje
        if caso_normal:
            match = re.search(
                r"^.*?:\s*(.+)", msj
            )  # Buscar el contenido después del nombre del autor
            if match:
                contenido = match.group(1)
            else:
                contenido = ""

        # filtro la puntuación y los paso a minuscula
        # contenido_sin_tilde = normalizar_texto(contenido)
        # contenido_sin_puntuacion = re.sub(r"[,\.!?]", "", contenido_sin_tilde.lower())
        contenido_normalizado = normalizar_texto(contenido)
        texts.append(
            [
                lemmatizer.lemmatize(palabra)
                for palabra in re.findall(r"\b\w+\b", contenido_normalizado)
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
        # rta_lda = lda_model
    return lda_model


def message_list_per_topic(topics_list, message_list):
    """
    dado la lista de temas (topics_list) de la forma
    [(n_tema [('tema', porcentaje)]), ... ]
    y la lista de mensajes
    devuele una lista de la forma
    [(n_tema, [lista de temas relevantes (para testing)] , [lista de mensajes relevantes al tema]), ....]
    """
    final_list = []
    for n_tema, lista_temas in topics_list:
        # ordenamos por relevancia la lista de temas para quedarnos con
        # el 70%? mas relevante
        lista_temas.sort(key=lambda x: x[1], reverse=True)
        suma_porcentaje = 0.0
        temas_relevantes = []

        for tema, porcentaje in lista_temas:
            # si agarré el top x%  ya la corto
            if suma_porcentaje >= 0.5:
                break
            suma_porcentaje += porcentaje

            # me voy quedando con los temas mas relevantes
            temas_relevantes.append(tema)

        # una vez que salí del bucle (i.e. tengo los temas relevantes)
        # hago una lista de mensajes filtrada
        mensajes_relevantes = [
            msj
            for msj in message_list
            if any(tema in normalizar_texto(msj) for tema in temas_relevantes)
        ]
        final_list.append((n_tema, temas_relevantes, mensajes_relevantes))

    return final_list


def chat_to_filtered_per_topic(chat):
    """
    esta funcion se encarga de ir llamando todo proceduralmente
    deberia ser la unica llamada desde afuera

    # chat: string del chat
    #     ya se asume que se parseo el path o el copia_pega

    """

    lista_mensajes, caso_normal = fragmentar_chat_cualquiera(chat)

    # no se cuantos topics deberia ser lo ideal
    lda_model = model_lda(lista_mensajes, caso_normal, num_topics=6)
    topics = lda_model.show_topics(formatted=False)
    lista_filtrada = message_list_per_topic(topics, lista_mensajes)
    return lista_filtrada


if __name__ == "__main__":
    """
    el main funciona como para debuggear
    """
    # with open("ejemplo.txt", "r") as file:
    #     chat_telegram = file.read()

    #     # print(fragmentar_chat_telegram(chat_telegram))
    #     lista_mensajes = fragmentar_chat_cualquiera(chat_telegram)
    #     lda_model = model_lda(lista_mensajes, 3)

    #     topicos = lda_model.show_topics(formatted=False)
    #     print(topicos)

    #     lista_filtrada = message_list_per_topic(topicos, lista_mensajes)

    print("=====")
    #     print(lista_filtrada)
