months_later_premise = 4
months_later_hypothesis = 4
investment_premise = 30000
investment_hypothesis = 90000

# the hypothesis refers to the number of months and the investment amount mentioned in the premise
if months_later_hypothesis!= months_later_premise:
    # check if the number of months in the hypothesis contradicts the number of months in the premise
    label = "contradiction"
elif investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
