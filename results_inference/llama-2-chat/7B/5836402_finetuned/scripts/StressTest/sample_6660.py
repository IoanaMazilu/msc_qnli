money_given_premise = 40
money_given_hypothesis = 70

# the hypothesis refers to the percentage of money given by Jones, which is also mentioned in the premise
if money_given_premise >= money_given_hypothesis:
    # check if the estimate of'money_given_hypothesis' contradicts the percentage of money given in the premise
    label = "contradiction"
elif money_given_hypothesis < money_given_premise:
    # check if the percentage of money given in the hypothesis contradicts the percentage of money given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
