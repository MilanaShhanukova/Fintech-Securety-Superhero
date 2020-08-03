import yaml
import os
from handler import Handler


def count_files(path2files: str):
    _, _, files = next(os.walk(path2files))
    return len(files)


def open_files(path2files: str = "dataset_PrivacyMap/annotations/"):
    file_count = count_files(path2files)

    for file_number in range(1, file_count + 1):
        with open(f"{path2files}policy_{file_number}.yml") as a_yaml_file:
            parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
            yield parsed_yaml_file


def save_file(company_name: str, data: list, path: str = os.getcwd(), category: str = None):
    pass


current_file = open_files()
for j, entry in enumerate(current_file):
    company = Handler(entry)
    company.handle_file()
