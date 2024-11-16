import chainlit as cl
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

# Загрузка токенизатора и модели
model_name = "sberbank-ai/rubert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
@cl.on_message
def handle_message(message: str):
    cl.Message(f"Вы написали: {message}")