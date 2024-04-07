# Premise: At the end of'n'years, Sandy got back 5 times the original investment.
# Hypothesis: At the end of'n'years, Sandy got back more than 3 times the original investment.
# Golden Label: entailment

investment_return_premise = 5
investment_return_hypothesis = 3

# the hypothesis refers to the investment return mentioned in the premise
if investment_return_premise < investment_return_hypothesis:
    # check if the 'investment_return_hypothesis' contradicts the investment return in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

