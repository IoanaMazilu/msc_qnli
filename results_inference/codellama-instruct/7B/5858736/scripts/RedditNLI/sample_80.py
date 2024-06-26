# Define variables with representative names for the numerical entities in both inputs
coca_cola_expansion_value = 5.1
britain_whitbread_sale_value = 5.1

# Extract all quantities as valid numbers (integers or floats)
coca_cola_expansion_value = float(coca_cola_expansion_value)
britain_whitbread_sale_value = float(britain_whitbread_sale_value)

# Use brief comments to explain what comparison you do between the defined variables
if coca_cola_expansion_value!= britain_whitbread_sale_value:
    # Check if the expansion value of Coca-Cola contradicts the sale value of Whitbread
    label = "contradiction"
else:
    # If the expansion value and sale value do not contradict each other, we can infer entailment
    label = "entailment"

print(label)
