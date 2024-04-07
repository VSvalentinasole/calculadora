import streamlit as st

def regla_de_tres_combustible(a):
    if a != None:
        return (a * 8) / 100
    else:
        return 0

def main():
    st.title("Calculadora de valores")

    a_input = st.text_input("Ingrese la cantidad de kilómetros:")
    
    if a_input:  # Verificar si se ingresó un valor
        try:
            a = float(a_input)
        except ValueError:
            st.error("Error: Por favor ingrese un número válido.")
            return
        
        resultado = regla_de_tres_combustible(a)
        precio = round(resultado * 1.8)
        amortizacion = int(a * 0.075)
        cantidad_horas = int(a / 50)
        precio_por_horas = int(cantidad_horas * 15)
        total = precio_por_horas + amortizacion + precio

        st.write(f"El resultado de la cantidad de litros es: {int(resultado)} LITROS")
        st.write(f"El resultado del precio es: {precio} EUROS")
        st.write(f"Amortización: {amortizacion} EUROS")
        st.write(f"La cantidad de horas del conductor: {cantidad_horas} HORAS")
        st.write(f"Precio por horas: {precio_por_horas} EUROS")
        st.write(f"Total: {total} EUROS")

if __name__ == "__main__":
    main()
