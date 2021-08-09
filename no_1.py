kata = input()
if kata.isupper():
    kevin= 0
    struat= 0
    vokal="AIUEO"

    for i in range(len(kata)):
        if kata[i] in vokal:
            kevin= kevin+len(kata)-i
        else:
            struat= struat+len(kata)-i
            
    if struat>kevin:
        print("Kevin :", kevin,"\n", "Stuart :", struat, "\n", "Pemenang : Stuart")
    elif struat==kevin:
        print("Kevin :", kevin,"\n", "Stuart :", struat, "\n", "Pemenang : Draw")
    else :
        print("Kevin :", kevin,"\n", "Stuart :", struat, "\n", "Pemenang : Kevin")
else:
    print("Input string hanya terdiri dari huruf kapital [A-Z]")

