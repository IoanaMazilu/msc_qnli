# Define variables with representative names for the numerical entities in both inputs
OA = 2
AC = 4
BD = 6

# Extract all quantities as valid numbers (integers or floats)
OA = float(OA)
AC = float(AC)
BD = float(BD)

# Use brief comments to explain what comparison you do between the defined variables
if OA < 6:
    # Check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)