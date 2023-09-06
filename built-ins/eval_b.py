"""
eval
The eval built-in is fairly controversial in the Python community. The reason
for this is that eval accepts strings and basically runs them. If we want to
allow users to input any string to be parsed and evaluated by eval, then we
just created a major security breach. However, if the code that uses eval is
only used by the developer and not the user, then it is okay to use. Some will
argue that it’s still not safe, but if we have a rogue developer, they can do
a lot more harm doing other things than using eval.
"""
var = 10
source = "var * 2"
print(eval(source))

"""
To evaluate a string-based expression, Python’s eval() runs the following steps:

* Parse expression
* Compile it to bytecode
* Evaluate it as a Python expression
* Return the result of the evaluation

There is another built-in function called exec which supports the dynamic 
execution of Python code. It’s a somewhat “dangerous” built-in too, but it 
doesn’t have a bad reputation that eval does. It’s a neat little tool, but use 
it with caution.
"""
