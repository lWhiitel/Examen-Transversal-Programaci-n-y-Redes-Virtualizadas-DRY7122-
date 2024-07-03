opcion = input("Quieres consultar una ACL (S/N): ")
while True:
    if opcion == "S":
        acl = int(input("Cual es el numero IPV4 ACL? "))
        if acl >= 1 and acl <= 99:
            print("!! ACL IPV4 Estandar !!")
        elif acl >=100 and acl <= 199:
            print("!! ACL IPV4 Extendida !!")
        else:
            print("!! Esta ACL IPV4 no corresponde a extendida o estándar !!")
    elif opcion == "N":
        print("!! ADIOS !!: ")
        break