import allsymbolextractor,nonterminalextractor,first
def follow(grammar,nonTerminal):
    allsymbols=allsymbolextractor.allSymbol(grammar)
    nonterminals=nonterminalextractor.nonterminal(grammar)
    terminals=[n for n in allsymbols if n not in nonterminals]
    print(terminals)
    print(nonterminals)
    print(nonTerminal)
    followList=[]

    startSymbol,_=grammar[0].split("\N{RIGHTWARDS ARROW}")
    for prod in grammar:
        left,right= prod.split("\N{RIGHTWARDS ARROW}")
        # right needs to be shifted to find the nonterminal
        for character in right:
            if (character==nonTerminal):
                occur=right.index(character)
                print(occur)
                try:
                    if(left[0]==startSymbol):
                        followList+=["$"]
                    if(right[occur]==right[-1]):
                        followList+=follow(grammar,left[0])
                    if(right[occur+1] in terminals):
                        followList+=right[occur+1]
                        
                    elif(right[occur+1] in nonterminals):
                        followList+=first.first(grammar,right[occur+1])
                except IndexError:
                    continue
    return list(set(followList))

if __name__=="__main__":
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    nonterminals=['E', 'T', 'F']

    print(follow(grammar,"F"))