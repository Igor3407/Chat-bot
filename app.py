import chainlit as cl
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Загрузка модели и токенизатора
model_name = "sberbank-ai/rubert-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

@cl.on_message
def answer_question(question: str):
    # Пример текста, на который будем отвечать
    context = "Ваш контекст для ответа на вопросы."

    # Токенизация входных данных
    inputs = tokenizer(question, context, return_tensors='pt', truncation=True, padding=True)

    # Получение предсказания
    with torch.no_grad():
        outputs = model(**inputs)
        answer_start = torch.argmax(outputs.start_logits)  # Начало ответа
        answer_end = torch.argmax(outputs.end_logits) + 1  # Конец ответа

    # Получение текста ответа
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][answer_start:answer_end]))

    # Возврат результата
    cl.Message(f"Ответ: {answer}")