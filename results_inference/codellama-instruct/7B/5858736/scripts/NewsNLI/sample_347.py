# Define variables with representative names for the numerical entities in both inputs
people_premise = 1200000
people_hypothesis = 1200000

# Extract all quantities as valid numbers (integers or floats)
people_premise = int(people_premise)
people_hypothesis = int(people_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if people_hypothesis!= people_premise:
    # Check if the number of people who have viewed the video on YouTube contradicts the number of people who have viewed it
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
