from autogen import AssistantAgent

def get_retriever_agent():
    return AssistantAgent(
        name="RetrieverAgent",
        system_message="你是税务法规的检索模块。请根据关键词，在已有法规库中返回最相关的条款原文。当前为模拟数据，未来会接入向量检索。",
        llm_config={
            "model": "qwen-chat",
            "base_url": "http://localhost:8000/v1",
            "api_key": "fake-key",
            "price": [0, 0]
        }
    )
