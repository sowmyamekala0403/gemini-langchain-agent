Gemini LangChain Agent

This project shows how to connect Google Gemini models with LangChain to create an intelligent conversational system. It helps generate useful and meaningful responses to user inputs by using Gemini’s AI power.

About the Project

The main idea of this project is to use Gemini API with LangChain to build a small AI chat agent that can answer questions, explain topics, or generate ideas in an easy and understandable way.

It works by loading your Gemini API key from a .env file, initializing the model, and then sending a prompt through LangChain to get a smart reply from Gemini.

Features

Connects Gemini API with LangChain

Generates simple and accurate responses

Supports both normal and streaming outputs

Beginner friendly and easy to modify

Can be used for chatbots, learning tools, or AI assistants

Files in the Project

main.py – Main Python file to run the Gemini-LangChain connection

checkgeminiversion.py – Used to check and list available Gemini models

.env – Stores your Gemini API key

requirements.txt – Contains all the required libraries

README.md – Explains the project

How It Works

Load your Gemini API key from the .env file

Initialize the Gemini model using LangChain

Give a prompt like a question or topic

The model gives a meaningful answer using Gemini’s understanding

Example Outputs

Example 1:

User: What is the Maillard reaction?
AI: The Maillard reaction is a chemical process that occurs when proteins and sugars react under heat, giving food its brown color and rich flavor.


Example 2:

User: Give me some creative ideas for an AI project.
AI: 1. AI-based study planner  
    2. Virtual cooking assistant  
    3. Smart health tracker  
    4. Chatbot for quick coding help

Requirements

Python 3.10 or above

Install libraries using: pip install -r requirements.txt

Gemini API key (stored in .env file)

Use Cases

Chatbot development

Educational tools

AI-based Q&A systems

Idea generation or writing assistants

Author

Sowmya Mekala
