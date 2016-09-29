#Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
#Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
#Have sonny greet jordan using the greet method.
#Have jordan greet sonny using the greet method.
#Write a print statement to print the contact info (email and phone) of Sonny.
#Write another print statement to print the contact info of Jordan.

class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_people_greeted = 0

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1


    def print_contact_info(self):
        print "%s's email: %s, %s's phone number: %s" % (self.name, self.email, self.name, self.phone)

    def add_friend(self, new_friend):
        self.friends.append(new_friend)

    def num_friends(self):
        print len(self.friends)

    def __repr__(self):
        return "" % (self.name, self.email, self.phone, self.friends, self.greeting_count)

    #def num_unique_people_greeted(self, other_person):



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
sonny.greet(jordan)
jordan.greet(sonny)
print sonny.email, sonny.phone
print jordan.email, jordan.phone

#Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person.
sonny.print_contact_info()

#Implement an add_friend method to Person
jordan.friends.append(sonny)
sonny.friends.append(jordan)

print len(jordan.friends) #Print to test and see if append is working

jordan.add_friend(sonny)
jordan.num_friends()

#Add a greeting count
sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
print sonny.greeting_count
