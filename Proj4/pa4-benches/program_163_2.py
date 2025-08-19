a:[str] = None
b:str = ""
i:int = 0


a = ["start: "]
b = input() 
print(b)
while i < len(b):
  a = a + [b[i]]
  print(b[i]) 
  i = i + 1

i = 0
while i < len(a):
  print(len(a[i]))
  i = i + 1
