from transformers import pipeline

# summarizer = pipeline(
#     "summarization", model="kabita-choudhary/finetuned-bart-for-conversation-summary"
# )


# # texto = ""
# # with open("./ejemplo2.txt", "r", encoding="utf-8") as chat:
# #     texto += chat.read()

# # print(summarizer(texto[:1024], max_length=1024, min_length=30, do_sample=False))


def summarize_chat(chat):
    # print("El input fue: ", chat)
    summarizer = pipeline(
        "summarization",
        model="kabita-choudhary/finetuned-bart-for-conversation-summary",
    )
    summary = summarizer(chat[:1024], max_length=1024, min_length=30, do_sample=False)
    return summary
