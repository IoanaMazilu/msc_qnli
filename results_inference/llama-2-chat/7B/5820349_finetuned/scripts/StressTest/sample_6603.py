return_investment_premise = 2
return_investment_hypothesis = 3

# the hypothesis refers to the return on investment mentioned in the premise
if return_investment_premise >= return_investment_hypothesis:
    # check if the estimate of'return_investment_premise' contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
