# Define variables for the numerical entities in the premise and hypothesis
boats_premise = 5.0
people_per_boat_premise = 3.0
people_hypothesis = 19.0

# Extract all quantities as valid numbers
total_boats_premise = boats_premise * people_per_boat_premise
total_people_hypothesis = people_hypothesis

# Use brief comments to explain what comparison you do between the defined variables
if total_people_hypothesis >= total_boats_premise:
    # Check if the total number of people in the hypothesis is greater than or equal to the total number of people in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
