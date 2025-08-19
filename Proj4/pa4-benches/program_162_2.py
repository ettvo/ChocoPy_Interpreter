x:str = ""


def recursiveReversePrint(a:str):
  def helper(i:int):
    if (i < 0):
      return 
    else:
      print(a[i])
    while False:
      return 
    helper(i-1)
  print(a)
  helper(len(a)-1)
  return   
x = input()
recursiveReversePrint(x)
