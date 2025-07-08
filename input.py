def get_input(grammar):
    print(grammar)
    augmented_grammar= []
    startSymbol, _ =grammar[0].split("\N{RIGHTWARDS ARROW}")
    augmented_grammar.append(startSymbol+'\''+"\N{RIGHTWARDS ARROW}"+"."+startSymbol)
    for production in grammar:
        left, right =production.split("\N{RIGHTWARDS ARROW}")
        augmented_grammar.append(left+"\N{RIGHTWARDS ARROW}."+right)
    return augmented_grammar


if __name__=="__main__":
    grammar= get_input(["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",])
    print(grammar)