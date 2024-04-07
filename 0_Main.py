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
        cantidad_horas = a / 50 if a >= 50 else (a * 60) / 50
        tiempo_unidad = "HORAS" if a >= 50 else "MINUTOS"
        precio_por_horas = int(cantidad_horas * 15)
        total = precio_por_horas + amortizacion + precio

        st.write(f"Combustible: {int(resultado)} LITROS")
        st.write(f"Precio combistible: {precio} EUROS")
        st.write(f"Amortización: {amortizacion} EUROS")
        st.write(f"Conductor: {round(cantidad_horas)} {tiempo_unidad}")
        st.write(f"Precio conductor: {precio_por_horas} EUROS")
        st.write(f"Total: {total} EUROS")
        
if __name__ == "__main__":
    main()
