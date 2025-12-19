from src.stages.extract.extract_html import ExtractHtml
from src.drivers.tests.http_requester import HttpRequesterSpy
from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError


def test_extract_html():
    http_requester = HttpRequesterSpy()
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(
        http_requester=http_requester, html_collector=html_collector
    )

    response = extract_html.extract()

    assert isinstance(response, ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert "html" in html_collector.collect_essential_information_attributes


def test_extract_html_error():
    http_requester = "Making a error."
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(
        http_requester=http_requester, html_collector=html_collector
    )

    try:
        extract_html.extract()
    except Exception as e:
        assert isinstance(e, ExtractError)
