import os
from openai import OpenAI
import gradio
client = OpenAI(
    api_key=os.environ.get("open_api_key"),
)
messages = [{"role": "system", "content": "You are a web developer"}]
def CustomGpt(user_input):
    messages.append({"role": "user", "content": user_input})
    chat_completion = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo",
    )
    reply= chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=CustomGpt, inputs = "text", outputs = "text", title ="THE CHATBOT")

demo.launch(share=True)
