jones_money_premise = 60
jones_money_hypothesis = 40

# the hypothesis refers to the percentage of money given by Jones to his wife
if jones_money_hypothesis <= jones_money_premise:
    # check if the estimate of 'jones_money_hypothesis' contradicts the percentage of money given in the premise
    label = "contradiction"
elif jones_money_premise!= jones_money_hypothesis:
    # check if the percentage of money given in the hypothesis contradicts the percentage of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
