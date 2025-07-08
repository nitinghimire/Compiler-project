def nonterminal(grammar):
    nonTerminals=[]
    for prod in grammar:
        nonTerminal,_=prod.split("\N{RIGHTWARDS ARROW}")
        nonTerminals.append(nonTerminal)
    nonTerminals=list(set(nonTerminals))
    return nonTerminals

if __name__=="__main__":
    grammar= nonterminal(["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",])
    print(grammar)