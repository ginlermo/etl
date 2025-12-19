import datetime

from src.stages.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {
            "first_name": "Domenico",
            "second_name": "Zampieri",
            "nickname": None,
            "artist_id": "3941",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3941",
            "extraction_date": datetime.date(2025, 12, 18),
        },
        {
            "first_name": "Domenico",
            "second_name": "Zampieri",
            "nickname": "called Domenichino",
            "artist_id": "3941",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3941",
            "extraction_date": datetime.date(2025, 12, 18),
        },
        {
            "first_name": "Enrique Antunez",
            "second_name": "Zanartú",
            "nickname": None,
            "artist_id": "3453",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3453",
            "extraction_date": datetime.date(2025, 12, 18),
        },
        {
            "first_name": "Antonio",
            "second_name": "Zanchi",
            "nickname": None,
            "artist_id": "35173",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=35173",
            "extraction_date": datetime.date(2025, 12, 18),
        },
        {
            "first_name": "Anton Maria",
            "second_name": "Zanetti",
            "nickname": None,
            "artist_id": "11133",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=11133",
            "extraction_date": datetime.date(2025, 12, 18),
        },
        {
            "first_name": "Leopoldina",
            "second_name": "Zanetti Borzino",
            "nickname": None,
            "artist_id": "3455",
            "link": "https://web.archive.org/web/20121002115714/http://www.nga.gov/cgi-bin/tsearch?artistid=3455",
            "extraction_date": datetime.date(2025, 12, 18),
        },
    ]
)
