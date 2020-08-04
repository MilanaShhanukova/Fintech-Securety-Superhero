from parser import *
from handler import Handler
from excel_handle import *

if __name__ == '__main__':

    unique_permissions = count_unique_permissions()
    table_of_companies = ExcelHandler(unique_permissions)
    current_file = open_policy_yaml_files()

    for entry in current_file:

        company = Handler(entry)
        company.handle_file()

        data = company.get_permissions_data()

        company_name = company.get_company_name()

        table_of_companies.add_company_into_table(company_name, data)

        #save_file(company_name, data)

    table_of_companies.save_excel_file()