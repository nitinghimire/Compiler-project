 
def closure(aGrammar,item, ntlist):
    temp=[]
    ntlistnotseen=ntlist
    for _ in range(len(aGrammar)):
        for prod in item:
            try:
                _, right= prod.split(".")
            except ValueError as err:
                continue
            if(right ==""):
                continue
            # try:
            if(right[0] in ntlistnotseen):
                ntlistnotseen.remove(right[0])
                match = [n for n in aGrammar if n.split("\N{RIGHTWARDS ARROW}")[0]==right[0]]
                if (match is not None):
                    temp.extend(match)
                    item = list(set(item+temp))
            else: continue
            # except IndexError as err:
            #     print("Index error occured meaning that the . is at the end of the production")
            #     continue
        if(item is not None):
            item = list(set(item+temp))
    return item


if __name__=="__main__":
    import nonterminalextractor as nte
    import input
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    grammar=input.get_input(grammar)
    item=["E\N{RIGHTWARDS ARROW}.T"]
    ntlist=nte.nonterminal(grammar)
    print(closure(grammar,item,ntlist))

    # test for . at the end of production rule
    item=["E\N{RIGHTWARDS ARROW}T."]
    print(closure(grammar,item,ntlist))
    print(len(grammar))