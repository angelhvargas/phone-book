import pytest


@pytest.mark.usefixtures('app', 'client', 'runner')
class TestServer():
    pass
    # def test_get_all_contacts(self, client):
    #     result = client.get('contact/all', '')
    #     print(result)
    #     assert result == "hi"
