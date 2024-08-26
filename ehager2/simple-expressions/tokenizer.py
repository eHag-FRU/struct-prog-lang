
#tokenizer

"""

break character stream into tokens, provide a token stream
"""

import re

#Caches the machinery that comes from the expression
#Escapping \ with \\
patterns = [
    ["\\(", "("],
    ["\\)", ")"],
    #["\\+\\+", "++"],
    ["\\+", "+"],
    ["\\-", "-"],
    ["\\*", "*"],
    ["\\/", "/"],
    [

        ["(\\d+\\.\\d*)|(\\d*.\\d+)|(\\d+)"], "number",
    ],

]

#Replaces the expressions into machines, compiles!!!!!
#Not actual expressions but a machine when compiled
for pattern in patterns:
    pattern[0] = re.compile(pattern[0])



def tokenize(characters):
    tokens = [] #Parsed tokens
    position = 0    #Position in string 

    #While still chars
    while position < len(characters):
        for pattern, tag in patterns:
            #Now a machine, not expression, so can check equality with it
            match = pattern.match(characters, position)

            if match:
                #Found match, quit looking, now can process
                break

        #NEVER PARSES AN EMPTY PATTERN SET!
        assert match

        #Now store the tag, to show the context of the match
        #Group 0 gives the smallest group of all of the matches
        #Position to give ideas where errors in tokens are located
        #Makes easier for debugging
        token = {
            'tag': tag,
            'value': match.group(0),
            'position': position,
        }
        position = match.end()
        tokens.append(token)

        for token in tokens:
            #Convert to integer OR float
            if token["tag"] == "number":
                if "." in token["value"]:
                    token[value] = float(token["value"])
                else:
                    token[value] = int(token["value"])

    return tokens
        

def test_simple_tokens():
    print("Testing simple tokens")

    #Testing the function
    assert tokenize("+") == [{'tag': '+', 'value': '+', 'position': 0}]
    assert tokenize("-") == [{'tag': '-', 'value': '-', 'position': 0}]

    #Position tracker
    i = 0

    for char in "+-*/":
        # print(tokens)

        #Assert each one
        assert tokens[0]["tag"] == char
        assert tokens[0]["value"] == char
        assert tokens[0]["position"] == i

    for characters in ["+", "-"]:
        tokens = tokenize(characters)
        assert tokens[0]["tag"] == characters
        assert tokens[0]["value"] == characters




    for number in ["123.45", "1.", ".1", "123"]:
            tokens = tokenize(number)
            assert tokens[0]["tag"] == "number"


    #Update position
    i = i + 1




#Main function
if __name__ == "__main__":
    test_simple_tokens()
    tokens = tokenize("123.45")
    print(tokens)
    print("done.")

    