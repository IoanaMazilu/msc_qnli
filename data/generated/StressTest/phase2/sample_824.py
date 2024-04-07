# Premise: Mary works in a restaurant a maximum of 70 hours.
# Hypothesis: Mary works in a restaurant a maximum of more than 70 hours.
# Golden Label: contradiction

max_work_hours_premise = 70

# the hypothesis refers to the maximum working hours of Mary mentioned in the premise
if max_work_hours_premise >= 70:
    # check if the estimate of 'max_work_hours_premise' contradicts the hypothesis of more than 70 hours
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

