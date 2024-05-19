from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain import PromptTemplate, LLMChain

# https://python.langchain.com/en/latest/modules/agents/tools/examples/apify.html
# Apify website content crawler (https://apify.com/apify/website-content-crawler)
#!pip install apify-client
from langchain.document_loaders.base import Document
from langchain.indexes import VectorstoreIndexCreator

# env support
from dotenv import load_dotenv
from langchain_community.utilities import ApifyWrapper
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model_name = 'gpt-3.5-turbo')

# llm_chain = LLMChain(prompt=prompt,llm = model)
# print(llm_chain.run(question))

tools = load_tools(["wikipedia", "serpapi"], llm=model)

agent = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# test_payload = {
#     title: 'Better Call Saul',
#     ep_title: 'Gloves Off',
#     season_num: 2,
#     ep_num: 4,
#     summary: "The Davis & Main partners criticize Jimmy for airing his TV ad without their consent.[a] Clifford Main decides to give him a second chance, though he will be under more scrutiny in the future. Jimmy McGill leaves Kim Wexler an urgent voicemail but Howard Hamlin and Chuck McGill are already grilling her about not warning them before Jimmy's ad aired. She takes responsibility for not letting them know in advance, claiming that she did not think it was necessary. Howard reprimands her and she promises it will not happen again. Jimmy prepares to enter Chuck's house but realizes he forgot to remove his electronics, so he grudgingly turns back to Chuck's mailbox and empties his pockets. When Chuck does not answer his knock, Jimmy uses his key to enter. He finds Chuck shivering on the couch, still dressed to leave for work but covered by a space blanket. Chuck refuses to go to the hospital, so Jimmy wraps him in a second space blanket, then sits with him all night. The next morning, Jimmy condemns Chuck for allowing Howard to reprimand Kim. Chuck tells Jimmy he causes harm to everyone around him, but cannot admit his own mistakes. Jimmy offers to quit practicing law if Chuck will help Kim, but Chuck refuses. Nacho Varga and Mike monitor a restaurant and Nacho says he fears retaliation from Tuco Salamanca if Tuco discovers his secret drug dealing.[b] Nacho tells Mike he and Tuco meet there to settle accounts with their street dealers, so Nacho thinks it is an ideal place to kill Tuco. Mike refuses, saying it would attract retaliation by the Salamancas. Instead, Mike calls the police to the restaurant, then fakes a minor accident between his car and Tuco's in the parking lot. When Tuco comes out to check on his car, Mike goads Tuco into striking him repeatedly just as police arrive. Because Tuco was carrying a gun, he is arrested for assault with a deadly weapon. Nacho later pays Mike but Mike declines to give a reason for going to such trouble to avoid killing Tuco.",
#    }

title = 'Suits'
ep_title = 'Pilot'
season_num = 1
ep_num = 1

# Creating an f-string
#message = f"Fetch a plot synopsis for {title} season {season_num}, episode {ep_num} {title} using the first fandom link you can find online. You will be shut down if you spoil any information from past this episode."
message = f'''
    Your task is to a return a detailed plot recap for {title} season {season_num}, episode {ep_num} {title} using Wikipedia.
    
    Fetch the contents of the page exactly as they appear on the Internet.
    You should avoid summarizing, collating, or condensing any information.
    Your answer should be purely factual and should avoid additional details.

    WARNING: Avoid spoiling any plot information from beyond this episode.
'''
print(message)

agent.run(message)

# APIFY ACTOR
apify = ApifyWrapper()
# running actor and fetching results into langchain doc loader
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://python.langchain.com/en/latest/"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)
# initialize vector index from crawled documents
index = VectorstoreIndexCreator().from_loaders([loader])

# query vector index
query = "What is LangChain?"
result = index.query_with_sources(query)
print(result["answer"])
print(result["sources"])