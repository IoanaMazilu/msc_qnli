percentage_money_given_premise = 40
percentage_money_given_hypothesis = 70

# the hypothesis refers to the percentage of money given by Jones to his wife, mentioned in the premise
if percentage_money_given_hypothesis <= percentage_money_given_premise:
    # check if the estimate of 'percentage_money_given_hypothesis' contradicts the percentage of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
