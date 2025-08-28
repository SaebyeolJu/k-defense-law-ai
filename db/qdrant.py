from qdrant_client import QdrantClient

# Initialize Qdrant client
client = QdrantClient(
    host="localhost",  # Change to your Qdrant host
    port=6333          # Default Qdrant port
)

collections = client.get_collections()

def create_collection(collection_name, vector_size):
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config={"size": vector_size, "distance": "Cosine"}
    )
    
    
create_collection("law_db", 1536)
print(f"Collection '{collection_name}' created with vector size {vector_size}.")

