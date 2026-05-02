from config.settings import NOTION_TOKEN
from autogen_ext.tools.mcp import StdioServerParams, mcp_server_tools

async def get_notion_mcp_tools():
    params = StdioServerParams(
        command='npx',
        args=["-y",'mcp-remote',"https://mcp.notion.com/mcp"],
        env={
            'NOTION_TOKEN':NOTION_TOKEN
        },
        read_timeout_seconds=20
    )
        

    mcp_tools = await mcp_server_tools(server_params=params)
    return mcp_tools