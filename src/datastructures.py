
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
        self._next_id = 4

        # example list of members
        self._members = [{
            "id": 1,
            "first_name" : "John",
            "last_name" : self.last_name,
            "age" : 33,
            "lucky_numbers" : [7,13,22]
        },

            {
            "id": 2,
            "first_name" : "Jane",
            "last_name" : self.last_name,
            "age" : 35,
            "lucky_numbers" : [10,14,3]
        },

            {
            "id": 3,
            "first_name" : "Jimmy",
            "last_name" : self.last_name,
            "age" : 5,
            "lucky_numbers" : [5]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId()
        member["last_name"] = self.last_name

        self._members.append(member)

        return member

    def delete_member(self, id):
        for index in range(len(self._members)):
            if self._members[index]["id"] == id:
                self._members.pop(index)
                return None

    def get_member(self, id):
        for item in self._members:
            if item["id"] == id:
                return item

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
