---
ChatBot Chain
Описание
ChatBot — это интерактивный чат-бот, разработанный с использованием нейросетевых технологий. Он предназначен для предоставления информации и развлечения.
---

## Создание и активация виртуального окружения
```bash
cd ChatBot
python -m venv .venv
source .venv/bin/activate # for mac/linux
source .venv/Scripts/activate # for win
```
## Установка зависимостей
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U -r requirements.txt
```

## Скачать сервер Ollama и запустить его (для работы под Windows)
```
https://ollama.com/

```
## Если сервер Ollama уже есть запусть через командную строку
```cmd
ollama serve
```

## Mistral for GraphRAG Inference
ollama pull mistral

## Nomic-Embed-Text for GraphRAG Embedding
ollama pull nomic-embed-text

## LLama3 for Autogen Inference
ollama pull llama3

## Установить и запустить сервер Ubuntu
Использование WSL
Включите WSL:
Откройте PowerShell от имени администратора и выполните команду:
powershell

wsl --install
Если у вас уже установлен WSL, убедитесь, что он обновлен:
powershell

wsl --update
Установите Ubuntu:
После установки WSL, откройте Microsoft Store и найдите "Ubuntu".
Выберите и установите версию Ubuntu (например, Ubuntu 20.04 или 22.04).
Запустите Ubuntu:
После установки запустите Ubuntu из меню "Пуск".
При первом запуске вам будет предложено создать пользователя и пароль.
Обновите пакеты:
В терминале Ubuntu выполните команды:
sudo apt update
sudo apt upgrade
sudo apt install [если требуется дополнительный пакетъ]
Запустите Apache:
sudo service apache2 start

## В терминале PyCharm перейдите в терминал Ubuntu 24

## Установка Conda

wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

bash Anaconda3-2024.10-1-Linux-x86_64.sh

## Активация Conda

eval "$(/home/user/anaconda3/bin/conda shell.bash hook)"

# Создание и активация conda_environment
conda create -n conda_env python=3.12
conda activate conda_env

## Установка зависимостей
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -U -r requirements.txt
```
pip install --upgrade langchain_ollama

## Доступ на HuggingFace
Чтобы получить новый токен API для Hugging Face, выполните следующие шаги:
1. Войдите в аккаунт Hugging Face
Перейдите на Hugging Face.
Нажмите на кнопку "Sign in" (Войти) в правом верхнем углу и введите свои учетные данные.
2. Перейдите в настройки
После входа в систему нажмите на свой аватар в правом верхнем углу.
Выберите "Settings" (Настройки) из выпадающего меню.
3. Получите токен
В настройках найдите раздел "Access Tokens" (Токены доступа).
Нажмите на кнопку "New token" (Новый токен).
Введите имя для вашего нового токена и выберите необходимые права доступа (например, для чтения, записи и т.д.).
Нажмите "Generate" (Сгенерировать).
4. Сохраните токен
Скопируйте сгенерированный токен и сохраните его в безопасном месте. Не делитесь своим токеном с другими людьми, так как он предоставляет доступ к вашему аккаунту.
Примечание
Если у вас уже есть токен, вы можете удалить его и создать новый, если нужно. Просто убедитесь, что у вас нет активных процессов, использующих старый токен, когда вы его удаляете.

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

## Загружаем модель
ollama pull llama3.2

## Запускаем 

chainlit run ollama.py


`

# ChainLit Local LLM Integration

This repository contains examples of integrating various local Large Language Models (LLMs) with ChainLit, a framework for building interactive applications with LLMs. Each example demonstrates how to set up a different LLM for use within the ChainLit environment.

## Description

The examples provided showcase how to integrate different LLMs, such as `Ollama`, `LlamaCpp`, and `HuggingFacePipeline`, into the ChainLit framework. These integrations allow users to interact with the models through a chat interface, where the models can provide responses based on their specialized capabilities, such as generating source code or providing historical information.

## Quickstart

To get started with these examples, follow the steps below:

1. Clone the repository to your local machine.
2. Install the required dependencies for ChainLit and the respective LLMs.
3. Choose the LLM you want to work with and navigate to its corresponding Python file.
4. Update any necessary paths or configurations, such as the `MODEL_PATH` for `LlamaCpp`.
5. Run the ChainLit application to start interacting with the LLM through the chat interface.

### Function Definitions

#### Ollama Integration (`ollama.py`)

- `on_chat_start`: Initializes the chat session with a historical context prompt.
- `on_message`: Streams the user's message to the model and sends back the model's response.

#### LlamaCpp Integration (`llama-cpp.py`)

- `instantiate_llm`: Loads the LlamaCpp model with the specified configuration.
- `main` (decorated with `@cl.on_chat_start`): Sets up the conversation chain with a system prompt for code generation.
- `main` (decorated with `@cl.on_message`): Handles incoming messages and generates responses using the conversation chain.

#### Llama2 Chat Integration (`llama2-chat.py`)

- `load_llama`: Loads the Llama2 model from HuggingFace with the specified tokenizer and streamer.
- `main` (decorated with `@cl.on_chat_start`): Initializes the LLM chain with a prompt for answering questions.
- `run`: Processes incoming messages and provides responses using the LLM chain.

