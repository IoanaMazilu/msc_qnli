# Define variables with representative names for the numerical entities in both inputs
amar_score = 64
bhavan_score = 36
chetan_score = 44

# Extract all quantities as valid numbers (integers or floats)

# Check if the hypothesis values contradict the premise
if amar_score >= 84:
    label = "contradiction"
elif bhavan_score!= 36 or chetan_score!= 44:
    label = "contradiction"
else:
    label = "entailment"

print(label)
