from autogen import AssistantAgent
from tools.law_tool import tax_law_parser

def get_tool_agent():
    agent = AssistantAgent(
        name="ToolAgent",
        system_message="你是一个税法解释专家，请根据法规条款与问法，判断该行为是否合法，并引用条文。",
        llm_config={
            "model": "qwen-chat",
            "base_url": "http://localhost:8000/v1",
            "api_key": "fake-key",
            "price": [0, 0]
        }
    )
    agent.register_function({
        "tax_law_parser": tax_law_parser
    })
    return agent
