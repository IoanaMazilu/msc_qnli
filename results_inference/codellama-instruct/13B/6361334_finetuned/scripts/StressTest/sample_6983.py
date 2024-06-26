borrowed_money_premise = 6
borrowed_money_hypothesis = 8

# the hypothesis refers to the rate of borrowed money mentioned in the premise
if borrowed_money_hypothesis <= borrowed_money_premise:
    # check if the estimate of 'borrowed_money_hypothesis' contradicts the rate of borrowed money in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
