original_investment_premise = 2
original_investment_hypothesis = 3

# the hypothesis refers to the original investment mentioned in the premise
if original_investment_premise <= original_investment_hypothesis:
    # check if the estimate of 'original_investment_hypothesis' contradicts the original investment in the premise
    label = "contradiction"
elif original_investment_hypothesis < original_investment_premise:
    # check if the original investment in the hypothesis contradicts the original investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
