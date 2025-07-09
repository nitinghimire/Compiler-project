import closure

def nextSymbolList(item):
    symbols=[]
    for prod in item:
        right= prod.split('.')[-1]
        if(right[0] != ""):
            symbols.append(right[0])
    symbols=list(set(symbols))
    return symbols

def moveDot(prod):
    left,right=prod.split(".")
    print("This is in movedot")
    print(left+right[0]+"."+right[1:])
    return left+right[0]+"."+right[1:]

def goto(state,symbol,grammar,ntlist):
    nextItem=[]
    for prod in state:
        print(prod.split(".")[-1][0])
        # temp =[moveDot(n) for n in state if prod.split(".")[-1][0]==symbol]
        temp=[]
        if(prod.split(".")[-1][0]==symbol):
            temp=[moveDot(prod)]
        nextItem=nextItem+temp
        print("This is before closure")
        print(nextItem)
    nextItem=list(set(nextItem))
    print(nextItem)
    nextItem=closure.closure(grammar,nextItem,ntlist)
    print("this is after closure")
    print(nextItem)
    return nextItem
        


if __name__=="__main__":
    import input,nonterminalextractor
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    augmentedGrammar=input.get_input(grammar)
    print(augmentedGrammar)

    print(nextSymbolList(augmentedGrammar))

    print(moveDot("E\N{RIGHTWARDS ARROW}.T"))

    ntlist=nonterminalextractor.nonterminal(grammar)
    print(goto(augmentedGrammar,"T",augmentedGrammar,ntlist))