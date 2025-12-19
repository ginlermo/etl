# pylint: disable=line-too-long

from datetime import date
from src.stages.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content=[
        {
            "name": "Zampieri, Domenico",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3941",
        },
        {
            "name": "Zampieri, called Domenichino, Domenico",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3941",
        },
        {
            "name": "Zanartú, Enrique Antunez",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3453",
        },
        {
            "name": "Zanchi, Antonio",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=35173",
        },
        {
            "name": "Zanetti, Anton Maria",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=11133",
        },
        {
            "name": "Zanetti Borzino, Leopoldina",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3455",
        },
    ],
    extraction_date=date.today(),
)
