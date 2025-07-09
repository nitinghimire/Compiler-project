import input,goto,nonterminalextractor,allsymbolextractor
def itemcollection(grammar):
    augmentedGrammar=input.get_input(grammar)
    ntlist=nonterminalextractor.nonterminal(grammar)
    print("This is the changed  terminal list")
    print(ntlist)
    print("This is the changed  terminal list")

    # allsymbol=allsymbolextractor.allSymbol(grammar)
    nextsymbol = goto.nextSymbolList(augmentedGrammar)

    itemCollection=[]
    itemDictionary={}
    itemCollection.append(augmentedGrammar)
    # itemDictionary["0"]=itemCollection[0]

    finalCollectionList=[]
    index=0
    stateNumber=0
    while True:
        for symbol in nextsymbol:
            dictItem={}
            tempList=[]
            item=goto.goto(itemCollection[index],symbol,augmentedGrammar,ntlist)
            
            if(item in itemCollection):
                # if item already exists then we only regfer to the old one
                
                for i,_item in enumerate(itemCollection):
                    if _item == item:
                        dictItem[i]=item
                        tempList=[index,symbol,dictItem]
                        finalCollectionList.append(tempList)
                print('i have reached here')
            else:
                # if the item doesnt exist then we add new state
                stateNumber+=1
                dictItem[stateNumber]=item
                tempList=[index,symbol,dictItem]
                finalCollectionList.append(tempList)

            if(item not in itemCollection):
                itemCollection.append(item)
        # need to change the nextsymbol, also index
        try:
            index+=1
            nextsymbol=goto.nextSymbolList(itemCollection[index])
        except IndexError :
            print("This is the changed non terminal list")
            print(ntlist)
            print("This is the changed non terminal list")

            print("This is item collection")
            print(itemCollection)
            print("This is item collection")
            return finalCollectionList


    

    # for index, item in enumerate(itemCollection):
    #     print(item)
    #     itemDictionary.update([(index,item)])
        
        

    print(itemCollection)
    print(itemDictionary)
    print(finalCollectionList)
    

if __name__=="__main__":
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    print(itemcollection(grammar))