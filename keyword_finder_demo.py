import openai
openai.api_key = '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'

messages = [
#     {"role": "system", "content": "You are a kind helpful assistant."},
]

q = 0
def add_keywords_col(df:pandas.DataFrame)->pandas.DataFrame:
    for i in range(len(df)):
        message = df.loc[i].description
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        df.loc[i].Course_Keywords = chat.choices[0].message.content


while q<3:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    q += 1
