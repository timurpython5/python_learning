person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
additional_person_info = {
    "job": "Engineer",
    "married": True,
    "city": "London"
}

person = person | additional_person_info

print(person)