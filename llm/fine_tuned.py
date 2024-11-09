from transformers import pipeline
from lda.lda import chat_to_filtered_per_topic

TELEGRAM = 0
WHATSAPP = 1


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
    topic_list = chat_to_filtered_per_topic(chat, type=TELEGRAM)
    for n_topic, topics, message_list in topic_list:
        joined_messages = "\n".join(message_list)
        summary = summarize_chat(joined_messages)

        # print(f"Resumen de tema {n_topic}:\n {summary}\n===\n")

        summary_list.append((n_topic, topics, summary))

    return summary_list


def pretty_print_summary_list(summary_list):
    """
    imprime de manera lejible la lista de resumenes
    """
    for n_tema, temas, resumen in summary_list:
        print(
            f"""
=============
Tema #{n_tema}
Temas relevantes = {temas}
Resumen:
{resumen}
=============
"""
        )
