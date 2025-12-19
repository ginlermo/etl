from src.infra.database_connector import DatabaseConnector


def test_database_connector():
    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None
