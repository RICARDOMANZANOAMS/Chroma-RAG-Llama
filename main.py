import chromadb
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_collection")
collection.add(
    documents=[
        "Ricardo has a dog who is name Smile",
        "Washington has a toyota car",
        "Sylvia has a pet who is named Mandy"

    ],
    ids=["id1", "id2","id3"]
)
results = collection.query(
    query_texts=["What is Ricardo's pet"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)