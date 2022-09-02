print("caluclate perimeter and area")
print("1.rectangle")
print("2.circle")
print("3.triangle")
choice=int(input("enter your choice"))
if choice==1:
    a=int(input("enter length"))
    b=int(input("enter breadth"))
    rperimeter=2*(a*b)
    rarea=a*b
    print("perimeter of rectangle is",rperimeter)
    print("area of rectangle is",rarea)
elif choice==2:
    a=float(input("enter radius"))
    carea=3.14*a*a
    cperimeter=2*3.14*a
    print("perimeter of circle is",cperimeter)
    print("area of circle is",carea)
elif choice==3:
    a=int (input("enter first side"))
    b=int(input("enter second side"))
    c=int(input("enter third side"))
    tperimeter=a+b+c
    tarea=0.5*a*b
    print("perimeter of traingle is",tperimeter)
    print("area of traingle is",tarea)