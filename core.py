import weaviate
from weaviate.classes.init import Auth
from weaviate.agents.query import QueryAgent
from weaviate.agents.classes import QueryAgentCollectionConfig
import os
from dotenv import load_dotenv

load_dotenv()

WEAVIATE_URL = os.getenv("WEAVIATE_URL")
WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY")
INFERENCE_PROVIDER_API_KEY = os.getenv("INFERENCE_PROVIDER_API_KEY")

headers = {
    "X-Google-Api-Key": INFERENCE_PROVIDER_API_KEY
}



def init_query_agent():
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=WEAVIATE_URL,
        auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
        headers=headers,
    )

    # Use the collections that actually exist in the dataset
    collections = [
        QueryAgentCollectionConfig(
            name="SampleWebsites",
            properties=["title", "description", "genres", "year", "rating", "type", "country"],
        ),
    ]

    agent = QueryAgent(
        client=client,
        collections=collections,
        system_prompt="You are a movie assistant. Answer in Bulgarian.",
    )
    return agent
