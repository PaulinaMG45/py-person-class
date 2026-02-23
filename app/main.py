class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int,
        **kwargs
    ) -> None:
        self.name = name
        self.age = age

        if kwargs.get("wife") is not None:
            self.wife = kwargs.get("wife")

        if kwargs.get("husband") is not None:
            self.husband = kwargs.get("husband")
            
        Person.people[name] = self


def create_person_list(people: list) -> list:

    people_ls = [Person(**person) for person in people]

    print(people_ls)

    for person in people_ls:

        if hasattr(person, "wife") and person.wife is not None:
            name = person.wife
            person.wife = Person.people[name]

        if hasattr(person, "husband") and person.husband is not None:
            name = person.husband
            person.husband = Person.people[name]

    return people_ls
