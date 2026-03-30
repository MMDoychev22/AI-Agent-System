import weaviate
from weaviate.classes.init import Auth
from weaviate.classes.config import Property, DataType, Vectorizers

WEAVIATE_URL = "https://dp3ywuvtm6kot0vk3fyia.c0.europe-west3.gcp.weaviate.cloud"
WEAVIATE_API_KEY = "dzExR2FJbmFrUlNpemZUNl9ZejU0cmNubGN3RXpOZlZXdUNZY0tBMTF2QzdvdmVuR2tGK01qa09QM3NRPV92MjAw"

client = weaviate.connect_to_weaviate_cloud(
    cluster_url=WEAVIATE_URL,
    auth_credentials=Auth.api_key(WEAVIATE_API_KEY),
)

client.collections.delete_all()

client.collections.create(
    name="Movies",
    properties=[
        Property(name="title", data_type=DataType.TEXT),
        Property(name="description", data_type=DataType.TEXT),
        Property(name="genres", data_type=DataType.TEXT_ARRAY),
        Property(name="year", data_type=DataType.INT),
        Property(name="rating", data_type=DataType.NUMBER),
        Property(name="type", data_type=DataType.TEXT),
        Property(name="country", data_type=DataType.TEXT),
    ],
    vectorizer_config=Vectorizers.TEXT2VEC_PALM,
)

client.collections.create(
    name="People",
    properties=[
        Property(name="name", data_type=DataType.TEXT),
        Property(name="role", data_type=DataType.TEXT),
        Property(name="known_for", data_type=DataType.TEXT_ARRAY),
        Property(name="nationality", data_type=DataType.TEXT),
    ],
    vectorizer_config=Vectorizers.TEXT2VEC_PALM,
)

client.close()
