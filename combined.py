from familyTreeGen import *


"""
##########################################
######## #  #  Story Gen  #  # ###########
##########################################

<stuff>
ok this has a start of how Arcs could work, but needs way to handle Setting and characters.
Things responsible for Setting should have Places be a class maybe.


"""

class Character(Person):#may also extend other classes in the future, such as char from timeless expanse
    def __init__(self,significance=0,protagonistAlly=0.5):
        Person.__init__(self)
        self.signif=significance
        self.protAlly=protagonistAlly
    #some other stuff




class Event():#should this exist?
    pass

class MajorEventOld(Event):#e.g. stated goals, challenges, end outcomes, real goals
    #should major event extend event? idk. maybe event shouldn't be a class
    def __init__(self,majorEventType,param1,param2=None,param3=None):
        #??? does this even need to be initialized or does it just have subclasses?
        #oh, this could have things with the type of event, and the parameters, ok
        self.majorEventType=majorEventType
        self.param1=param1
        self.param2=param2
        self.param3=param3
        pass
    pass




#wait, should types of major events be subclasses of majorEvent or instances?
#if its instances than it might be hard to put stuff for where what to do with the different types goes
#and if its subclasses than it can be in the methods and stuff.
#ok.
#blah blah blah

class MajorEvent(Event):
    #general forms of the methods go here
    isFallingAction=False
    pass

class majorEventKill(MajorEvent):
    def __init__(self,killee,killer=None):
        self.killee=killee
        self.killer=killer #maybe these should be a generic thing, a generic for each MajorEvent subclass? I don't know.
        #maybe something to do with prerequisite things? (to allow for "first you must collect the 7 mcCrystals of Guffinland" type stuff

class majorEventGet(MajorEvent):
    def __init__(self,thingToGet,partyGetting=None,gettingFrom=None):
        self.thing=thingToGet
        self.partyGetting=partyGetting
        self.gettingFrom=gettingFrom

class majorEventGoTo(MajorEvent):
    def __init__(self,placeToGo,partyGoingTo=None,partyGoingFrom=None):
        self.placeToGo=placeToGo
        self.partyGoingTo=partyGoingTo
        self.partyGoingFrom=partyGoingFrom


#ok also needs a thing for storing the story's structure so that objects of these classes can be contained by them
#that way the MajorEvent subclasses can have a method called that populates more of the fields
#which then fleshes out the story
#Maybe this can be the same type of structure at multiple levels
#maybe something called arc or something.

class arc():#this is either the class for entire story arcs or for arcs of all sizes, maybe subclasses for different sizes
    def __init__(self,majorEndEvents,majorGoalEvents,subPeaksNumber=None):#maybe something else, maybe a scale
        self.majorEndEvents=majorEndEvents
        self.majorGoalEvents=majorGoalEvents #these names might have to be changed
        self.subPeaksNumber=subPeaksNumber
        self.subPeaksArr=[]#Maybe this could be a list of arcs? I think that makes sense.
        self.subTroughArr=[]#this too
        self.hook=None
        self.baseline=None
        self.climax=None
        self.fallingAction=None#should these be lists of arcs or arcs or events?
        #if they are
        #oh, they should probly be arcs


        
        #hmm, how to determine when it has recursed to the bottom level?
    def populateSubArcs(self,levels=0):#maybe the depth should be a propert of the object?
        endEventsCopy=self.majorEndEvents[:]
        endEventsCopyNextPass=[]
        fallingActionList=[]
        for majorEndEvent in endEventsCopy:#should this be in reverse order? falling action should be last but order of them shouldnt be reversed
            if(majorEndEvent.isFallingAction):#wait what if the endEvents on different levels? if something is falling action on one level but not on another?
                fallingActionList.append(majorEndEvent)#maybe this should be an insert? Maybe the isfallingaction should be a method not a field?
            else:
                endEventsCopyNextPass.append(majorEndEvent)
        if(fallingActionList==[]):
            fallingActionList.append(MajorEventGoTo("home/back"))#this event thing should be based on setting, which is the other half.
            
        #a=self.majorEndEvents
        #if(a.isFallingAction)
        pass
            
