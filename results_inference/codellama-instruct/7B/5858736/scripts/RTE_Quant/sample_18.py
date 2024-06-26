# Define variables for the numerical entities in the premise and hypothesis
people_killed_premise = 70000
people_displaced_premise = 2000000
people_killed_hypothesis = 200000

# Extract all quantities as valid numbers
people_killed_premise = int(people_killed_premise)
people_displaced_premise = int(people_displaced_premise)
people_killed_hypothesis = int(people_killed_hypothesis)

# Perform calculations if necessary
total_people_affected = people_killed_premise + people_displaced_premise

# Use brief comments to explain what comparison you do between the defined variables
if people_killed_hypothesis > people_killed_premise:
    # Check if the number of people killed in the hypothesis is greater than the number of people killed in the premise
    label = "entailment"
elif people_killed_hypothesis < people_killed_premise:
    # Check if the number of people killed in the hypothesis is less than the number of people killed in the premise
    label = "contradiction"
else:
    # If the number of people killed in the hypothesis is equal to the number of people killed in the premise, we can infer neutrality
    label = "neutral"

print(label)
