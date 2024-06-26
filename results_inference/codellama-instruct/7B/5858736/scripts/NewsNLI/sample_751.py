# Define variables with representative names for the numerical entities in both inputs
gm_premise = 6-2
gm_hypothesis = 7-5

# Extract all quantities as valid numbers (integers or floats)
gm_premise = float(gm_premise.split("-")[0])
gm_hypothesis = float(gm_hypothesis.split("-")[0])

# Use brief comments to explain what comparison you do between the defined variables
if gm_hypothesis > gm_premise:
    # Check if the hypothesis mentions a higher number of games won than the premise
    label = "entailment"
else:
    # If the hypothesis does not mention a higher number of games won than the premise, we can infer neutrality
    label = "neutral"

print(label)
