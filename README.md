# 税务智能问答系统（taxbot-autogen）

## 项目简介

本项目是一个基于多智能体（Multi-Agent）协作的税务问答机器人，能够自动解析用户税务相关问题，检索法规，调用工具进行判断，并输出结构化、可追溯的最终答复。系统采用大语言模型（如 Qwen-Chat）作为智能体核心，支持本地大模型推理服务。

---

## 系统结构与工作流程

整体流程如下（详见 `autogen-agent-flow.txt`）：

```
                +------------------+
                |   用户提问       |
                +--------+---------+
                         |
                         v
                +--------+---------+
                |  QueryAgent      | ← 问法分类、关键词提取
                +--------+---------+
                         |
              +----------+----------+
              |                     |
              v                     v
+--------------------+    +--------------------+
|   RetrieverAgent   |    |  ToolAgent         | ← 法规检索、工具判断
+--------------------+    +--------------------+
              \                     /
               \                   /
                \                 /
                 v               v
                +------------------+
                |  AnswerAgent     | ← 结构化输出+条文引用
                +------------------+
                         |
                         v
                +------------------+
                | 最终答复         |
                +------------------+
```

---

## 主要功能模块

### Agents（智能体）

- **QueryAgent**：解析用户问题，分类并提取关键词。
- **RetrieverAgent**：根据关键词检索最相关的法规条文（目前为模拟数据）。
- **ToolAgent**：调用税法工具函数，对法规条文和问题进行合法性判断。
- **AnswerAgent**：综合分析，生成结构化答复，包含结论、引用法规、解释说明，并在合适时输出"最终答复"以终止对话。

### Tools（工具）

- **law_tool.py**：提供 `tax_law_parser` 工具函数，输入问题和法规片段，输出判断结果（可扩展为 LLM 或规则引擎）。

### Data（数据）

- **mock_tax_laws.json**：模拟税法数据（可扩展为真实法规库）。

---

## 安装与环境准备

1. **依赖安装**

   建议使用 Python 3.10+，并安装如下依赖（可根据实际情况补充 requirements.txt）：

   ```bash
   pip install requests
   # 以及 fastchat、autogen 等相关依赖
   ```

2. **启动本地大模型服务**

   按照 `start-qwen-service.txt` 的说明，分别在三个终端依次执行：

   ```bash
   # 1. 启动 controller
   python3 -m fastchat.serve.controller

   # 2. 启动 model worker
   python3 -m fastchat.serve.model_worker --model-path /root/FastChat/qwen-chat --device cuda

   # 3. 启动 OpenAI 兼容入口
   python3 -m fastchat.serve.openai_api_server --host 127.0.0.1 --port 8000
   ```

---

## 使用方法

1. **运行主程序**

   ```bash
   python run.py
   ```

   系统会自动发起一轮多智能体协作问答，输出结构化的税务答复，并在出现"最终答复"时自动终止。

2. **自定义提问**

   可在 `run.py` 中修改 `manager.initiate_chat` 的 `message` 参数，输入你关心的税务问题。

---

## API 测试示例

你可以用 `test_openai_api.py` 脚本测试大模型 API 是否可用：

```python
import requests

url = "http://127.0.0.1:8000/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fake-key"
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
```

---

## 各模块说明

- `agents/query_agent.py`：问法解析
- `agents/retriever_agent.py`：法规检索
- `agents/tool_agent.py`：工具调用
- `agents/answer_agent.py`：结构化答复
- `tools/law_tool.py`：税法判断工具
- `data/mock_tax_laws.json`：法规数据（可扩展）

---

## 常见问题与优化建议

- **如何终止对话？**  
  在 `AnswerAgent` 的回复中包含"最终答复"或"已解答"，并在 `GroupChatManager` 初始化时设置 `is_termination_msg` 参数即可自动终止。

- **如何扩展法规库？**  
  可将真实法规数据导入 `data/` 目录，并完善 `RetrieverAgent` 和 `law_tool.py` 的检索与解析逻辑。

- **如何接入更强大的大模型？**  
  修改各 agent 的 `llm_config`，指向你部署的任意 OpenAI 兼容大模型服务即可。

---

## 后续改进方向

- 接入真实的法规知识库和向量检索
- 工具函数升级为 LLM 或规则引擎
- 增加多轮追问、上下文记忆等高级功能
- 丰富 API 接口，支持 Web UI 或微信/钉钉等多端接入

---

如有任何问题或建议，欢迎随时反馈！

---

你可以直接将以上内容保存为 `README.md` 文件，方便用户和开发者查阅。  
如果需要英文版或更详细的技术细节，也可以随时告诉我！ 
