import os
import sys
from sys import argv
import shutil
import requests
import json
import time

# 文档加工
from langchain_community.document_loaders import DirectoryLoader, UnstructuredWordDocumentLoader, UnstructuredHTMLLoader, UnstructuredMarkdownLoader, PythonLoader 

# 从文件导入
from send import *
from models_load import *

print(f"接收到的参数：{sys.argv}")


embedding_data_path = sys.argv[1]
question = sys.argv[2]
chat_type = str(sys.argv[3])
user_id = str(sys.argv[4])
group_id = str(sys.argv[5])
at = str(sys.argv[6])
source_id = str(sys.argv[7])
user_state = str(sys.argv[8])



print("*" * 40)

print(f"embedding_data_path:", embedding_data_path)
print(f"question:", question)
print(f"chat_type:", chat_type)
print(f"user_id:", user_id)
print(f"group_id:", group_id)
print(f"at:", at)
print(f"source_id:", source_id)
print(f"user_state:", user_state)

print("*" * 40)


def load_documents(data_path):
    print("正在加载" + data_path + "下的所有文档...")
    loader = DirectoryLoader(data_path, show_progress=True, use_multithreading=True)
    loaders = loader.load()
    print(loaders)
    return loaders




# wxid = user_id
# content = f"{load_documents(embedding_data_path)}\n{question}"
# GMI_SERVER_URL = f'{GMI_SERVER}?wxid={wxid}&content={content}'

# print("*" * 40)
# print("正在向llm提交...")

# try:
#     response_text = requests.get(GMI_SERVER_URL).text
#     json_response = json.loads(response_text)
#     reply = json_response.get('reply')
#     print("="*40, "\n",type(reply), reply)
#     response_message = reply
# except Exception as e:
#     response_message = "LLM响应错误"

# print("*" * 40)
# print(f"答案： {response_message}")

try:
    query = f"{load_documents(embedding_data_path)}\n{question}"
    response_message = chat_generic_langchain(source_id, query, user_state)
except Exception as e:
    response_message = f"错误：{e}"

print("*" * 40)
print(f"答案： {response_message}")


# 发送消息
answer_action(chat_type, user_id, group_id, at, response_message)






