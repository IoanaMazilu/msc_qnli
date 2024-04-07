# Premise: At the end of'n'years, Sandy got back 7 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back 1 times the original investment.
# Golden Label: contradiction

return_investment_premise = 7
return_investment_hypothesis = 1

# the hypothesis refers to the return on investment after 'n' years mentioned in the premise
if return_investment_premise == return_investment_hypothesis:
    # check if the return on investment in the hypothesis exactly matches the return mentioned in the premise
    label = "entailment"
elif return_investment_hypothesis > return_investment_premise:
    # check if the return on investment in the hypothesis contradicts the return reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

