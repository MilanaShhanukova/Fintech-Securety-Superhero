import yaml
import os
import json


def count_files(path2files: str) -> int:
    """
    Count files in the directory
    :param path2files: str - path to your files
    :return: int
    """
    _, _, files = next(os.walk(path2files))
    return len(files)


def open_yaml_files(path2files: str = "dataset_PrivacyMap/annotations/") -> iter:
    """
    Open yaml files in the directory

    :param path2files: str - path to your yaml files
    :return: generator object
    """
    file_count = count_files(path2files)

    for file_number in range(1, file_count + 1):
        with open(f"{path2files}policy_{file_number}.yml") as a_yaml_file:
            parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
            yield parsed_yaml_file


def save_file(company_name: str, data: list, path: str = None, category: bool = False) -> None:
    """
    Save your files as a json format

    :param company_name: str - set a company name. it's used as a file name
    :param data: str - list of permissions
    :param path: str
    :param category: bool - if you want to save by categories select this one
    :return: None
    """

    if not os.path.isdir("permissions_data"):
        try:
            os.mkdir(f"permissions_data", 0o755)
        except OSError:
            print("Creation of the directory failed")
    else:
        with open(f'permissions_data/{company_name}.json', 'w') as f:
            json.dump(data, f)



