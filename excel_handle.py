import pandas as pd
import yaml


def open_yaml_features_file(path2file: str):
    with open(path2file, mode='r') as yaml_file:
        return yaml.load(yaml_file, Loader=yaml.FullLoader)


def unique_features(path2file: str = 'dataset_PrivacyMap/features.yml') -> map:
    """
    Parse a features file to get only unique features

    :param path2file: str - path to features.yaml file
    :return: map - key it's a unique permission, value is a description
    """
    parsed_yaml_file = open_yaml_features_file(path2file)
    return {i['practices'][1]: i['features'] for i in parsed_yaml_file['data_types']}


class ExcelHandler:

    def __init__(self, unique_permissions: map):
        """
        Initialize a pandas DataFrame by unique_permission. You need to get this set of data
        with a count_unique_permissions function.

        :param unique_permissions: map - result of a count_unique_permissions function
        """
        self.companies_permissions = pd.DataFrame(columns=[key for key in unique_permissions.keys()])

    def get_df(self) -> pd.DataFrame:
        return self.companies_permissions

    def add_company_into_table(self, company_name: str, company_information: list) -> None:
        """
        Add a company and permissions to the table.
        If a company has permission then this cell will be "Yes"
        otherwise "No"

        :param company_name: str - name of company. You can get this information with Handler.get_company_name
        :param company_information: list - it consists permissions and their description. Get this information with
        Handler.get_permissions_data
        :return: None
        """

        df_columns = self.companies_permissions.columns.tolist()  # Get unique columns. Columns consist permissions.
        company_permission = {i[1] for i in company_information}  # Get permissions from a certain company

        res = list()

        for permission in df_columns:
            res.append('Yes') if permission in company_permission else res.append(' ')
        self.companies_permissions.loc[company_name] = res  # Add to pandas DataFrame

    def save_excel_file(self, path: str = "table_of_companies") -> None:
        with pd.ExcelWriter(f'{path}.xlsx') as writer:
            self.companies_permissions.to_excel(writer)
