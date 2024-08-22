c={
    "carrier": " not mentioned",
    "invoice": " $234.00 (this is different)",
    "amount": " this is fine" 
}

def formating(b):
    for key,value in b.items():
        if "not" in value:
            b[key]="unknow"
        elif "(" in value:
            b[key]=value.split("(")[0]
        else:
          b[key]=value.split(" ")[1:-1]
    return b     
print(c)
a=formating(c)
print(a)



