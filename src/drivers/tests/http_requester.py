class HttpRequesterSpy:
    def __init__(self) -> None:
        self.request_from_page_count = 0

    def request_from_page(self) -> dict:
        self.request_from_page_count += 1

        return {"status_code": 200, "html": "<h1>Some H1<h1>"}
