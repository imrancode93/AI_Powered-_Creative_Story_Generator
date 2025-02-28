from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI  # ✅ Use ChatOpenAI for chat models
from dotenv import load_dotenv
import os

# Load API keys from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Chat LLM (Supports ChatGPT models)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7, openai_api_key=OPENAI_API_KEY)

# Define the prompt template
story_prompt = PromptTemplate(
    input_variables=["genre", "theme", "characters", "story_length"],
    template="Write a {story_length} story in the {genre} genre. The story should be about {theme}. The main characters are: {characters}."
)

def generate_story(user_input):
    prompt = story_prompt.format(**user_input)
    story = llm.invoke(prompt)  # ✅ Use invoke() for chat models
    return story.content  # ✅ Extract text from response

if __name__ == "__main__":
    user_input = {
        "genre": "Sci-Fi",
        "theme": "Time Travel",
        "characters": "Dr. Nova, AI Assistant X-99",
        "story_length": "Short"
    }
    print(generate_story(user_input))
