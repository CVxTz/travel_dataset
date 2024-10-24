import os
from pathlib import Path
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

client_medium = ChatOpenAI(
    openai_api_base="https://api.studio.nebius.ai/v1/",
    model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    openai_api_key=os.environ.get("NEBIUS_API_KEY"),
    temperature=0,
)

client_large = ChatOpenAI(
    openai_api_base="https://api.studio.nebius.ai/v1/",
    model="meta-llama/Meta-Llama-3.1-70B-Instruct",
    openai_api_key=os.environ.get("NEBIUS_API_KEY"),
    temperature=0,
)
