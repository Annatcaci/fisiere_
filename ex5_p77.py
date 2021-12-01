def Check_Voc(vocale):
    with open("exercitiul5.txt") as f:
        a=f.read()

    for i in a:
        if i.isalpha()==True:
            b=[i for i in a if i in vocale]
            print(len(b)," - numarul de vocale")
            print(b)
    print("Ana")
vocale="AaOoUuIiEe"
