Juguetes={
    'JM200':['Peluche','ansaldo',6,'inflable'],
    'BC190':['Piezas','megapieza',9,'Rompecabezas'],
    'PC122':['ROBOT','TRONIC',12,"Electrico"],

}

Inventario={

    'JM200':[10900,9],
    'BC190':[5890,2],
    'PC122':[18900,1]
}

def stock_tipo(tipo):
    total=0
    for codigo in Juguetes:
        if Juguetes[codigo][3].lower()==tipo.lower():
            total= total + Inventario[codigo][1]
    print(f"el stock para el tipo {tipo} es: {total}")

def bucar_por_precio(p_min, p_max):
    resultados=[]
    for codigo in Inventario:
        precio,stock = Inventario[codigo]
        if p_min<=precio<= p_max and stock >0:
            nombre,marca=Juguetes[codigo][0], Juguetes[codigo][1]
            resultados.append(f"{marca}-{nombre}")
    
    if resultados:
        print("juguetes encontrados", sorted(resultados))
    else:
        print("no hay juguetes en ese rango")

while True:
    print( "Menu")
    print("1- buscar por stock")
    print("2- buscar por rango de precios")

    opcion=input("ingrese su opcion")

    if opcion=="1":
        tipo = input("ingrese el tipo: ")
        stock_tipo(tipo)

    elif opcion=="2":
        try:
            p_min=int(input("precio minimo: "))
            p_max=int(input("ingrese precio maximo:"))
            bucar_por_precio(p_min,p_max)
        except:
            print("debe ingresar numeros xd")


    break