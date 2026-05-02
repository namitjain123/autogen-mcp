from agents.notion_agent import get_notion_agent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat


async def get_notion_team():
    agent= await get_notion_agent()

    team = RoundRobinGroupChat(
            participants=[agent],
            max_turns=5,
            termination_condition=TextMentionTermination('TERMINATE')
        )
    return team