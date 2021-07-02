def reverse_fun(param):
  return param[::-1]

def reverse_word(param):
    words= param.split(' ')
    return words[::-1]
mytxt = reverse_fun("I wonder how this text looks like backwards")
mytxt2 = reverse_word("I wonder how this text looks like backwards")
print(mytxt)
print(mytxt2)