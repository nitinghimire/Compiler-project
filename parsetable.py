import allsymbolextractor, nonterminalextractor, follow

def parseTable(grammar,itemSetDict):
    # let us define the parse table as a list of tuples
    table=[]
    allsymbols=allsymbolextractor.allSymbol(grammar)
    nonterminals=nonterminalextractor.nonterminal(grammar)
    terminals=[n for n in allsymbols if n not in nonterminals]
    followList= {n :follow.follow(grammar,n) for n in nonterminals}
    firstRow= terminals
    firstRow.append("$")
    firstRow+=nonterminals

    print(firstRow)

    table.append(firstRow)

    # last part  of goto contains the largest state value 
    states=itemSetDict[-1][0]

    for i in range(states+1):
        lists=[None]*states
        table.append(lists)
    
    #filling up the parsing table with shift action and goto entries
    for dictitem in itemSetDict:
        if dictitem[1] in terminals:
            table[dictitem[0]+1][firstRow.index(dictitem[1])]='s'+str(list(dictitem[2].keys())[0])

        if dictitem[1] in nonterminals:
            table[dictitem[0]+1][firstRow.index(dictitem[1])]=str(list(dictitem[2].keys())[0])

        # print(list(dictitem[2].values()))
        # print("This is between")
        # print(list(dictitem[2].values())[-1])

        if "." in [n[-1] for n in list(dictitem[2].values())[-1]]:
            
            for prod in list(dictitem[2].values())[-1]:
                if prod[-1]==".":
                    completedNonterminal,_=prod.split("\N{RIGHTWARDS ARROW}")
                    wholeProduction=prod.replace(".","")
                    break
            followTerminal= follow.follow(grammar,completedNonterminal)
            for symbol in followTerminal:
                
                table[list(dictitem[2].keys())[0]][firstRow.index(symbol)]="r"+str(grammar.index(wholeProduction))

    print(table)

if __name__=="__main__":
    import itemcollection
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    itemset=itemcollection.itemcollection(grammar)
    print(itemset)

    parseTable(grammar,itemset)