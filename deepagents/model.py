from langchain_openai import ChatOpenAI


def get_default_model():
    return ChatOpenAI(model_name="o3")
