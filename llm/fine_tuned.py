from transformers import pipeline
from lda.lda import chat_to_filtered_per_topic


def summarize_chat(chat):
    """
    resume un chat nomas
    """
    summarizer = pipeline(
        "summarization",
        model="kabita-choudhary/finetuned-bart-for-conversation-summary",
    )
    summary = summarizer(chat[:1024], max_length=1024, min_length=30, do_sample=False)
    return summary


def summarize_per_topic(chat):
    """
    resumen por tema encontrado
    """
    summary_list = []
    topic_list = chat_to_filtered_per_topic(chat)
    for n_topic, topics, message_list in topic_list:
        joined_messages = "\n".join(message_list)
        summary = summarize_chat(joined_messages)

        # print(f"Resumen de tema {n_topic}:\n {summary}\n===\n")

        summary_list.append((n_topic, topics, summary, joined_messages))

    return summary_list


def pretty_print_summary_list(summary_list, show_messages=False):
    """
    imprime de manera lejible la lista de resumenes
    """
    text = ""
    for n_tema, temas, resumen, messages in summary_list:
        text += f"""
=============
Tema #{n_tema}
Temas relevantes = {temas}
Resumen:
{resumen}

"""
        if show_messages:
            text += messages
        text += "\n=============\n"
    print(text)


def pretty_string_summary_list(summary_list, show_messages=False):
    """
    imprime de manera lejible la lista de resumenes
    """
    text = ""
    for n_tema, temas, resumen, messages in summary_list:
        text += f"""
=============
Tema #{n_tema}
Temas relevantes = {temas}
Resumen:
{resumen}

"""
        if show_messages:
            text += messages
        text += "\n=============\n"
    return text
