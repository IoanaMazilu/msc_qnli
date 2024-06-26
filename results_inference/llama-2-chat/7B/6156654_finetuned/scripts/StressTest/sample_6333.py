working_days_premise = 7
total_days_task = 14
working_days_hypothesis = 2

# the hypothesis refers to the number of working days on the task before Blake joined, which is also mentioned in the premise
if working_days_hypothesis > working_days_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
