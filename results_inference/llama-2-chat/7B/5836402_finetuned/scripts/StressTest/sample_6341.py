shifts_premise = 4
shifts_hypothesis = 4

# the hypothesis refers to the number of shifts and the average orders per hour mentioned in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif shifts_hypothesis > shifts_premise:
    # if the hypothesis value is greater than the premise value, it is entailed
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
