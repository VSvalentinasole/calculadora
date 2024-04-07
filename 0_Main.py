import streamlit as st


def regla_de_tres_combustible(a):
    if a != None:
        return (a * 8) / 100
    else:
        return 0

def main():
    st.title("Calculadora de delivery")

    st.markdown("[Google Maps](https://www.google.com/maps)")

    a_input = st.text_input("Ingrese la distancia en kilometros:")
    
    if a_input:  # Verificar si se ingresó un valor
        try:
            a = float(a_input)
        except ValueError:
            st.error("Error: Por favor ingrese un número válido.")
            return
        
        resultado = regla_de_tres_combustible(a)
        precio = round(resultado * 1.8)
        amortizacion = int(a * 0.075)
        if a>=50:
            cantidad_horas = int(a/50)
            st.write(f"Conductor: {cantidad_horas} HORAS")

        else:
            cantidad_horas = int((a*60)/50)
            st.write(f"Conductor: {cantidad_horas} MINUTOS")

        precio_por_horas = int(cantidad_horas * 15)
        total = precio_por_horas + amortizacion + precio

        st.write(f"Combustible: {int(resultado)} LITROS")
        st.write(f"Precio combistible: {precio} EUROS")
        st.write(f"Amortización: {amortizacion} EUROS")
        st.write(f"Precio conductor: {precio_por_horas} EUROS")
        st.write(f"Total: {total} EUROS")

if __name__ == "__main__":
    main()
