🕸️ Web Scraper & ETL Pipeline Learning

The scraper is a robust data engineering pipeline designed to automate the collection, processing, and storage of data from web.archive.org.

The system performs two main functions:

    Scraping: Navigates target websites to harvest raw data (HTML/JSON).

    ETL (Extract, Transform, Load): Cleans, normalizes, and structures the raw data before loading it into a [PostgreSQL] for analysis.

⚙️ Architecture

The pipeline follows a modular architecture:

    Extract (Scraper):

        Uses [BeautifulSoup] to crawl specific endpoints.

        Handles pagination, user-agent rotation, and request throttling to avoid IP bans.

        Saves raw data to a staging area (local JSON files).

    Transform:

        Parses raw HTML/JSON.

        Cleans dirty data (removes nulls, duplicates, and HTML tags).

        Standardizes formats (dates to ISO 8601, currency conversion).

        Validates data schema using [DataClasess].

    Load:

        Connects to the destination database.

        Performs upserts (update if exists, insert if new) to maintain data integrity.