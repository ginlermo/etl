from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TransformContract
from src.errors.transform_error import TransformError


class TransformRawData:
    def transform(self, extract_contract: ExtractContract) -> TransformContract:
        try:
            transformed_information = self.__filter_and_transform_data(extract_contract)
            transformed_data_contract = TransformContract(
                load_content=transformed_information
            )

            return transformed_data_contract
        except Exception as e:
            raise TransformError(str(e)) from e

    def __filter_and_transform_data(
        self, extract_contract: ExtractContract
    ) -> list[dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content

        transformed_data_content = []

        for data_item in data_content:
            link = data_item["link"]

            if "artistid" not in link:
                continue

            if ", " in data_item["name"]:
                names = data_item["name"].split(", ")

            elif " " in data_item["name"]:
                names = data_item["name"].split(" ")

            else:
                names = [data_item["name"]]

            transformed_data = self.__transform_data(names=names, link=link)
            transformed_data["extraction_date"] = extraction_date

            transformed_data_content.append(transformed_data)

        return transformed_data_content

    @classmethod
    def __transform_data(cls, names: list, link: str) -> dict:
        link_split = link.split("artistid=")

        if len(names) == 2:
            return {
                "first_name": names[1],
                "second_name": names[0],
                "nickname": None,
                "artist_id": link_split[1],
                "link": link,
            }

        if len(names) == 3:
            return {
                "first_name": names[2],
                "second_name": names[0],
                "nickname": names[1],
                "artist_id": link_split[1],
                "link": link,
            }

        return {
            "first_name": names[0],
            "second_name": None,
            "nickname": None,
            "artist_id": link_split[1],
            "link": link,
        }
