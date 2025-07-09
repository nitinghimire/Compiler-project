import allsymbolextractor,nonterminalextractor

def first(grammar,symbol):
    allsymbols=allsymbolextractor.allSymbol(grammar)
    nonterminals=nonterminalextractor.nonterminal(grammar)
    terminals=[n for n in allsymbols if n not in nonterminals]
    print(terminals)
    print(nonterminals)
    print(symbol)
    firstList=[]
    if(symbol[0] in terminals):
            firstList.append(symbol[0])
            return firstList
    if(symbol[0] in nonterminals):
        for prod in grammar:
            left,right= prod.split("\N{RIGHTWARDS ARROW}")
            if right[0]!=left[0]:
                if(left[0]==symbol[0]):
                    if(right[0] in nonterminals ):
                        print(right[0])
                        firstList=firstList+first(grammar,right[0])
                        print(firstList)
                    else:
                         firstList=firstList+[right[0]]
            if right[0]==left[0]:
                 continue
        return firstList
                 
                 
        




if __name__=="__main__":
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    nonterminals=['E', 'T', 'F']

    print(first(grammar,'E'))