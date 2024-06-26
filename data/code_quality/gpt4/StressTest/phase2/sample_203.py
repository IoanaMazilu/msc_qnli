working_days_premise = 5
working_days_hypothesis = 5

# the hypothesis refers to the number of days they both work together, also mentioned in the premise
if working_days_hypothesis != working_days_premise:
    # check if the number of working days in the hypothesis contradicts with the number of working days in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
