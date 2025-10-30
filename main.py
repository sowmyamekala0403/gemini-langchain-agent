import os
import getpass
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Check and set Gemini API key
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google Gemini API key: ")

print("✅ Gemini API key configured!")

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.7)
print(f"✅ Initialized model: {model.__class__.__name__}")

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {expertise}."),
    ("human", "Explain {topic} in a simple and clear way.")
])

# Build LCEL chain
assistant_chain = prompt_template | model | StrOutputParser()

# Example 1: Normal response
response = assistant_chain.invoke({
    "expertise": "neuroscience",
    "topic": "how neurons communicate"
})
print("\n🧠 Response:")
print(response)

# Example 2: Streaming response
print("\n🌊 Streaming response:")
for chunk in assistant_chain.stream({
    "expertise": "culinary science",
    "topic": "the Maillard reaction"
}):
    print(chunk, end="", flush=True)
