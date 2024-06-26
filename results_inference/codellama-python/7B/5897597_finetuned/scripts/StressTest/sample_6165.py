money_given_premise = 95
money_given_hypothesis = 85

# the hypothesis refers to the amount of money given to John mentioned in the premise
if money_given_premise <= money_given_hypothesis:
    # check if the estimate of'money_given_hypothesis' contradicts the amount of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
