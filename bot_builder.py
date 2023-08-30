# bot_builder.py
from bot_prompt_template import BotPromptTemplate
from chat_gpt import ChatGPT

def initialize_bots(bot_list, assignment_description, api_key):
    created_bots = []
    
    for i, bot_params in enumerate(bot_list):
        bot = BotPromptTemplate(
            name=bot_params["name"],
            role=bot_params["role"],
            expertise_areas=bot_params["expertise_areas"],
            key_skills=bot_params["key_skills"],
            task_description=bot_params["task_description"],
            assignment_description=assignment_description
        )

        bot_prompt = bot.get_prompt()

        gpt = ChatGPT(api_key, bot_prompt, retries=5)
        
        chatbot = { "bot": bot, "gpt": gpt }

        created_bots.append(chatbot)

    return created_bots
