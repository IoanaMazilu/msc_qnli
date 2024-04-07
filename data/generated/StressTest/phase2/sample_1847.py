# Premise: At the end of'n'years, Sandy got back 3 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back 1 times the original investment.
# Golden Label: contradiction

investment_return_premise = 3
investment_return_hypothesis = 1

# the hypothesis refers to the amount Sandy got back at the end of 'n' years, also mentioned in the premise
if investment_return_hypothesis == investment_return_premise:
    # check if the amount Sandy got back in the hypothesis matches the amount stated in the premise
    label = "entailment"
elif investment_return_hypothesis > investment_return_premise:
    # check if the amount Sandy got back in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, it cannot contradict the premise
    # but it cannot be explicitly entailed from the premise either, as the premise states a higher return
    label = "neutral"

print(label)

