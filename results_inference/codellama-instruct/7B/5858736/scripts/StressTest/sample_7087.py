# Define variables with representative names for the numerical entities in both inputs
dan_hours_premise = 8
dan_hours_hypothesis = 6
annie_hours_premise = 0
annie_hours_hypothesis = 0

# Extract all quantities as valid numbers (integers or floats)
dan_hours_premise = int(dan_hours_premise)
dan_hours_hypothesis = int(dan_hours_hypothesis)
annie_hours_premise = int(annie_hours_premise)
annie_hours_hypothesis = int(annie_hours_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if dan_hours_hypothesis <= dan_hours_premise:
    # Check if the estimate of 'dan_hours_hypothesis' contradicts the number of hours worked by Dan in the premise
    label = "contradiction"
elif annie_hours_hypothesis!= annie_hours_premise:
    # Check if the number of hours worked by Annie in the hypothesis contradicts the number of hours worked by Annie in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
