from src.stages.load.load_data import LoadData
from src.stages.contracts.mocks.transform_contract import transform_contract_mock
from src.errors.load_error import LoadError


class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_attributes = []

    def insert_artist(self, data):
        self.insert_artist_attributes.append(data)


def test_load_data() -> None:
    repository = RepositorySpy()
    load_data = LoadData(repository)

    load_data.load(transform_contract_mock)

    assert repository.insert_artist_attributes == transform_contract_mock.load_content


def test_load_data_error() -> None:
    repository = RepositorySpy()
    load_data = LoadData(repository)

    try:
        load_data.load("Load error.")
    except Exception as e:
        assert isinstance(e, LoadError)
