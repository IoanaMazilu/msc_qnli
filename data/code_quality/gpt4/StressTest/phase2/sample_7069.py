shift_hours_premise = 2
shift_hours_hypothesis = 8
orders_per_hour = 40

# the hypothesis refers to the number of worked hours mentioned in the premise
if shift_hours_premise != shift_hours_hypothesis:
    # check if the number of worked hours in the hypothesis contradicts the number of worked hours reported in the premise
    label = "contradiction"
else:
    # if the hours in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)