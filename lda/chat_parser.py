import re


# def fragmentar_chat_telegram(chat):
#     """toma un pedazo de chat de telegram y
#     devuelve los mensajes en forma de lista

#     los chats de telegram son de la forma
#     NOMBRE APELLIDO, [MM/DD/AA H:MM AM]
#     CONTENIDO
#     <espacio vacio>
#     NOMBRE APELLIDO....


#     Buscamos conservar contenido y nombre
#     """
#     whatsapp_phone_pattern = r"\[\d{1,2}/\d{1,2} \d{1,2}:\d{2}\] (.*?): (.*)"

#     # patron de mensajes en telegram, regex ♥
#     telegram_pattern = (
#         r"([A-Za-z\s]+), \[\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{2}\s?[APM]{2}\]\n(.+?)\n"
#     )

#     # Encontrar todas las coincidencias
#     matches = re.findall(telegram_pattern, chat, re.DOTALL)

#     # lista de la forma
#     # [NOMBRE APELLIDO: CONTENIDO]
#     message_list = [f"{name.strip()}: {content.strip()}" for name, content in matches]

#     return message_list


def fragmentar_chat_cualquiera(chat):
    """
    dado un chat de Telegram o Whatsapp del celular guarda cada mensaje en una lista

    se agrega la flag "caso_normal" para los casos que no son cubiertos por
    los patrones de abajo (Telegram o Whatsapp celular)

    """
    whatsapp_phone_pattern = r"\[(\d{1,2}/\d{1,2} \d{2}:\d{2})\] (\w+): (.+)"

    # patron de mensajes en telegram, regex ♥
    telegram_pattern = (
        r"([A-Za-z\s]+), \[\d{1,2}/\d{1,2}/\d{2} \d{1,2}:\d{2}\s?[APM]{2}\]\n(.+?)\n"
    )

    whatasapp_02_pattern = (
        r"\[\d{1,2}:\d{2} (?:a\.m\.|p\.m\.), \d{1,2}/\d{1,2}/\d{4}\] ([^:]+): (.+)"
    )

    matches_wasap = re.findall(whatsapp_phone_pattern, chat)
    matches_telegram = re.findall(telegram_pattern, chat, re.DOTALL)
    matches_wasap_02 = re.findall(whatasapp_02_pattern, chat)

    telegram_list = [
        f"{name.strip()}: {content.strip()}" for name, content in matches_telegram
    ]

    whatsapp_list = [
        f"{name.strip()}: {content.strip()}" for fecha, name, content in matches_wasap
    ]
    whatsapp_02_list = [
        f"{name.strip()}: {content.strip()}" for name, content in matches_wasap_02
    ]
    caso_normal = True
    message_list = telegram_list + whatsapp_list + whatsapp_02_list

    # esto sucede si ninguno tiene hace match, entonces es otro formato
    # por ahora se asume que este formato viene sin fechas
    if message_list == []:
        message_list = chat.split("\n")
        caso_normal = False
        # message_list = list(filter(lambda x: x != "", message_list))

    return message_list, caso_normal


if __name__ == "__main__":
    with open("ejemplos/telegram_corto.txt", "r") as file:
        chat_telegram = file.read()

        # print(fragmentar_chat_telegram(chat_telegram))
        print(fragmentar_chat_cualquiera(chat=chat_telegram))

    print("==========")
    with open("ejemplos/whatsapp_corto.txt", "r") as file:
        chat_wasap = file.read()

        # print(fragmentar_chat_telegram(chat_telegram))
        print(fragmentar_chat_cualquiera(chat=chat_wasap))
