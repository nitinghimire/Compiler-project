from tabulate import tabulate
import parsetable,itemcollection

if __name__=="__main__":
    grammar= ["E\N{RIGHTWARDS ARROW}E+T",
               "E\N{RIGHTWARDS ARROW}T",
               "T\N{RIGHTWARDS ARROW}TF",
               "T\N{RIGHTWARDS ARROW}F",
               "F\N{RIGHTWARDS ARROW}F*",
               "F\N{RIGHTWARDS ARROW}a",
               "F\N{RIGHTWARDS ARROW}b",]
    
    itemset=itemcollection.itemcollection(grammar)
    print(itemset)

    table,columnIndex=parsetable.parseTable(grammar,itemset)
    print(table)

    stack=["$","0"]
    input_buffer=["$","b","+","a"]

    while True: 
        result = table[int(stack[-1])+1][columnIndex.index(input_buffer[-1])]
        if result==None:
            raise AttributeError("There is no such entry in the parse table. Parsing Failed!")
        if(result[0]=="s"):
            print("here")
            print(stack)
            print(input_buffer)
            stack.append(input_buffer[-1])
            stack.append(result[1:])
            input_buffer.pop()
            print(stack)
            print(input_buffer)
            continue
        if(result[0]=="r"):
            # try:
            sizeOfR=len(grammar[int(result[1:])].split("\N{RIGHTWARDS ARROW}")[-1])
            print(stack)
            for i in range(2*sizeOfR):
                stack.pop()
            print(stack)
            stack.append(grammar[int(result[1:])].split("\N{RIGHTWARDS ARROW}")[0])
            print(stack)
            result=table[int(stack[-2])+1][columnIndex.index(stack[-1])]
            stack.append(result)
            print(stack)
            continue
            # except:
            #     print("error converting")
        if result=="Accept":
            break
        
        
        print(result)
        
    table, columnIndex = parsetable.parseTable(grammar, itemset)
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    print("Parsing was a Success!")