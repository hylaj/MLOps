from app import model


def test_load_sklearn():
    assert model.sklearn_model is not None


def test_load_sentence_transformer():
    assert model.sentence_transformer_model is not None
