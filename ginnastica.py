with open("scores.txt","r") as file:
    liste=[]
    for line in file:
        i=0
        stripped=line.strip()
        splitted=stripped.split(" ")
        new=[]
        for eleman in splitted:
            if i==0 or i==1 or i==2 or i==3:
                new.append(str(eleman))
            else:
                new.append(float(eleman))
            i+=1
        liste.append(new)
    sum1=[]
    a=0
    for karakter in range(len(liste)):
        sum1.append(liste[karakter][4:])
    for element in sum1:
        q=sorted(element)
        q.pop(0)
        q.pop(-1)
        sums=[]
        sum=0
        for kar in q:
            sum=kar+sum
            sums.append(sum)
        liste[a].insert(0,round(sum,2))
        a+=1

    females=[]
    for deli in range(len(liste)):
        if liste[deli][3]=="F":
            females.append(liste[deli])

    print("Female winner:")
    print(f"{sorted(females)[-1][1]} {sorted(females)[-1][2]} {sorted(females)[-1][4]}--Score:{sorted(females)[-1][0]}")
    print("overall national rankings:")
    ita=0
    usa=0
    rus=0
    gbr=0
    for p in liste:
        if (p[4])=="ITA":
            ita+=p[0]
        elif p[4]=="USA":
            usa+=p[0]
        elif p[4]=="RUS":
            rus+=p[0]
        elif p[4]=="GRB":
            gbr+=p[0]

    countries=[["ITA",ita],["USA",usa],["RUS",rus],["GRB",gbr]]
    names=[ita,usa,rus,gbr]
    r=0
    for g in range(len(countries)):
        for t in range(len(countries)-1):
            if sorted(names,reverse=True)[g] in countries[t]:
                print(f"{r+1}){countries[t][0]}--Total score: {countries[t][1]}")
                r+=1





















