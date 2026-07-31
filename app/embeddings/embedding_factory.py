from app.embeddings.sentence_transformer_embedder import SentenceTransformerEmbedder

class EmbedderFactory:

    @staticmethod
    def get_embedder():
        return SentenceTransformerEmbedder()