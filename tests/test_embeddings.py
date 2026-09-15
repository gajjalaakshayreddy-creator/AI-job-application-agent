from src.matching.embeddings import (
    EmbeddingService,
    calculate_similarity
)


def test_similar_text_has_high_similarity():

    service = EmbeddingService()

    text_a = (
        "Build applications using "
        "Azure OpenAI and large language models."
    )

    text_b = (
        "Develop AI applications using "
        "Azure hosted foundation models."
    )

    embedding_a = service.create_embedding(
        text_a
    )

    embedding_b = service.create_embedding(
        text_b
    )

    similarity = calculate_similarity(
        embedding_a,
        embedding_b
    )

    assert similarity > 0.5