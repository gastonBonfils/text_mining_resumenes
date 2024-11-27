from llm.fine_tuned import (
    summarize_chat,
    summarize_per_topic,
    pretty_string_summary_list,
)
import os


def process_file(file_path):
    """
    caso que se pasa un archivo
    """
    content = ""
    try:
        with open(file_path) as file:
            content = file.read()
    except:
        print("El archivo no se encontró")
        # exit(1)
        content = None
    return content


def test_particular(archivo):
    """
    dado el nombre del archivo (no la ruta), corre
    - resumir todo junto
    - resumir por tema
    y los escribe a un archivo
    """
    chat = process_file(os.path.join("ejemplos", archivo))

    resumen_crudo = summarize_chat(chat)
    print(resumen_crudo)

    lista_resumenes = summarize_per_topic(chat)

    with open(
        os.path.join("ejemplos_resultados", f"res_{archivo}"), "w+"
    ) as output_file:
        final_text = ""
        final_text += "Resumen Crudo:\n"
        final_text += str(resumen_crudo) + "\n\n"
        final_text += "Resumenes por Tema:\n"
        resuemens_por_tema = pretty_string_summary_list(
            lista_resumenes, show_messages=True
        )
        final_text += resuemens_por_tema
        output_file.write(final_text)


def full_tests():
    for archivo in os.listdir("ejemplos"):
        if archivo.endswith(".txt"):
            test_particular(archivo)


if __name__ == "__main__":
    # Your code here
    # test_particular("telegram_02.txt")
    # print("miau")
    ruta = input(
        "Que archivo te gustaría testear? \nSI NO SE ENCUENTRA EL ARCHIVO SE TESTEA TODOs\n"
    )
    contenido = process_file(ruta)
    if contenido is None:
        full_tests()
    else:
        nombre_archivo = os.path.basename(ruta)
        test_particular(nombre_archivo)
