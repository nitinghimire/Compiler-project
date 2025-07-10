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
    firstRow=(firstRow)

    print(firstRow)

    table.append(firstRow)

    # last part of goto contains the largest state value 
    states=itemSetDict[-1][0]

    for i in range(states+1):
        table.append([None] * len(firstRow))

    # filling up the parsing table with shift action and goto entries
    for dictitem in itemSetDict:
        if dictitem[1] in terminals:
            print("helllodfasoidfhoahsdf")
            print(list(dictitem[2].keys())[0])
            table[dictitem[0]+1][firstRow.index(dictitem[1])] = 's' + str(list(dictitem[2].keys())[0])

        if dictitem[1] in nonterminals:
            table[dictitem[0]+1][firstRow.index(dictitem[1])] = int(list(dictitem[2].keys())[0])

        print("this one right here asdfasdfasdf")
        print(list(dictitem[2].values())[-1])

        if any(prod.endswith('.') for prod in list(dictitem[2].values())[-1]):
            for prod in list(dictitem[2].values())[-1]:
                if prod.endswith("."):
                    completedNonterminal, _ = prod.split("\N{RIGHTWARDS ARROW}")
                    print(completedNonterminal)
                    wholeProduction = prod.replace(".", "")
                    print(wholeProduction)
                    break
            followTerminal = follow.follow(grammar, completedNonterminal)
            print(followTerminal)

            print(grammar[0].split("\N{RIGHTWARDS ARROW}")[0])
            print("above")
            print(list(dictitem[2].keys())[0])

            if completedNonterminal.endswith("'"):  # Check if it's the augmented start symbol
                table[list(dictitem[2].keys())[0]+1][firstRow.index("$")] = "Accept"


            for symbol in followTerminal:
                table[list(dictitem[2].keys())[0]+1][firstRow.index(symbol)] = "r" + str(grammar.index(wholeProduction))

    print(table)
    return table, firstRow

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
