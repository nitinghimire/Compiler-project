def allSymbol(grammar):
    allSymbols=[]
    for prod in grammar:
        characterList=list(prod)
        allSymbols=allSymbols+characterList
    allSymbols=list(set(allSymbols))
    allSymbols.remove("\N{RIGHTWARDS ARROW}")
    return allSymbols

if __name__=="__main__":
    grammar= allSymbol(["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",])
    print(grammar)