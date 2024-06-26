# Define variables for the premise and hypothesis
first_hours_premise = 12
additional_hours_premise = 1.5
first_hours_hypothesis = 82
additional_hours_hypothesis = 1.5

# The hypothesis refers to the hours of work and pay mentioned in the premise
if first_hours_hypothesis <= first_hours_premise:
    # Check if the number of hours in the first week mentioned in the hypothesis contradicts the number of hours in the first week mentioned in the premise
    label = "contradiction"
elif additional_hours_hypothesis!= additional_hours_premise:
    # Check if the pay rate for additional hours in the hypothesis contradicts the pay rate for additional hours in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
