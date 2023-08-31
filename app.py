from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from bot_builder import initialize_bots
from bots_needed import bot_list
import logging

app = Flask(__name__)
CORS(app)

created_bots = None
project_logs_dir = None
project_name_dir = None

@app.route('/bots', methods=['GET'])
def get_bots():
    bots = [bot['name'] for bot in bot_list]
    return jsonify(bots)


@app.route('/init_chat', methods=['POST'])
def init_chat():
    global created_bots, project_logs_dir, project_name_dir
    data = request.json
    print(f"data: {data}")

    project_name_input = data['project_name']
    project_description_input = data['project_description']
    user_message = data.get('user_message', None)

    api_key_chatbot = os.getenv("OPENAI_API_KEY_CHATBOT")

    chat_logs_dir = "chat_logs"
    if not os.path.exists(chat_logs_dir):
        os.makedirs(chat_logs_dir)

    project_name_dir = project_name_input.replace(" ", "_")
    project_logs_dir = os.path.join(chat_logs_dir, project_name_dir)
    if not os.path.exists(project_logs_dir):
        os.makedirs(project_logs_dir)

    project_idea = f"{project_name_input} - {project_description_input}"
    assignment_description = (
        f"Help brainstorm and design a project based on this idea: {project_idea} "
        "The tech stack must include React Native and TypeScript for the mobile app and Python for the endpoints. "
        "The database can be whatever suits the project's needs. "
        "Use vector databases for any long term memory if there is a need for an ai agent or chatbot. "
        "Your role is to provide input and suggestions related to your area of expertise."
    )

    selected_bot_names = [name.strip().lower() for name in data['selected_bot_names']]
    print(f'selected_bot_names: {selected_bot_names}')
    selected_bots = [bot for bot in bot_list if bot["name"].lower() in selected_bot_names]
    print(f'selected_bots: {selected_bots}')
    created_bots = initialize_bots(selected_bots, assignment_description, api_key_chatbot)
    print(f'created_bots: {created_bots}')

    output_messages = []
    for chatbot in created_bots:
        prompt = chatbot['bot'].get_prompt()
        bot_name = chatbot['bot'].get_name()
        print(f"chatbot prompt: {prompt}")
        if user_message:
            log_file = os.path.join(project_logs_dir, f'{bot_name}_conversation_log.txt')
            response = chatbot['gpt'].chat(user_message, log_file, project_name_dir)
            output_messages.append({
                "agent": chatbot['bot'].get_name(),
                "message": response,
            })

            print(f"Response: {response}")

    return jsonify(output_messages)

@app.route('/chat', methods=['POST'])
def chat():
    global created_bots, project_logs_dir, project_name_dir
    data = request.json
    print(f"data: {data}")
    user_message = data.get('user_message', None)
    selected_bot_names = [name.strip().lower() for name in data['selected_bot_names']]
    print(f'selected_bot_names: {selected_bot_names}')
    selected_bots = [bot for bot in created_bots if bot['bot'].get_name().lower() in selected_bot_names]
    print(f'selected_bots: {selected_bots}')
    output_messages = []
    for chatbot in selected_bots:
        if user_message:
            bot_name = chatbot['bot'].get_name()
            log_file = os.path.join(project_logs_dir, f'{bot_name}_conversation_log.txt')
            response = chatbot['gpt'].chat(user_message, log_file, project_name_dir)
            output_messages.append({
                "agent": bot_name,
                "message": response,
            })

            print(f"Response: {response}")

    return jsonify(output_messages)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    app.run(debug=True)
