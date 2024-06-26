# Variables for premise and hypothesis
last_year_travel_premise = 0
last_year_travel_hypothesis = 6

# Check if hypothesis values contradict premise values
if last_year_travel_hypothesis <= last_year_travel_premise:
    label = "contradiction"
elif last_year_travel_hypothesis - last_year_travel_premise > 3:
    # Check if the difference between hypothesis and premise values is greater than 3, indicating entailment
    label = "entailment"
else:
    # If the hypothesis values are consistent with the premise values but cannot be explicitly entailed from them, label is neutral
    label = "neutral"

print(label)
