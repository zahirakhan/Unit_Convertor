import streamlit as st

#Configuration 
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>UNIT CONVERTER</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Convert Units Easily in Lenghts, Weight & Temperature</p>", unsafe_allow_html=True)

# Conversion Data
conversion_factors = {
    "Length": {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254},
    "Weight": {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495},
    "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
}

# Sidebar
category = st.sidebar.selectbox("Select Unit Category", list(conversion_factors.keys()))
st.sidebar.markdown("Project By Zahira Khan")

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    base_value = value * conversion_factors[category][from_unit]
    return base_value / conversion_factors[category][to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Input 
units = list(conversion_factors[category].keys())
value = st.number_input(f"Enter value to convert ({category}):", min_value=0.0, step=0.1)
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Output
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.markdown(f"<p class='result'>{value} {from_unit} = <strong>{result:.4f} {to_unit}</strong></p>", unsafe_allow_html=True)
