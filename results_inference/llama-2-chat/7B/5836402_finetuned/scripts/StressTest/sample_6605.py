original_investment_premise = 2
original_investment_hypothesis = 2

# the hypothesis refers to the original investment mentioned in the premise
if original_investment_premise >= original_investment_hypothesis:
    # check if the estimate of 'original_investment_hypothesis' contradicts the number of original investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
