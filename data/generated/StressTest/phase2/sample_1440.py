# Premise: Mary works in a restaurant a maximum of 40 hours.
# Hypothesis: Mary works in a restaurant a maximum of more than 30 hours.
# Golden Label: entailment

max_hours_worked_premise = 40
max_hours_worked_hypothesis = 30

# the hypothesis talks about the maximum number of hours Mary works, referenced also in the premise
if max_hours_worked_hypothesis >= max_hours_worked_premise:
    # check if the hypothesis value contradicts the maximum number of hours worked as per the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

