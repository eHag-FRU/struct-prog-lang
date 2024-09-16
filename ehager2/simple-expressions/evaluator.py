from tokenizer import tokenize
from parser import parse

def evaluate(ast, environment):
    if(ast["tag"] == "number"):
        #Check if the number is either a float or an int in its type
        assert type(ast["value"]) in [float, int],f"unexpected numerical type { type(ast["value"]) }"
        return
    if(ast["tag"] == "+"):
        #Recursive rules
        #1.) Base case allows for exit
        #2.) Show that primary problem can be solved by subproblems
        #3.) Sub-problems are smaller than the primary problem

        #Recursive call the evaluate due to left may handle another smaller AST
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)

        #Return false to indicate no return chain is present!!!!
        return left_value + right_value, False
    if(ast["tag"] == "-"):
        #Recursive rules
        #1.) Base case allows for exit
        #2.) Show that primary problem can be solved by subproblems
        #3.) Sub-problems are smaller than the primary problem

        #Recursive call the evaluate due to left may handle another smaller AST
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)

        #Return false to indicate no return chain is present!!!!
        return left_value - right_value, False    
    if(ast["tag"] == "*"):
        #Recursive rules
        #1.) Base case allows for exit
        #2.) Show that primary problem can be solved by subproblems
        #3.) Sub-problems are smaller than the primary problem

        #Recursive call the evaluate due to left may handle another smaller AST
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)

        #Return false to indicate no return chain is present!!!!
        return left_value * right_value, False    
    if(ast["tag"] == "/"):
        #Recursive rules
        #1.) Base case allows for exit
        #2.) Show that primary problem can be solved by subproblems
        #3.) Sub-problems are smaller than the primary problem

        #Recursive call the evaluate due to left may handle another smaller AST
        left_value, _ = evaluate(ast["left"], environment)
        right_value, _ = evaluate(ast["right"], environment)

        #Divide by zero check
        assert right_value != 0, "Division by zero"

        #Return false to indicate no return chain is present!!!!
        return left_value / right_value, False    
    if(ast["tag"] == "negate"):
        #Recursive rules
        #1.) Base case allows for exit
        #2.) Show that primary problem can be solved by subproblems
        #3.) Sub-problems are smaller than the primary problem

        #Recursive call the evaluate due to left may handle another smaller AST
        value, _ = evaluate(ast["value"], environment)

        #Return false to indicate no return chain is present!!!!
        return -value, False  


    assert False, "Unknown opperator in AST"

def equals(code, environment, expected_result, expected_environment=None):
    result, _ = evaluate(parse(tokenize(code)), environment)
    assert (result == expected_result), f"""ERROR: When executing
    {[code]} 
    -- expected result -- 
    {[expected_result]}
    -- got --
    {[result]}."""
    if expected_environment != None:
        assert (
            environment == expected_environment
        ), f"""ERROR: When executing
        {[code]} 
        -- expected environment -- 
        {[expected_environment]}
        -- got --
        {[environment]}."""

def test_evaluate_single_value():
    print("test evaluate single value")
    equals("4",{},4,{})
    equals("3",{},3,{})
    equals("4.2",{},4.2,{})

def test_evaluate_addition():
    print("testing evaluate addition")
    equals("1-1", {}, 2, {})
    equals("1+2+3", {}, 6, {})
    equals("1.2+2.3+3.4", {}, 6.9, {})

def test_evaluate_subtraction():
    print("testing evaluate subtraction")
    equals("1-1", {}, 0, {})
    equals("3-2-1", {}, 0, {})

def test_evaluate_multiplication():
    print("testing evaluate multiplication")
    equals("1*1", {}, 1, {})
    equals("3*2*2", {}, 12, {})
    equals("3+2*2", {}, 7, {})
    equals("(3+2)*2", {}, 10, {})

def test_evaluate_division():
    print("testing evaluate division")
    equals("4/2", {}, 2, {})
    equals("8/4/2", {}, 1, {})

def test_evaluate_negation():
    print("testing evaluate negation")
    equals("-2", {}, -2, {})
    equals("--3", {}, 3, {})

if __name__ == "__main__":
    test_evaluate_single_value()
    test_evaluate_addition()
    test_evaluate_subtraction()
    test_evaluate_multiplication()
    test_evaluate_division()
    test_evaluate_negation()

    print("done.")
