a="abcdefghijklmnopqrstuvwxyz1234567890"
p=(input("rentre yon fraz\n")) 
for i in p:
    if not i in a :
        p=p.replace(i,"-") 
        
print ("le SLUG est:" , p )


