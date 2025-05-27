def tax_law_parser(question: str, law_snippet: str) -> str:
    # mock version，之后可以接 LLM 或 rule-based 解析
    if "小规模" in question and "13%" in question:
        return "根据《国家税务总局公告2023年第6号》，小规模纳税人不能开13%专票，属于违规行为。"
    return "暂无法判断，请补充更多背景。"
