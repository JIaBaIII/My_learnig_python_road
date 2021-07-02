import ast

response_ws = input()
response_dict = ast.literal_eval(response_ws)
print(type(response_dict))
