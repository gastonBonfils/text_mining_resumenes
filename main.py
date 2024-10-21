import argparse
from fine_tuned import summarize_chat
import sys


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
        exit(1)
    return content


def process_input():
    """
    caso que se pasa sin archivo
    """
    # chat = input("Pega tu chat: ")
    print("Copia el chat y luego toca Ctrl + D")
    msg = sys.stdin.readlines()
    chat = "".join(msg)
    # print()
    # exit()
    return chat


def main():
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(description="Procesar un archivo de texto.")

    # Añadir un argumento para el archivo
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="La ruta al archivo que se va a procesar.",
        required=False,
    )

    # Parsear los argumentos
    args = parser.parse_args()

    # Llamar a la función para procesar el archivo
    chat = ""
    if args.file is None:
        chat = process_input()
    else:
        chat = process_file(args.file)

    summary = summarize_chat(chat)

    print(summary)


if __name__ == "__main__":
    main()
