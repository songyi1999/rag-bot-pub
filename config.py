# 机器人 QQ 号
bot_qq = "564523222"

# 管理员 QQ 号
admin_qq = "85245222"

# 允许的聊天回复
chat_type_allow = [
    "private",    # 私聊回复
    "group_at",   # 只有群中 @ 才回复
    "group" ,     # 回复群中所有聊天，这样机器人什么人说话它都会接话
    # "Unkown" ,  # 其它类型聊天也回复
    ]

# 群中@特征字符
at_string = f"[CQ:at,qq={bot_qq}]"

# 允许上传的文件类型
allowed_extensions = [
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".csv",
    ".pdf",
    ".md",
    ".html",
    ".txt",
    ".htm",
    ".py"
]

# go-cqhttp Websocket 监听地址
ws_url = "ws://192.168.66.20:25522"  # 根据go-cqhttp配置文件中的地址修改

# go-cqhttp http API接口地址
http_url = "http://192.168.66.20:25533" # 根据go-cqhttp配置文件中的地址修改

# 源文档路径 
data_path = "./data"

# 分割文档的块大小
chunk_size = 800

# 分割文档时连续部分的重叠区大小
chunk_overlap = 128

# 保存聊天记录的大小
chat_history_size_set = 1024 # 记录越大，每次发给大模型分析的数据越多，上下文越全面。但是会增加响应的时间，而且随着话题的多样复杂，会降低大模型分析的精准度

# 量化后数据保存路径
db_path = "./chroma_db"

# gemini api key 
GOOGLE_API_KEY = "your GOOGLE_API_KEY"
#gemini api key的申请地址：https://makersuite.google.com/app/prompts/new_freeform ，条件：拥有google帐号

# 通义千问 api key
DASHSCOPE_API_KEY  = "your DASHSCOPE_API_KEY"

# 附赠我的 gemini 聊天 API：
GMI_SERVER = 'http://107.175.206.30:5001/chat'

# 模型配置 
## 本地量化模型
embedding_ollama_conf = {
    "base_url": "http://192.168.66.24:11434", 
    "model": "nomic-embed-text"
}
## goole量化模型
embedding_google_conf = {
    "model": "models/embedding-001"
} 
## 本地语言模型 
llm_ollama_conf = {
    "base_url": "http://192.168.66.26:11434", 
    "model": "qwen:7b"
}
## 线上google gemini语言模型
llm_gemini_conf = {
    "model": "gemini-pro",
    "temperature": 0.7
} 
## 线上 通义千问 语言模型
llm_tongyi_conf = {
    "model_name": "qwen-max", # qwen-max-longcontext | qwen-max
    "temperature": 0.7,
    "streaming": False
} 

# 模型选择
model_choice = {
    "embedding":"ollama", # embedding: ollama | google
    "llm": "ollama" # llm: ollama | gemini | tongyi
}






