from autogen import AssistantAgent

def get_answer_agent():
    return AssistantAgent(
        name="AnswerAgent",
        system_message=(
            "你是税务问答的答复生成模块。请综合之前分析内容，生成结构化回复，包含：结论、引用法规、解释说明。"
            "如果你认为问题已经完全解答，请在回复最后加上“最终答复”四个字。"
        ),
        llm_config={
            "model": "qwen-chat",
            "base_url": "http://localhost:8000/v1",
            "api_key": "fake-key",
            "price": [0, 0]
        }
    )
