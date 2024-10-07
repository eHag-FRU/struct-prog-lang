import sys

from pprint import pprint
from evaluator import evaluate
from parser import parse
from tokenizer import tokenize

def main():
    if len(sys.argv) > 1:
        #open file
        with open(sys.argv[1], 'r') as f:
            source_code = f.read()
        
        tokens = tokenize(source_code)
        ast = parse(tokens)
        evaluate(ast)
        exit

    #REPL Loop
    while True:
        environment = {}

        try:
            # read input
            source_code = input(">> ")
            if source_code.strip() in ["exit", "quit"]:
                break
            if source_code.strip in ["debug"]:
                debug = not(debug)
                continue
            tokens = tokenize(source_code)
            ast = parse(tokens)
            evaluate(ast, environment)
            if debug:
                pprint(environment)
        except Exception as e:
            print(f"Error: {e}")


if "__name__" == "__main__":
    main()