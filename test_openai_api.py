import requests

url = "http://127.0.0.1:8000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fake-key"  # 你的api_key，和tool_agent.py里一致
}
data = {
    "model": "qwen-chat",
    "messages": [
        {"role": "user", "content": "你好，请简单介绍一下你自己。"}
    ]
}

response = requests.post(url, headers=headers, json=data)
print("状态码:", response.status_code)
print("返回内容:", response.json())