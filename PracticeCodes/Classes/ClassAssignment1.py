"""

STATUS :- In review

# *** Note: -  Read the given criteria line-by-line. First take notes and write how to design the class along with
Variables. Don't forget to change the status on line3 after completion of this assignment.

# TODO:- Create a class Person

# TODO: - The Person class consists of Person Age, Person Name, Person Married status, Person's number of Children,
# TODO: - and Person Children Names, person Gender, persons partner name

# What values can be expected in the class variables

1. Person Name            : The name should has the person's FIRST NAME and LAST NAME.

2. Person Age             : It store the person's age

#3. Married Status         : Single or Married or diverse

4. Person's children      : 0(Means person has No children) or 1(means pearson has 1 child) or 2(means person has 2 children)

5. Person's Children Name : [](means person has no children), ["XYZ"](Person has only one child and XYZ is his/her name)

6. Person's Gender        : Male or Female or Other.

7. Person's Partners Name : First and Last Name of the partner
"""


# Write your code here

class Person:
    def __init__(self, name, age, married, children, childrenname, gender, partnersname):
        self.name = name
        self.age = age
        self.married = married
        self.children = children
        self.childrenname = childrenname
        self.gender = gender
        self.partnersname = partnersname

    def setName(self, newName):
        self.name = newName

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def getMarried(self):
        print(self.married)

    def getChildren(self):
        print(self.children)

    def getChildrenName(self):
        print(self.childrenname)

    def getGender(self):
        print(self.gender)

    def getPartnersName(self):
        print(self.partnersname)


if __name__ == "__main__":
    p = Person("Chaitanya Krishna", 28, "married", 0, "NA", "Female", "Ranadeep")
    p.getName()
    p.getAge()
    p.getMarried()
    p.getChildren()
    p.getChildrenName()
    p.getGender()
    p.getPartnersName()

    # Here to setting the new name
    p.setName("Saikrishna")

    # printing the new name
    p.getName()

    print(p.gender)
