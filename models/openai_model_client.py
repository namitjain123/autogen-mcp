from config.settings import model, OPENAI_API_KEY
from autogen_ext.models.openai import OpenAIChatCompletionClient

def get_openai_model_client():
    model_client = OpenAIChatCompletionClient(model=model,
                                       api_key=OPENAI_API_KEY)
    
    return model_client