PyAgents - Chat with AI Bots!
=============================

Welcome to PyAgents! This project aims to provide a streamlined and interactive way to chat with a team of AI-powered bots. Each bot has a unique role and set of skills, and together, they can help you brainstorm ideas, design projects, and solve problems.

Features
--------

-   Chat with a range of bots, each with a unique role and skills.
-   Bots' roles include Python developer, React Native engineer, Data Scientist, Technical Program Manager, Collaboration Manager, and Security Engineer.
-   All bots can provide helpful input and suggestions related to their area of expertise.
-   The conversation with the bots is colored for easy reading.

Setup
-----

### Installation

1.  Clone this repository to your local machine.
2.  Install the required packages with `pip install -r requirements.txt`

### API keys

You'll need to provide API keys for each of the bots. These should be set as environment variables, named as follows:

-   `OPENAI_API_KEY_CHATBOT1`
-   `OPENAI_API_KEY_CHATBOT2`
-   `OPENAI_API_KEY_CHATBOT3`
-   `OPENAI_API_KEY_CHATBOT4`
-   `OPENAI_API_KEY_CHATBOT5`
-   `OPENAI_API_KEY_CHATBOT6`
-   `OPENAI_API_KEY_CHATBOT7`
-   `OPENAI_API_KEY_CHATBOT8`
-   `OPENAI_API_KEY_CHATBOT9`

We recommend using a `.env` file to store these variables. An example file is included in the repository.

Usage
-----

Run the `pyagents.py` script to start the program. You'll be asked to provide a project name and description, which will be used to set the assignment for the bots.

After that, you'll be shown a list of available bots and their roles. You can select which bots you'd like to include in the project by entering their names, separated by commas.

The conversation will then start, with the user's project idea presented to the bots. You can interact with the bots, and the conversation will be saved in a log file for later reference.

Contributing
------------

We welcome contributions to this project! Please feel free to open an issue or pull request if you have a suggestion or find a bug.

License
-------

This project is licensed under the MIT License.

Note: This project uses the OpenAI API, which has its own terms of use. Please review these terms before using this project.
