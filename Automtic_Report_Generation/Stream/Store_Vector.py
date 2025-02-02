import chromadb
from sentence_transformers import SentenceTransformer

def Vector_Process(Query, Data):

    if not Query or Data is None:
        return "Please provide a valid query or upload data."

    Model = SentenceTransformer('all-MiniLM-L6-v2')
    Client = chromadb.Client()
    Collection = Client.create_collection(name="ProductData")

    Labelled_Text = []
    for index, row in Data.iterrows():
        Label = "\n".join([f"{col}: {row[col]}" for col in row.index])
        Labelled_Text.append(Label)

    Embeds = Model.encode(Labelled_Text, batch_size=25)
    Collection.add(
        ids=[str(index) for index in range(len(Labelled_Text))],
        embeddings=Embeds,
        metadatas=[{"text": label} for label in Labelled_Text]
    )

    # Vector Query
    Query_Embed = Model.encode(Query)
    Result = Collection.query(query_embeddings=[Query_Embed], n_results=5)  # Limit results to top 5 matches
    Relevant_Data = [item['text'] for metadata_list in Result.get("metadatas", []) for item in metadata_list]
    Pass_Content = "\n".join(Relevant_Data) if Relevant_Data else "No relevant data found."

    return Pass_Content
