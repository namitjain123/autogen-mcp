from teams.notion_team import get_notion_team
import asyncio
from flask import Flask, jsonify, request
from pyngrok import ngrok
from flask_cors import CORS
from config.settings import port, NGROK_AUTH_TOKEN
import traceback

async def run_task(task: str) -> str:
    print("Starting run_task")
    team = await get_notion_team()
    print("Team created successfully")

    output = []
    async for msg in team.run_stream(task=task):
        print("STREAM MSG:", msg)
        output.append(str(msg))

    return '\n \n \n'.join(output)


app =Flask(__name__)
CORS(app)

@app.route('/health',methods=['GET'])
def health():
    return jsonify({"status":"ok","message":"Notion MCP Flask app is live"}),200

@app.route('/',methods=['GET'])
def root():
    return jsonify({'message':'MCP Notion app is live , use /health or /run to work'}),200

@app.route('/run', methods=['POST'])
def run():
    try:
        data = request.get_json()

        task = data.get('task')

        if not task:
            return jsonify({'error':"Missing Task"}),400
        
        print(f"Got the task {task}")

        result = asyncio.run(run_task(task=task))

        return jsonify({'status':'sucess','result':result}),200
    

    except Exception as e:
        return jsonify({'status':'error','result':str(e)}),500
    

if __name__== '__main__':
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    public_url = ngrok.connect(port)
    print(f"Public url : {public_url} \n\n")

    app.run(port=port)
