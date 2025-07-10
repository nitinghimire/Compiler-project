from tabulate import tabulate
import parsetable, itemcollection

if __name__ == "__main__":
    grammar = [
        "E\N{RIGHTWARDS ARROW}E+T",
        "E\N{RIGHTWARDS ARROW}T",
        "T\N{RIGHTWARDS ARROW}TF",
        "T\N{RIGHTWARDS ARROW}F",
        "F\N{RIGHTWARDS ARROW}F*",
        "F\N{RIGHTWARDS ARROW}a",
        "F\N{RIGHTWARDS ARROW}b",
    ]

    itemset = itemcollection.itemcollection(grammar)
    table, columnIndex = parsetable.parseTable(grammar, itemset)

    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

    stack = ["$", "0"]
    input_buffer = ["$", "b", "+", "a"]
    derivation_steps = []  
    
    
    def print_simulation_step(stack, input_buffer, output=""):
        stack_str = " ".join(str(x) for x in stack)
        input_str = " ".join(str(x) for x in reversed(input_buffer))
        print(f"{stack_str:<15} | {input_str:<15} | {output}")
    
    # Print header
    print("\nParsing Simulation:")
    print("Stack           | Input           | Output")
    print("-" * 50)
    
    # Print initial state
    print_simulation_step(stack, input_buffer)

    while True:
        result = table[int(stack[-1]) + 1][columnIndex.index(input_buffer[-1])]
        if result is None:
            raise AttributeError("There is no such entry in the parse table. Parsing Failed!")

        if result[0] == "s":
            stack.append(input_buffer[-1])
            stack.append(result[1:])
            input_buffer.pop()
            print_simulation_step(stack, input_buffer)
            continue

        if result[0] == "r":
            rule_index = int(result[1:])
            production = grammar[rule_index]
            rhs = production.split("\N{RIGHTWARDS ARROW}")[-1]
            sizeOfR = len(rhs)

            for _ in range(2 * sizeOfR):
                stack.pop()

            lhs = production.split("\N{RIGHTWARDS ARROW}")[0]
            stack.append(lhs)
            goto_result = table[int(stack[-2]) + 1][columnIndex.index(lhs)]
            stack.append(goto_result)

            derivation_steps.append(production)  
            print_simulation_step(stack, input_buffer, production)

            continue

        if result == "Accept":
            print_simulation_step(stack, input_buffer, "Accept")
            break

    print("\nParsing was a Success!")
    print("\nReverse of Rightmost Derivation:")
    for step in derivation_steps:
        print(step)