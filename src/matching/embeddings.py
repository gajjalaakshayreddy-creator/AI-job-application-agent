from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(
            model_name
        )

    def create_embedding(
        self,
        text: str
    ):
        return self.model.encode(
            text,
            normalize_embeddings=True
        )
from sentence_transformers import util


def calculate_similarity(
    embedding_a,
    embedding_b
) -> float:

    similarity = util.cos_sim(
        embedding_a,
        embedding_b
    )

    return float(
        similarity[0][0]
    )