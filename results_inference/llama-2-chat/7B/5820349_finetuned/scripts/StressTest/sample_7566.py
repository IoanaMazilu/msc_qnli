shifts_premise = 4
shifts_hypothesis = 4
hours_per_shift = 12
orders_per_hour = 40
shifts_hours_premise = shifts_premise * hours_per_shift
shifts_hours_hypothesis = shifts_hypothesis * hours_per_shift

# the hypothesis refers to the number of hours Jill worked this week, mentioned in the premise
if shifts_hours_premise!= shifts_hours_hypothesis:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
