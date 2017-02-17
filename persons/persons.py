import random
import string
class Person(object):
    """This is the base class for staff and fellow"""
    def __init__(self, name, designation):
        self.name = name
        self.ID = ""
        self.office = ""
        self.designation = designation

    def get_existing_id(self, person_list):
        """This function extracts a list of existing id from person list"""
        id_list = []
        for i in range(0, len(person_list)):
            id_list.append(person_list[i].ID)
        return id_list

    def generate_id(self, designation, person_list):
        """This function generates id for either staff or fellow."""
        prefix = "F-" if designation.lower() == "fellow" else "S-"
        id_exist = True
        person_id = ""
        while id_exist:
            person_id = prefix + ''.join(\
                    random.choice(string.ascii_uppercase + string.digits)
                                  for _ in range(5))
            if not (person_id in self.get_existing_id(person_list)):
                id_exist = False
            self.ID = person_id
