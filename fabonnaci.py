nterms=int(input("Enter no you want to print series:"))
n1,n2=0,1
count=0
if nterms<=0:
    print("please enter a positive integer!!!")
elif nterms==1:
    print("Fabonnaci series upto",nterms," :")
else:
    print("Fabonnaci series is:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    

