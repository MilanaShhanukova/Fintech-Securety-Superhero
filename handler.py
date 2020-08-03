class Handler:

    def __init__(self, entry):

        self._permissions = list()
        self._initial_data = entry
        self._company_name = str

    def handle_file(self):

        self.__set_company_name()

        for i in self._initial_data['segments']:
            self.__handle_data(i)

    def __set_company_name(self):
        self._company_name = self._initial_data['policy_name']

    def get_company_name(self):
        return self._company_name

    def __handle_data(self, data):
        for key, values in data.items():
            if key == 'sentences':
                if values:
                    for i in values:
                        permission = [i['sentence_text'], i['annotations'][0]['practice']]
                        self._permissions.append(permission)

    def get_permissions_data(self):
        return self._permissions
