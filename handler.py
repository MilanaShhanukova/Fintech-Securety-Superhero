from edit_data import new_features


class Handler:

    def __init__(self, initial_data: dict):
        """

        :param initial_data: dict
        """
        self._permissions = list()
        self._initial_data = initial_data
        self._company_name = str
        self.advertisement = ["advertisements", "targeting", "advertising", "ad",
              "adverts", "remarketing", "promote", "promotion", "announce", "announcement",
               "publicize",]
        self.analytics = ["analytics", "statistics",
                          "analysis", "analytically", "analyze", "scrutiny",]


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

    def __check_test_attitude(self, text):
        for key_word in self.advertisement:
            if key_word in text:
                return 'advertisement'

        for key_word in self.analytics:
            if key_word in text:
                return 'analytic'
        return 'Undefined'

    def __handle_data(self, data):
        for key, values in data.items():
            if (key == 'sentences') and values:
                for i in values:
                    permission = i['annotations'][0]['practice']
                    if '3rdParty' in permission:
                        text_attitude = self.__check_test_attitude(i['sentence_text'])
                        all_permissions = [i['sentence_text'], new_features[permission], text_attitude]
                        self._permissions.append(all_permissions)

    def get_company_data(self) -> tuple:
        return self._permissions, self._company_name
