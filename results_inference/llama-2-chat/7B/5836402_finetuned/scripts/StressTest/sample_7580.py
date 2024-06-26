days_work_premise = 8
days_work_hypothesis = 8

# the hypothesis refers to the number of days worked and the amount earned, both mentioned in the premise
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the number of days worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
