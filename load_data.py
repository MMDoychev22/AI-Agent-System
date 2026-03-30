import weaviate
from weaviate.classes.init import Auth

WEAVIATE_URL = "https://dp3ywuvtm6kot0vk3fyia.c0.europe-west3.gcp.weaviate.cloud"
WEAVIATE_API_KEY = "dzExR2FJbmFrUlNpemZUNl9ZejU0cmNubGN3RXpOZlZXdUNZY0tBMTF2QzdvdmVuR2tGK01qa09QM3NRPV92MjAw"
INFERENCE_PROVIDER_API_KEY = "AIzaSyAZ0PcdiPoDKSwgl_ckcAYzCLQxQVZo8OU"

headers = {
    "X-Google-Api-Key": INFERENCE_PROVIDER_API_KEY
}

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
    headers=headers,
)

movies = client.collections.get("Movies")
people = client.collections.get("People")

with movies.batch.dynamic() as b:
    b.add_object({"title":"Inception","description":"Dream heist","genres":["Sci-Fi"],"year":2010,"rating":8.8,"type":"movie","country":"USA"})
    b.add_object({"title":"Interstellar","description":"Space travel","genres":["Sci-Fi"],"year":2014,"rating":8.6,"type":"movie","country":"USA"})
    b.add_object({"title":"La La Land","description":"Musical romance","genres":["Romance"],"year":2016,"rating":8.0,"type":"movie","country":"USA"})

with people.batch.dynamic() as b:
    b.add_object({"name":"Leonardo DiCaprio","role":"actor","known_for":"Inception","nationality":"USA"})
    b.add_object({"name":"Christopher Nolan","role":"director","known_for":"Inception, Interstellar","nationality":"UK"})
