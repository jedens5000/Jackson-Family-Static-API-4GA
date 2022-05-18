
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "Michael",
            "last_name": last_name,
            "age": "50 deceased",
        },
        {
            "id": self._generateId(),
            "first_name": "Tito",
            "last_name": last_name,
            "age": 68,
        },
        {
            "id": self._generateId(),
            "first_name": "Jackie",
            "last_name": last_name,
            "age": 71,
        },
        {
            "id": self._generateId(),
            "first_name": "Jermaine",
            "last_name": last_name,
            "age": 67,
        },
        {
            "id": self._generateId(),
            "first_name": "Marlon",
            "last_name": last_name,
            "age": 65,
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 9)

    def add_member(self, member):
        _members.append(member)
        return "item has been added"

    def delete_member(self, id):
        for member in self._members: # or --> for member in _members:
            if id == member.id:
                _members.remove(member)
        return "item has been removed"
        

    def get_member(self, id):
        for member in self._members: 
            if id == member.id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
