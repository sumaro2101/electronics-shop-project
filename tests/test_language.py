import pytest

@pytest.mark.property
class TestLanguage:
        
    def test_language_raises(init_keyboard):
        with pytest.raises(AttributeError):
            init_keyboard.language = "RU"