from httpx import get
from src.drivers.interfaces.http_requester import HttpRequesterInterface


class HttpRequester(HttpRequesterInterface):
    def __init__(self) -> None:
        self.__url = "https://web.archive.org/web/20121002115714/http://www.nga.gov/collection/anZ1.htm"

    def request_from_page(self) -> dict:
        response = get(self.__url)

        return {"status_code": response.status_code, "html": response.text}
