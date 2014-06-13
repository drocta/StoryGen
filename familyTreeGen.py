"""Family tree generator

NOTE:
This is for default things. Not intended as social commentary.
It should be easy to modify if desired."""
import random

listOfMaleNames=["Tim", "Joe", "Dude", "Claudius", "Frank", "John", "Smith"]
listOfFemaleNames=["Bria", "Ann", "Abby", "Abba", "Jane"]

class Person():
    """A person for a generated family tree.
        TODO: add support for adopted children, and remarried people
        TODO: if two people are made to be spouses, combine their children list
        current methods:
        __str__
        consistentify # not implemented
        setFather
        setMother
        setSpouse
        newSpouse
        addChild
        newChild
        addChildToCouple (maybe rename/combine)
        newChildForCouple
        ensureParentsAreMarried
        """
    def __init__(self,gender=False):
        self.children=[]
        self.father=None
        self.mother=None
        self.spouse=None
        if(gender==False):
            self.gender=random.choice(["Male","Female"])
        else:
            self.gender=gender
        if(self.gender=="Male"):
            self.firstName=random.choice(listOfMaleNames)
        elif(self.gender=="Female"):
            self.firstName=random.choice(listOfFemaleNames)
        else:
            self.firstName="None"
        self.lastName="Noneson"
        self.spouse=None
    def __str__(self):
        return self.firstName+" "+self.lastName
    def consistentify(self):
        pass #not implemented
    def setFather(self,father):
        self.father=father
        if((self.father.lastName=="Noneson")):
            if(self.lastName=="Noneson"):
                self.lastName=self.father.firstName+"son"
        else:
            self.lastName=self.father.lastName
        if(self not in father.children):
            father.children.append(self)
        #if(self.mother!=None):
        #    father.setSpouse(self.mother)
        self.ensureParentsAreMarried()
    def setMother(self,mother):
        self.mother=mother
        if(self.lastName=="Nonesone"):
            self.lastName=self.mother.lastName
        if(self not in mother.children):
            mother.children.append(self)
        #if(self.father!=None):
        #    mother.setSpouse(self.father)
        self.ensureParentsAreMarried()
    def setSpouse(self,spouse):
        self.spouse=spouse
        spouse.spouse=self
    def newSpouse(self):
        newSpouse = Person(oppositeGender(self.gender))
        self.setSpouse(newSpouse)
        self.spouse.lastName=self.lastName
        return newSpouse
    def addChild(self,child):
        self.children.append(child)
        if(self.gender=="Male"):
            child.setFather(self)
        elif(self.gender=="Female"):
            child.setMother(self)
        else:
            print "error."#not implemented
    def newChild(self):
        child=Person()
        self.addChild(child)
        #self.spouse.addChild(child)
        return child
    def addChildToCouple(self,child):
        self.addChild(child)
        if(self.spouse!=None):
            self.spouse.addChild(child)
    def newChildForCouple(self):
        child=Person()
        self.addChildToCouple(child)
        return child
    def newFather0(self):
        if(self.father!=None):
            return False
        self.father=Person("Male")
        self.father.addChild(self)
        if(self.mother!=None):
            self.father.setSpouse(self.mother)
            self.father.lastName=self.mother.LastName
        if(self.spouse==None):
            self.father.lastName=self.lastName
        else:
            if(self.spouse.parentsLastName()==self.lastName):
                self.father.lastName=newLastName()
            else:
                if(self.gender=="Male"):
                    self.father.lastName=self.lastName
                else:
                    self.father.lastName=newLastName()
        return self.father
    def newParent(self):
        np=Person("notYetSet")
        if(self.parentsLastName()!=None):
            np.lastName=self.parentsLastName()
        elif((self.spouse!=None) and (self.spouse.parentsLastName()==self.lastName)):#second part is not evaluated if they don't have a spouse
            np.lastName=newLastName()
        elif((self.spouse!=None) and (self.spouse.parentsLastName()!=None)):#ditto. (because of how and works)
            np.lastName=self.lastName
        elif(self.gender=="Male"):
            np.lastName=self.lastName
        else:
            np.lastName=newLastName()
        return np
    def newMother(self):
        if(self.mother!=None):
            print "warning: mother already set, returning current mother."
            return self.mother
        nm=self.newParent()
        nm.gender="Female"
        nm.firstName=random.choice(listOfFemaleNames)
        self.mother=nm
        nm.addChild(self)
        self.ensureParentsAreMarried()
        return nm
    def newFather(self):
        if(self.father!=None):
            print "warning: father already set, returning current father."
            return self.father
        nf=self.newParent()
        nf.gender="Male"
        nf.firstName=random.choice(listOfMaleNames)
        self.father=nf
        nf.addChild(self)
        self.ensureParentsAreMarried()
        return nf
        
            

    def parentsLastName(self):
        father,mother=self.father,self.mother
        if((father==None)and(mother==None)):
            return None
        eitherParent=father or mother # based on how or is handled. If father is truthy, results in father. otherwise results in mother.
        #as neither are None at this line, this will yield a valid Person object
        return eitherParent.lastName

    def ensureParentsAreMarried(self):
        if((self.father and self.mother)!=None):#ensures that both parents exist
            self.father.setSpouse(self.mother)
    




def oppositeGender(gender):
    if(gender=="Male"):
        return "Female"
    elif(gender=="Female"):
        return "Male"
    else:
        return random.choice(["Male","Female"])

def newLastName():
    return random.choice(["Baker","Barker","Smith","Dudeson","Lenhart","Thompson","Posener","Diaz","Drefs"])

def indentLines(someStr):
    lines=someStr.split("\n")
    if(lines[-1]==""):
        lines.pop(-1)
    outStr="\n    ".join(lines)
    outStr="    "+outStr
    return outStr

def dispFamily1(aPerson):
    outText=""
    outText+= str(aPerson) + " , " + str(aPerson.spouse) +"\n    children: "
    for child in aPerson.children:
        outText+= str(child)+ ", "
    #outText+="\n"
    for child in aPerson.children:
        outText+=indentLines("\n("+dispFamily1(child)+")")
    return outText
