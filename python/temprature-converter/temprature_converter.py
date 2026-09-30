F = 0
C = 0

def c_to_f(C):
    #Formel for convertering til F
    return (C * 9/5) + 32 

def f_to_c(F):
    #Formel for convertering til C
    return (F - 32) * 5/9 

#Bruker input
choice = input(" Vel Celsius(C) eller Fahrenheit(F): ").upper() 

#Hvis C velges, be om input, kjør formel og print
if choice == ("C"):
    c_value = float(input("How many degrees?: "))
    result = c_to_f(c_value)
    print(f"{c_value} Celsius blir {result: .1f} Fahrenheit.")

#Hvis F velges, be om input, kjør formel og print
elif choice == ("F"):
    f_value = float(input("How many degrees?: "))
    result = f_to_c(f_value)
    print(f"{f_value} Fahrenheit blir {result: .1f} Celsius.")

#All annen input feiler
else:
    print ("Ugyldig valg.")