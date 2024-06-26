# Define variables for the premise and hypothesis
first_hours_premise = 24
additional_hours_premise = 1.5
first_hours_hypothesis = 54
additional_hours_hypothesis = 1.5

# The hypothesis refers to Harry's pay rate for the first hours and additional hours worked that week
if first_hours_hypothesis!= first_hours_premise:
    # Check if the number of hours Harry is paid x dollars per hour contradicts the premise
    label = "contradiction"
elif additional_hours_hypothesis!= additional_hours_premise:
    # Check if the pay rate for additional hours contradicts the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
