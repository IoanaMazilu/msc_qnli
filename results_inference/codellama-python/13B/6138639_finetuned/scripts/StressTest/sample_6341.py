shifts_premise = 4
shifts_hypothesis = 4
average_premise = 40
average_hypothesis = 40

# the hypothesis refers to the number of shifts and average earnings per hour mentioned in the premise
if shifts_hypothesis <= shifts_premise:
    # check if the estimate of'shifts_hypothesis' contradicts the number of shifts in the premise
    label = "contradiction"
elif average_hypothesis!= average_premise:
    # check if the average earnings per hour in the hypothesis contradicts the average earnings per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
