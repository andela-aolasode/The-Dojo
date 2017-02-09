from unittest import TestCase
from persons.persons import Persons
from persons.staffs import Staff
from persons.employees import Employee
from persons.fellows import Fellow

class TestPersons(TestCase):
    def test_add_person_successfully(self):
        """ This function test for successful adding of person """
        new_person = Persons()

        """ This check successful adding of staff person """
        new_staff = new_person.add_person("Andy Carroll", "staff")
        self.assertIsInstance(Staff)
        self.assertEqual(new_staff.name, "Andy Carroll")
        self.assertIsInstance(Employee)

        """ This check successful adding of fellow person """
        new_fellow = new_person.add_person("Jeremy Johnson", "fellow", "Y")
        self.assertIsInstance(Fellow)
        self.assertEqual(new_fellow.name, "Jeremy Johnson")
        self.assertIsInstance(Employee)
        self.assertEqual(new_fellow.livingspace, "")

    def test_add_person_invalid_input(self):
        """ This function checks for invalid inputs """
        new_person = Persons()

        """ Returns error message instead of object staff with invalid inputs """
        new_staff = new_person.add_person("Andy Carroll", "staff", "Y")
        self.assertEqual(new_staff,"Staff cannot request for a livingspace!")
        new_staff = new_person.add_person("  ", "staff")
        self.assertEqual(new_staff,"Staff cannot be created with empty name!")
        new_staff = new_person.add_person("Samora Dake","type","Y")
        self.assertEqual(new_staff,"Person cannot br created due to invalid designation!")
