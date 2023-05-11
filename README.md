ChatGPT

PDF Summary Generator with Python Script

Overview

The PDF Summary Generator is a Python-based application that leverages the capabilities of OpenAI's GPT-3 language model to automatically generate summaries, notes, and other content from PDF documents. The application provides a RESTful API endpoint that accepts PDF files as input and returns a JSON object containing the generated summaries, notes, and additional content.

The application uses the pdfplumber library to extract text from PDF files, and the openai library to interact with the GPT-3 API. The application is built using the Flask web framework, making it easy to deploy and use.

Features

Extract text from PDF files and convert them to plain text format.

Generate summaries of the extracted text using GPT-3.

Generate notes and summaries of notes from the text.

Generate additional content such as essential information and blog posts.

Provide a RESTful API endpoint for easy integration with other applications.

Prerequisites

To use the PDF Summary Generator, you need the following:

Python 3.6 or higher

An OpenAI API key (you can obtain one by signing up for an account on the OpenAI platform)

The following Python libraries: flask, pdfplumber, openai, glob2, and textwrap

Installation

Clone the repository:

bash

Copy code

git clone https://github.com/antoine1anthony/flask-pdf-summary-api.git

cd pdf-summary-generator

Install the required Python libraries:

Copy code

pip install -r requirements.txt

Create a file named openaiapikey.txt in the project directory and paste your OpenAI API key into it.

(Optional) Customize the GPT-3 prompts and chatbot responses by modifying the text files in the project directory.

Usage

To run the PDF Summary Generator application, execute the following command in the project directory:

css

Copy code

python main.py

This will start the Flask development server, and the application will be accessible at http://localhost:8000/pdfsummary.

To use the API endpoint, send a POST request to http://localhost:8000/pdfsummary with the PDF files you want to summarize as multipart file attachments. The endpoint will return a JSON object containing the generated summaries, notes, and additional content.

You can use tools like Postman or curl to send requests to the API endpoint.

Example Request

bash

Copy code

curl -X POST -F "pdfs=@example.pdf" http://localhost:8000/pdfsummary

Example Response

json

Copy code

{

  "summary": "This is the summary of the PDF document...",

  "notes": "These are the notes extracted from the document...",

  "notes_summary": "This is the summary of the notes...",

  "essential_info": "This is the essential information extracted...",

  "blog_post": "This is the generated blog post based on the content..."

}

Contributing

Contributions to the PDF Summary Generator are welcome! If you would like to contribute, please fork the repository, make your changes, and submit a pull request. If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository.

License

The PDF Summary Generator is released under the MIT License. See the LICENSE file for more details.

Disclaimer

This application uses the GPT-3 language model provided by OpenAI. The quality of the generated content may vary, and users are advised to review the output before using it for any critical purposes. The application is provided "as is" without any warranties or guarantees. Users are responsible for any consequences resulting from the use of this application and its generated content.# PyAgents - Chat with AI Bots!

Welcome to PyAgents! This project aims to provide a streamlined and interactive way to chat with a team of AI-powered bots. Each bot has a unique role and set of skills, and together, they can help you brainstorm ideas, design projects, and solve problems.

## Features

- Chat with a range of bots, each with a unique role and skills.

- Bots' roles include Python developer, React Native engineer, Data Scientist, Technical Program Manager, Collaboration Manager, and Security Engineer.

- All bots can provide helpful input and suggestions related to their area of expertise.

- The conversation with the bots is colored for easy reading.

## Setup

### Installation

1\. Clone this repository to your local machine.

2\. Install the required packages with `pip install -r requirements.txt`

### API keys

You'll need to provide API keys for each of the bots. These should be set as environment variables, named as follows:

- `OPENAI_API_KEY_CHATBOT1`

- `OPENAI_API_KEY_CHATBOT2`

- `OPENAI_API_KEY_CHATBOT3`

- `OPENAI_API_KEY_CHATBOT4`

- `OPENAI_API_KEY_CHATBOT5`

- `OPENAI_API_KEY_CHATBOT6`

- `OPENAI_API_KEY_CHATBOT7`

- `OPENAI_API_KEY_CHATBOT8`

- `OPENAI_API_KEY_CHATBOT9`

We recommend using a `.env` file to store these variables. An example file is included in the repository.

## Usage

Run the `pyagents.py` script to start the program. You'll be asked to provide a project name and description, which will be used to set the assignment for the bots.

After that, you'll be shown a list of available bots and their roles. You can select which bots you'd like to include in the project by entering their names, separated by commas.

The conversation will then start, with the user's project idea presented to the bots. You can interact with the bots, and the conversation will be saved in a log file for later reference.

## Contributing

We welcome contributions to this project! Please feel free to open an issue or pull request if you have a suggestion or find a bug.

## License

This project is licensed under the MIT License.

Note: This project uses the OpenAI API, which has its own terms of use. Please review these terms before using this project.