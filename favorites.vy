# pragma version 0.4.0
# @license MIT

# storage variable onot get initialzed
struct Person:
    favourite_number: uint256
    name: String[100]

my_favourite_number: public(uint256) #0


list_of_numbers: public(uint256[5])
list_of_people: public(Person[5])
list_of_people_index: uint256

name_to_favourite_number: public(HashMap[String[100],uint256])

@deploy
def __init__():
    self.my_favourite_number = 7


@external  # that means this contract is called by us and people outside also call this function
# @internal  # this called with the internal function only
def store(new_number: uint256):
    # here self is very specific this means the contract that we are in --> state variable
    self.my_favourite_number = new_number
    

# cannot call external function vis self or via library

@external
def add():
    self.my_favourite_number += 1



# while reading we donot spend gas to read from the blockchain
# we have to spend the gas for updating the state of the blockchain


@external
@view  # by this state that we are only returning there is no need to update the state of blockchain
def retrieve() -> uint256:
    return self.my_favourite_number


@external
def add_person(new_name: String[100],new_number: uint256):
    # Add favourite number to the numbers list

    # Add the person to the person's list
    new_person: Person = Person(favourite_number = new_number,name = new_name)
    self.list_of_people[self.list_of_people_index] = new_person
    self.list_of_numbers[self.list_of_people_index] = new_number
    self.list_of_people_index = self.list_of_people_index + 1

    self.name_to_favourite_number[new_name] = new_number
