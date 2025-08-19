def ascii_scales(dim:str):
    i:int = 0
    j:int = 0
    prev:str = ""
    
    print(dim)

    while j < len(dim):
        i = 0
        if j % 2 == 0:
            prev = "/"
            print("/")
        else:
            prev = "\\"
            print("\\")

        while i < len(dim):
            if prev == "/":
                print("-\\")
            else:
                print("_/")
                
            i = i + 1
        
        j = j + 1
    
    return

i:str = ""

i = input()
ascii_scales(i)