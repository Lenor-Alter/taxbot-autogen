from autogen import GroupChat, GroupChatManager
from agents.query_agent import get_query_agent
from agents.retriever_agent import get_retriever_agent
from agents.tool_agent import get_tool_agent
from agents.answer_agent import get_answer_agent

query_agent = get_query_agent()
retriever_agent = get_retriever_agent()
tool_agent = get_tool_agent()
answer_agent = get_answer_agent()

group_chat = GroupChat(
    agents=[query_agent, retriever_agent, tool_agent, answer_agent],
    messages=[],
    max_round=5,
)
manager = GroupChatManager(
    groupchat=group_chat,
    name="TaxBotManager",
    llm_config={
        "model": "qwen-chat",
        "base_url": "http://localhost:8000/v1",
        "api_key": "fake-key",
        "price": [0, 0]
    },
    is_termination_msg=lambda msg: "最终答复" in msg.get("content", "") or "已解答" in msg.get("content", "")
)

manager.initiate_chat(
    query_agent,
    message="小规模纳税人能不能开13%的专票？"
)
