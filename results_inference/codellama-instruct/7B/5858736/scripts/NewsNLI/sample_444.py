# Define variables with representative names for the numerical entities in both inputs
wales_differential_premise = 3
france_differential_premise = 0
scotland_differential_premise = -51

wales_differential_hypothesis = 3
france_differential_hypothesis = 0
scotland_differential_hypothesis = -51

# Extract all quantities as valid numbers (integers or floats)
wales_differential_premise = int(wales_differential_premise)
france_differential_premise = int(france_differential_premise)
scotland_differential_premise = int(scotland_differential_premise)

wales_differential_hypothesis = int(wales_differential_hypothesis)
france_differential_hypothesis = int(france_differential_hypothesis)
scotland_differential_hypothesis = int(scotland_differential_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if wales_differential_hypothesis!= wales_differential_premise:
    # Check if the difference in differential between Wales and France in the hypothesis contradicts the difference in differential reported in the premise
    label = "contradiction"
elif scotland_differential_hypothesis!= scotland_differential_premise:
    # Check if the difference in differential between Scotland and Wales in the hypothesis contradicts the difference in differential reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
