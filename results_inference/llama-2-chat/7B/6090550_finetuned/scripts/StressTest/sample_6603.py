original_investment_multiplier_premise = 2
original_investment_multiplier_hypothesis = 3

# the hypothesis refers to the original investment multiplier at the end of 'n' years, as mentioned in the premise
if original_investment_multiplier_premise > original_investment_multiplier_hypothesis:
    # check if the 'original_investment_multiplier_premise' contradicts the hypothesis statement
    label = "contradiction"
elif original_investment_multiplier_premise == original_investment_multiplier_hypothesis:
    # check if the 'original_investment_multiplier_premise' is equal to the 'original_investment_multiplier_hypothesis'
    label = "neutral"
else:
    # if the 'original_investment_multiplier_premise' is less than 'original_investment_multiplier_hypothesis', we can infer entailment
    label = "entailment"

print(label)
