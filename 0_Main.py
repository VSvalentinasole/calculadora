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
        amortizacion = round(a * 0.075)
        if a>=50:
            cantidad_horas = (a/60)
            st.write(f"Combustible (8 LITROS/100KM): {round(resultado)} LITROS")
            st.write(f"Precio combistible (1.8 EUROS/LITRO): {precio} EUROS")
            st.write(f"Amortización (7.5 CENT/KM): {amortizacion} EUROS")
            st.write(f"Conductor (60KM/H): {round(cantidad_horas)} HORAS")
            precio_por_horas = round(cantidad_horas * 15)
            st.write(f"Precio conductor (15 EUROS/HORA): {precio_por_horas} EUROS")
            total = precio_por_horas + amortizacion + precio
            st.write(f"Total: {total} EUROS")
        
        else:
            cantidad_horas = ((a*60)/60)
            st.write(f"Combustible (8 LITROS/100KM): {round(resultado)} LITROS")
            st.write(f"Precio combistible (1.8 EUROS/LITRO): {precio} EUROS")
            st.write(f"Amortización (7.5 CENT/KM): {amortizacion} EUROS")
            st.write(f"Conductor (60KM/H): {round(cantidad_horas)} MINUTOS")
            precio_por_horas = round(cantidad_horas * 0.25)
            st.write(f"Precio conductor  (15 EUROS/HORA): {precio_por_horas} EUROS")
            total = precio_por_horas + amortizacion + precio
            st.write(f"Total: {total} EUROS")
        
if __name__ == "__main__":
    main()
