import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Any doubts in recipe ASK ME! "}]

def CustomChatGPT(Any_doubts_in_recipe_ASK_ME):
    messages.append({"role": "user", "content": Any_doubts_in_recipe_ASK_ME})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Recipe Chatbot",
    description="Enter your doubts in the recipe, and the chatbot will assist you.",
    examples=[["How much salt should I add to the recipe?"],
    ["How to make briyani for 4 people?"]],
    )

demo.launch(share=True)

