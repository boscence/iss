from devup.src.get_iss_location import get_iss_location


class TestOne:

    def test_iss(self):
        is_dict = get_iss_location()
        isinstance(is_dict, dict)

    def test_one(self):
        assert 2 == 2
