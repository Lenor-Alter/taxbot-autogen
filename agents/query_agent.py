from autogen import AssistantAgent

def get_query_agent():
    return AssistantAgent(
        name="QueryAgent",
        system_message="你是一个税务问答助手的问法解析模块，请根据用户输入的问题，判断问题属于哪一类（例如: 开票、认证、抵扣、税率、政策），并提取关键词。",
        llm_config={
            "model": "qwen-chat",
            "base_url": "http://localhost:8000/v1",
            "api_key": "fake-key",
            "price": [0, 0]
        }
    )
