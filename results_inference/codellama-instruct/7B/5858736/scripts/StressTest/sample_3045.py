# Define variables with representative names for the numerical entities in both inputs
monday_hours_premise = 8
wednesday_hours_premise = 8
friday_hours_premise = 8
tuesday_hours_premise = 6
thursday_hours_premise = 6

monday_hours_hypothesis = 5
wednesday_hours_hypothesis = 5
friday_hours_hypothesis = 5
tuesday_hours_hypothesis = 6
thursday_hours_hypothesis = 6

# Extract all quantities as valid numbers (integers or floats)
monday_hours_premise = int(monday_hours_premise)
wednesday_hours_premise = int(wednesday_hours_premise)
friday_hours_premise = int(friday_hours_premise)
tuesday_hours_premise = int(tuesday_hours_premise)
thursday_hours_premise = int(thursday_hours_premise)

monday_hours_hypothesis = int(monday_hours_hypothesis)
wednesday_hours_hypothesis = int(wednesday_hours_hypothesis)
friday_hours_hypothesis = int(friday_hours_hypothesis)
tuesday_hours_hypothesis = int(tuesday_hours_hypothesis)
thursday_hours_hypothesis = int(thursday_hours_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if (monday_hours_hypothesis <= monday_hours_premise and
    wednesday_hours_hypothesis <= wednesday_hours_premise and
    friday_hours_hypothesis <= friday_hours_premise and
    tuesday_hours_hypothesis <= tuesday_hours_premise and
    thursday_hours_hypothesis <= thursday_hours_premise):
    # Check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
