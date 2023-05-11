# pyagents.py
from colorama import Fore, Style, init
import logging
import os

from dotenv import load_dotenv
from bot_builder import initialize_bots
from bots_needed import bot_list

# Initialize colorama
init()

def print_colored(agent, text):
    agent_colors = {
        "Customer": Fore.LIGHTGREEN_EX,
        "Mx.Pythonista": Fore.YELLOW,
        "Mx.PyDev": Fore.CYAN,
        "Dr.Data": Fore.GREEN,
        "Professor.AI": Fore.MAGENTA,
        "Mx.ReactNative": Fore.RED,
        "Mx.NativeDev": Fore.BLUE,
        "Mx.TechPM": Fore.WHITE,
        "Mx.Collab": Fore.LIGHTBLUE_EX,
        "Mx.Security": Fore.LIGHTBLACK_EX,
    }
    color = agent_colors.get(agent, "")
    print(color + f"{agent}: {text}" + Style.RESET_ALL, end="")

if __name__ == "__main__":
    # Set logging level
    logging.basicConfig(level=logging.INFO)

    # Load environment variables
    load_dotenv()

    # Set chatbot prompts and get the API keys from environment variables
    # Remember to set these variables in your environment or .env file
   
    api_key_chatbot1 = os.getenv("OPENAI_API_KEY_CHATBOT1")
    api_key_chatbot2 = os.getenv("OPENAI_API_KEY_CHATBOT2")
    api_key_chatbot3 = os.getenv("OPENAI_API_KEY_CHATBOT3")
    api_key_chatbot4 = os.getenv("OPENAI_API_KEY_CHATBOT4")
    api_key_chatbot5 = os.getenv("OPENAI_API_KEY_CHATBOT5")
    api_key_chatbot6 = os.getenv("OPENAI_API_KEY_CHATBOT6")
    api_key_chatbot7 = os.getenv("OPENAI_API_KEY_CHATBOT7")
    api_key_chatbot8 = os.getenv("OPENAI_API_KEY_CHATBOT8")
    api_key_chatbot9 = os.getenv("OPENAI_API_KEY_CHATBOT9")

    # Take user input for the project idea and details
    print("\nPlease enter your project name:")
    project_name_input = input()
    project_name_dir = project_name_input.replace(" ", "_")  # Replace spaces with underscores
    if not os.path.exists(project_name_dir):  # Create the project directory if it doesn't exist
        os.makedirs(project_name_dir)

    print("\nPlease enter the project description:")
    project_description_input = input()

    project_idea = f"{project_name_input} - {project_description_input}"

    # Create list of api keys
    api_keys = [ api_key_chatbot1, api_key_chatbot2, api_key_chatbot3, api_key_chatbot4, api_key_chatbot5, api_key_chatbot6, api_key_chatbot7, api_key_chatbot8, api_key_chatbot9 ]

    # Update the assignment_description for each bot with the user's project idea
    assignment_description=f"Help brainstorm and design a project based on this idea: {project_idea} The tech stack must include React Native and TypeScript for the mobile app and Python for the endpoints. The database can be whatever suits the project's needs. Use vector databses for any long term memory if there is a need for an ai agent or chatbot. Your role is to provide input and suggestions related to your area of expertise."

    # List of all available bots
    all_bots = bot_list

    # Display available bots and their roles
    print("\nAvailable bots and their roles:\n")
    for bot in all_bots:
        print(f"{bot['name']}: {bot['role']}")

    # Ask user which bots are needed for their project
    print("\nWhich bots are needed for your project? Please enter the names (as listed above), separated by commas:")
    selected_bot_names = input().split(',')

    # Remove any leading/trailing white space from the bot names and convert to lowercase
    selected_bot_names = [name.strip().lower() for name in selected_bot_names]

    # Filter the full bot list to only include the selected bots
    selected_bots = [bot for bot in all_bots if bot["name"].lower() in selected_bot_names]

    # Create the bots
    created_bots = initialize_bots(selected_bots, assignment_description, api_keys)

    # Number of turns for each chatbot
    num_turns = 20

    # Start the conversation with the user's project idea
    user_message = f"Hello Everyone. Here's my project idea: {project_idea}. Let's start brainstorming!"

    for i in range(num_turns):

        turn_number = i + 1

        print(f"Turn {turn_number}:")

        # Define log file for the conversation
        log_file = os.path.join(project_name_dir, f'turn_{turn_number}_conversation_log.txt')
        
        # Save log file for the conversation
        with open(log_file, 'w') as f:
            f.write(f"Turn {turn_number}:\n\n")

        # Customer generates a response
        if user_message and i == 0:
            print_colored("Customer", f"{user_message}\n\n")

        # Customer generates a response every 3rd turn
        elif i % 3 == 0:
            print("Customer, do you want to continue the conversation? (yes/no)")
            user_message = input()

            if user_message.lower() == 'no':
                break
            else:
                print("Please provide your input:")
                user_message = input()
                print_colored("Customer", f"{user_message}\n\n")

        # Loop through each bot in created_bots
        for chatbot in created_bots:
            # Check if there is a user message
            if user_message:
                response = chatbot['gpt'].chat(user_message, log_file, project_name_dir)
                user_message = response
                print_colored(chatbot['bot'].get_name(), f"{user_message}\n\n")
            else:
                break

