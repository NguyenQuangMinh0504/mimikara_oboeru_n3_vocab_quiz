def get_example(word: str) -> str:
    """Return example of word using Open AI"""
    from openai import OpenAI
    client = OpenAI(api_key="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")
    messages = [
        {"role": "user",
         "content": "Đặt câu tiếng Nhật với từ {}. Giải thích ý nghĩa câu và các hán tự dùng trong câu.".format(word),
         }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content
