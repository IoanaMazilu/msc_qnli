# Define variables with representative names for the numerical entities in both inputs
people_village_premise = 5
people_village_hypothesis = 5
deaths_bombardment_premise = 5
deaths_bombardment_hypothesis = 5
fear_remainder_premise = 15
fear_remainder_hypothesis = 15

# Extract all quantities as valid numbers (integers or floats)
people_village_premise = float(people_village_premise)
people_village_hypothesis = float(people_village_hypothesis)
deaths_bombardment_premise = float(deaths_bombardment_premise)
deaths_bombardment_hypothesis = float(deaths_bombardment_hypothesis)
fear_remainder_premise = float(fear_remainder_premise)
fear_remainder_hypothesis = float(fear_remainder_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if people_village_hypothesis <= people_village_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'people_village_premise'
    label = "contradiction"
elif deaths_bombardment_hypothesis <= deaths_bombardment_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'deaths_bombardment_premise'
    label = "contradiction"
elif fear_remainder_hypothesis <= fear_remainder_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'fear_remainder_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
