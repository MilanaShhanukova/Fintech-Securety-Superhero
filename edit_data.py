import os
import json


#получение имен файлов из базы данных + преобразованных имен без расширения
def list_of_files(path: str = 'files') -> tuple:
    directory = os.getcwd() + path
    files = os.listdir(directory)
    json_files = list(filter(lambda x: x.endswith('.json'), files))
    files = [file[:-5] for file in json_files]
    return json_files, files


companies_names, names_of_files = list_of_files()

#получение всех видов данных для одного файла
def get_features(file_name:str, path: str = 'files') -> set:
    # поменяем директорию, если не находимся в папке с файлами о данных
    directory = os.getcwd()
    if not directory.endswith(path):
        os.chdir(os.getcwd() + path)

    with open(file_name) as file:
        info_data = json.load(file)
        if info_data != 0:
            features = [info_data[i][1] for i in range(len(info_data) - 1)]
            return set(features)


#преобразованная база компания-все виды данных
def dict_file_features() -> dict:
    file_features = {}
    for name in names_of_files:
        file_features[name] = get_features(name + ".json")
    return file_features

company_features = dict_file_features()

def clean_companies() -> list:
    clean = []
    for company, data in company_features.items():
        if len(data) == 0:
            clean.append(company)
    return clean

no_data_companies = clean_companies()


#преобразованная база данные-все компании
def dict_feature_companies() -> dict:
    features = []
    for company, data in company_features.items():
        for feature in data:
            if feature not in features:
                features.append(feature)

    feature_company = {feature: [] for feature in features}

    for company, data in company_features.items():
        for feature in data:
            feature_company[feature].append(company)
    return feature_company


feature_company = dict_feature_companies()

#преобразованные названия данных
new_features = {'Identifier_Cookie_or_similar_Tech_3rdParty': "Cookie or web-beacon files",
                'Demographic_3rdParty': "Your demographic group",
                'Contact_E_Mail_Address_3rdParty': "Email address",
                'Identifier_IP_Address_3rdParty': "IP Address",
                'Contact_City_3rdParty': "Your city or hometown",
                'Location_3rdParty': "Your location",
                'Identifier_Device_ID_3rdParty': "You device id",
                'Identifier_3rdParty': "Your unique identity",
                'Identifier_Ad_ID_3rdParty': "Your advertisment id",
                'Contact_3rdParty': "Your contact info",
                'Demographic_Age_3rdParty': "Your age",
                'Contact_Postal_Address_3rdParty':"Physical, home, work addresses",
                'Contact_Phone_Number_3rdParty': "Your phone number",
                'Contact_Address_Book_3rdParty': "Your phone book",
                'Contact_ZIP_3rdParty': "Your area code",
                'Contact_Password_3rdParty': "Your credential and passwords",
                "Location_WiFi_3rdParty": "Your wifi-location",
                "Location_IP_Address_3rdParty": "Your IP Address",
                "Location_GPS_3rdParty": "Your GPS location",
                "Location_Cell_Tower_3rdParty": "Location of your network-base",
                "Location_Bluetooth_3rdParty": "Detailed location of your bluetooth-device",
                "Identifier_SSID_BSSID_3rdParty": "Wifi networks that you used",
                "Identifier_SIM_Serial_3rdParty": "Your serial number",
                "Identifier_Mobile_Carrier_3rdParty": "Your mobile oparator",
                "Identifier_MAC_3rdParty": "Your hardware or device id",
                "Identifier_IMSI_3rdParty": "Your international mobile subscriber",
                "Identifier_IMEI_3rdParty": "Your international mobile equipment",
                "Facebook_SSO": "Login credentials from one of your accounts",
                "Demographic_Gender_3rdParty": "Your gender"
               }


def data_to_graph() -> dict:
    feature_companies = {}
    for key in new_features.keys():
        feature_companies[new_features[key]] = feature_company[key]

    return feature_companies

feature_companies = data_to_graph()
