cylinder_oil_premise = 8
cylinder_oil_hypothesis = float(input("Enter the number of oil cylinders used: "))

# Check if the hypothesis value contradicts the premise value
if cylinder_oil_hypothesis > cylinder_oil_premise:
    label = "contradiction"
elif cylinder_oil_hypothesis <= cylinder_oil_premise:
    # Check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # The hypothesis value is not consistent with the premise value
    label = "entailment"

print(label)
