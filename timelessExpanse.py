class char():
    def __init__(self,vengefulness):
        self.knowsof=[]
        self.vengefulness=vengefulness
        self.protects={}
        self.protectedby={}
        self.name="wiggilytuff"

    def addProtectee(self,other,strength):
        "takes another thing and makes it protect the thing."
        self.protects[other]=strength
        other.protects[self]=strength

    def __str__(self):
        return self.name


def simulate(harmsListInitial):
    newHarmsList=harmsListInitial
    for i in range(5):
        harmsList=newHarmsList
        newHarmsList=[]
        for harm in harmsList:
            harmer,harmee,severity=harm
            if(severity==0):
                continue
            newHarmsList.append(
                (harmee,harmer,severity*harmee.vengefulness)
                )
            for protector in protectedby:
                #note: in this current version, does not take into account
                #allowing for someone to protect
                # "everyone they know of"
                #it also doesn't have 
                newHarmsList.append(
                    (protector,harmer,severity*harmee.protectedby[protector])
                    )
        harmSumDictionary={}
        for harm in newHarmsList:
            harmer,harmee,severity=harm
            if( (harmer,harmee) not in harmSumDictionary):
                harmSumDictionary[(harmer,harmee)]=0.0
            harmSumDictionary[(harmer,harmee)]+=severity
        newHarmsList=[]
        for pair in harmSumDictionary:
            harmer,harmee=pair
            severity=harmSumDictionary[pair]
            newHarmsList.append(
                (harmer,harmee,severity)
                )
            #ok
        
            
