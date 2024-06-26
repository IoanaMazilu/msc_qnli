# Define variables with representative names for the numerical entities in both inputs
people_premise = 120
percentage_premise = 60
people_hypothesis = 520

# Extract all quantities as valid numbers (integers or floats)
people_premise = int(people_premise)
percentage_premise = float(percentage_premise)
people_hypothesis = int(people_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if percentage_premise <= percentage_hypothesis:
    # Check if the estimate of 'percentage_hypothesis' contradicts the percentage reported in the premise
    label = "contradiction"
elif people_hypothesis!= people_premise:
    # Check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
