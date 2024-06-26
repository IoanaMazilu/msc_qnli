# Define variables with representative names for the numerical entities in both inputs
people_invited_premise = 18.0
people_arrived_premise = 12.0
tables_premise = 3.0

# Extract all quantities as valid numbers
people_arrived_hypothesis = 10.0

# Use brief comments to explain what comparison you do between the defined variables
if people_arrived_hypothesis > people_invited_premise:
    # Check if the number of people who arrived exceeds the number of people invited
    label = "contradiction"
elif tables_premise < people_arrived_hypothesis / people_invited_premise:
    # Check if the number of tables needed is less than the number of people who arrived divided by the number of people invited
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
