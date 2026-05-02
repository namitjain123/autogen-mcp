from dotenv import load_dotenv
import os
load_dotenv()

NGROK_AUTH_TOKEN= os.getenv('NGROK_AUTH_TOKEN')
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

port= 7001


model='gpt-4o'
