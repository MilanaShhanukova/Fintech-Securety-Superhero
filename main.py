from parser import *
from handler import Handler
from excel_handle import *

if __name__ == '__main__':

    unique_permissions = unique_features()

    table_of_companies = ExcelHandler(unique_permissions)

    privacy_files = open_policy_yaml_files()

    for current_privacy_file in privacy_files:

        company = Handler(current_privacy_file)
        company.handle_file()

        company_permissions, company_name = company.get_company_data()

        table_of_companies.add_company_into_table(company_name, company_permissions)

        save_file_as_json(company_name, company_permissions)

