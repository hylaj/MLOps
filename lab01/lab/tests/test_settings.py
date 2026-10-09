from settings import Settings


def test_settings_load_correctly():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "mlops"
    assert settings.API_KEY == "api_key_67890"
