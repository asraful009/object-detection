
from faker.proxy import Faker
import random

class PersonInfo:
    def __init__(self, asserts_path, image="", locale="en_US"):
        self.__faker = Faker(locale)
        self.company = self.__faker.company()
        self.domain = self.__faker.domain_name()
        self.name = self.__faker.name()
        self.email = self.__faker.email(True, self.domain)
        self.phone = self.__faker.phone_number()
        self.position = self.__faker.job()
        self.company_email = self.__faker.email(True, self.domain)
        self.address = f"{self.__faker.building_number()} {self.__faker.street_name()} {self.__faker.country_code()}, {self.__faker.postcode()}"
        self.logo_path = image
        self.fonts = {}
        background_color = ["#FFF5E4", "#FFFBE6", "#F7F7F8", "#FFFBE6", "#ECFFE6",
                                 "#EEF7FF", "#E7FBE6"]
        self.background_color = background_color[random.randint(0, len(background_color) - 1)]

        if locale == "bn_BD":
            self.fonts["bold"] = f"{asserts_path}/fonts/bangla/NotoSerifBengali/NotoSerifBengali-Bold.ttf"
            self.fonts["regular"] = f"{asserts_path}/fonts/bangla/NotoSerifBengali/NotoSerifBengali-Regular.ttf"
            self.fonts["light"] = f"{asserts_path}/fonts/bangla/NotoSerifBengali/NotoSerifBengali-light.ttf"
        else:
            self.fonts["bold"] = f"{asserts_path}/fonts/JetBrainsMono-Bold.ttf"
            self.fonts["regular"] = f"{asserts_path}/fonts/JetBrainsMono-Regular.ttf"
            self.fonts["light"] = f"{asserts_path}/fonts/JetBrainsMono-light.ttf"

    def to_dict(self):
        return {
            "company": self.company,
            "domain": self.domain,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "position": self.position,
            "company_email": self.company_email,
            "address": self.address,
            "logo_path": self.logo_path,
            "fonts": self.fonts,
            "background_color" : self.background_color
        }