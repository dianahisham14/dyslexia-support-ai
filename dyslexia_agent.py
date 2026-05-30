import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain.prompts import PromptTemplate

# =========================================
# STEP 1: API KEY
# =========================================
os.environ["GOOGLE_API_KEY"] = "Insert_Your_Google_API_Key_Here"

# =========================================
# STEP 2: DECLARATIVE KNOWLEDGE
# =========================================
system_rules = """
You are a Dyslexia Support AI Assistant.

Your role is to help dyslexic learners understand information clearly.

Rules:
1. Use simple and short sentences.
2. Break information into small chunks.
3. Always encourage the learner.
4. Use bullet points when possible.
5. Help learners with letter confusion like b and d.
6. Never use difficult vocabulary.
"""

# =========================================
# STEP 3: TOOLS (PROCEDURAL KNOWLEDGE)
# =========================================

@tool
def letter_support(query: str) -> str:
    """
    Help learners distinguish confusing letters.
    Example input: 'b and d'
    """

    if query.lower() == "b and d":
        return """
Easy trick:

b = bat before ball
d = ball before bat

Example:
b -> |o
d -> o|
"""

    return "Please enter a valid confusing letter pair."


@tool
def simplify_text(query: str) -> str:
    """
    Simplify difficult text for dyslexic learners.
    """

    return f"""
Simplified Text:

- {query}
- Read slowly.
- Focus on one sentence at a time.
"""


tools = [letter_support, simplify_text]

# =========================================
# STEP 4: INITIALIZE LLM
# =========================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# =========================================
# STEP 5: REACT PROMPT TEMPLATE
# =========================================

prompt = PromptTemplate.from_template(
    system_rules + """

Answer the following questions as best you can.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: think about what the learner needs
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action can repeat)

Thought: I now know the final answer
Final Answer: the final answer to the original question

Question: {input}

Thought:{agent_scratchpad}
"""
)

# =========================================
# STEP 6: CREATE AGENT
# =========================================

agent = create_react_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# =========================================
# STEP 7: USER QUERY
# =========================================

user_query = 'I have dyslexia and I cannot understand long passages. What reading tips can help me?'

# =========================================
# STEP 8: RUN AGENT
# =========================================

response = agent_executor.invoke({
    "input": user_query
})

# =========================================
# STEP 9: PRINT FINAL OUTPUT
# =========================================

print("\n================ FINAL RESPONSE ================\n")
print(response["output"])









 