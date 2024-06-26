work_hours_premise = 8
work_hours_hypothesis = 1
average_order_value = 40

# the hypothesis refers to the work hours and average order value mentioned in the premise
if work_hours_premise == work_hours_hypothesis + 1:
    # check if the hypothesis value corresponds to the premise
    label = "entailment"
elif work_hours_premise != work_hours_hypothesis + 1:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict or correspond to the premise values, we can infer neutrality
    label = "neutral"

print(label)
