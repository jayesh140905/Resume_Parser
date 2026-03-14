from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_sections(query, chunks, index):

    query_embedding = model.encode([query])

    D, I = index.search(query_embedding, k=3)

    results = []

    for i in I[0]:
        results.append(chunks[i])

    return results