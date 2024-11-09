import re


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
    telegram_pattern = (
        r"([A-Za-z\s]+), \[\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{2}\s?[APM]{2}\]\n(.+?)\n"
    )

    # Encontrar todas las coincidencias
    matches = re.findall(telegram_pattern, chat, re.DOTALL)

    # lista de la forma
    # [NOMBRE APELLIDO: CONTENIDO]
    message_list = [f"{name.strip()}: {content.strip()}" for name, content in matches]

    return message_list


if __name__ == "__main__":
    with open("ejemplo.txt", "r") as file:
        chat_telegram = file.read()

        print(fragmentar_chat_telegram(chat_telegram))
