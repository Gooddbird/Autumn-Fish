from langgraph.graph import add_messages
from pydantic import BaseModel
from langchain.messages import AnyMessage
from typing import List
from typing_extensions import Annotated


class AgentState(BaseModel):
    use_input: str
    messages: Annotated[List[AnyMessage], add_messages]
    tools: List[str]
    skills: List[str]