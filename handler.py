class Handler:

    def __init__(self, initial_data: dict):
        """

        :param initial_data: dict
        """
        self._permissions = list()
        self._initial_data = initial_data
        self._company_name = str

    def handle_file(self) -> None:
        """
        Parse a policy file. You'll get a company name and permissions and their description

        :return: None
        """
        self.__set_company_name()

        for i in self._initial_data['segments']:  # Handle each permission
            self.__handle_data(i)

    def __set_company_name(self):
        self._company_name = self._initial_data['policy_name']  # This stroke consists a company name in the file

    def get_company_name(self):
        return self._company_name

    def __handle_data(self, data):
        for key, values in data.items():
            if (key == 'sentences') and values:
                for i in values:
                    permission = i['annotations'][0]['practice']
                    if '3rdParty' in permission:
                        all_permissions = [i['sentence_text'], permission]
                        self._permissions.append(all_permissions)

    def get_permissions_data(self) -> list:
        return self._permissions
