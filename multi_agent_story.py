from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Adjust temperature for more creativity (Feature 3)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=1.0, openai_api_key=OPENAI_API_KEY)

# ✅ Add Memory (Feature 1)
memory = ConversationBufferMemory()
prompt = PromptTemplate(input_variables=["input"], template="{input}")
llm_chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# ✅ Define AI Agents
plot_developer = Agent(
    role="Plot Developer",
    goal="Create a structured storyline with an exciting plot twist",
    backstory="A master storyteller who specializes in building gripping narratives",
    verbose=True,
    llm=llm_chain.llm  # ✅ Use memory-enabled LLM
)

character_designer = Agent(
    role="Character Designer",
    goal="Develop unique characters with depth, personality, and motivations",
    backstory="A novelist skilled in character development",
    verbose=True,
    llm=llm_chain.llm
)

dialogue_writer = Agent(
    role="Dialogue Writer",
    goal="Write engaging and natural conversations between characters",
    backstory="A scriptwriter with expertise in storytelling and character dialogues",
    verbose=True,
    llm=llm_chain.llm
)

grammar_checker = Agent(
    role="Grammar & Flow Checker",
    goal="Ensure proper sentence structure, readability, and coherence in the story",
    backstory="An expert editor who refines text to perfection",
    verbose=True,
    llm=llm_chain.llm
)

# ✅ New: World Builder AI (Feature 3)
world_builder = Agent(
    role="World Builder",
    goal="Create a detailed and immersive world for the story",
    backstory="An AI specialized in world-building for epic adventures",
    verbose=True,
    llm=llm_chain.llm
)

# ✅ Define Tasks
plot_task = Task(description="Develop an engaging story plot", agent=plot_developer)
character_task = Task(description="Create characters for the story", agent=character_designer)
dialogue_task = Task(description="Write dialogues for the story", agent=dialogue_writer)
grammar_task = Task(description="Review the story for grammar and flow", agent=grammar_checker)
world_task = Task(description="Design a vivid and immersive world for the story", agent=world_builder)

# ✅ CrewAI with all agents
story_crew = Crew(
    agents=[plot_developer, character_designer, dialogue_writer, grammar_checker, world_builder],
    tasks=[plot_task, character_task, dialogue_task, grammar_task, world_task],
    verbose=True
)

# ✅ Feature 2: User Interactive Mode
def interactive_story():
    while True:
        user_feedback = input("\n💡 Modify story? (yes/no): ").strip().lower()
        if user_feedback == "no":
            print("\n📖 Final Story Output:\n", memory.buffer)
            break  # Exit loop if user doesn't want to modify

        feedback = input("🔄 What should be changed? (e.g., Make it scarier!): ")
        memory.save_context({"user": feedback}, {"agent": "Updating story..."})

        print("\n🚀 AI is modifying the story...")
        story_crew.kickoff()  # Generate new version with memory

# ✅ Run the AI storytelling process
if __name__ == "__main__":
    interactive_story()
