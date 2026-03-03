class TestString:

    def test_check_string_length(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "String is longer than 15 symbols"