from tokenizer import tokenize
from parser import parse

#Enviornment to help with variables and other values that live there for context
def evaluate(ast, enviornment):
    return 4, False

#Speeds up testing
def equals(code, enviornment, expected_result, expected_enviornment=None):
    result, _ = evaluate(parse(tokenize(code)), enviornment)
    print (enviornment)
    assert (result == expected_result), f"""ERROR: When executing {[code]} 
    -- expected --
    {[expected_result]}
    -- got --
    {[result]}."""

    if expected_enviornment != None:
        assert (
            enviornment == expected_enviornment
        ), f"""ERROR: When executing
        {[code]}
        
        -- Expected Enviornment --
        {[expected_enviornment]}
        
        -- Got --
        {[enviornment]}."""

def test_evaluate_single_value():
    print("test evaluate single value")
    equals("4", {}, 4, {})

if  __name__ == "__name__":
    test_evaluate_single_value()
    print("done.")