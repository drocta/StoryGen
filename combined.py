from familyTreeGen import *


"""
##########################################
######## #  #  Story Gen  #  # ###########
##########################################

<stuff>

"""

class Character(Person):#may also extend other classes in the future, such as char from timeless expanse
    def __init__(self,significance=0,protagonistAlly=0.5):
        Person.__init__(self)
        self.signif=significance
        self.protAlly=protagonistAlly
