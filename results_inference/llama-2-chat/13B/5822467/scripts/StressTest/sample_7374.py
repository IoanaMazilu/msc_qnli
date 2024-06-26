shift_premise = 16 * 4
shift_hypothesis = 36 * 4
order_premise = 40

# the hypothesis refers to the number of shifts and the average orders per hour, both mentioned in the premise
if shift_hypothesis <= shift_premise:
    # check if the estimate of'shift_hypothesis' contradicts the number of shifts reported in the premise
    label = "contradiction"
elif order_premise!= shift_hypothesis * order_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
