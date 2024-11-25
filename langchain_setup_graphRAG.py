# from langchain.document_loaders import TextLoader
from langchain.document_loaders.text import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from graphRAG import GraphRAG
from langchain.document_loaders import TextLoader
# Загрузка документа
loader = TextLoader("pp138.txt")
documents = loader.load()

# Разделение текста на управляемые части
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
split_documents = text_splitter.split_documents(documents)

# Инициализация графа знаний
graph = GraphRAG()

# Добавление документов в граф
for doc in split_documents:
    graph.add_document(doc)

# Построение графа
graph.build_graph()

# Сохранение графа в файл
graph.save("knowledge_graph.json")