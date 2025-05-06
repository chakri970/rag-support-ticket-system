import json
import faiss

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def load_tickets(path="data/tickets.json"):
    with open(path) as f:
        return json.load(f)


def build_index(tickets):
    texts = [f"{t['title']} {t['issue']} {t['resolution']}" for t in tickets]
    embeddings = model.encode(texts, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, embeddings


def save_index(index, path="embeddings/index.faiss"):
    faiss.write_index(index, path)


def load_index(path="embeddings/index.faiss"):
    return faiss.read_index(path)


def search_tickets(query, index, tickets, top_k=2):
    query_vec = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_vec, top_k)
    return [tickets[i] for i in indices[0]]
