shift_premise = 4 * 10
shift_hypothesis = 4 * 70
order_premise = 40
order_hypothesis = 40

# the hypothesis talks about the number of shifts and the average orders per hour, referenced also in the premise
if shift_hypothesis <= shift_premise:
    # check if the hypothesis value contradicts the estimate of more than'shift_premise' shifts
    label = "contradiction"
elif order_hypothesis!= order_premise:
    # check if the number of orders in the hypothesis contradicts the number of orders reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
