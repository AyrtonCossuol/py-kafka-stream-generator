import json

import faker

class GenerateDatafake:
    def __init__(self) -> None:
        self.fake = faker.Faker('pt-BR')

    def generate_json_fake(self) -> dict:
        """
        Gerador de informações fakes
        """
        simple_profile = self.fake.simple_profile()

        return json.dumps(
            {
                'user_fake': simple_profile['username'],
                'name_fake': simple_profile['name'],
                'sex_fake': simple_profile['sex'],
                'address_fake': ' '.join(simple_profile['address'].split('\n')),
                'email_fake': simple_profile['mail'],
                'birthdate_fake': str(simple_profile['birthdate'])
            }
        )