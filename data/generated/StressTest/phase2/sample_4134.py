# Premise: Sandy invested a certain sum of money at 12% p.
# Hypothesis: Sandy invested a certain sum of money at less than 72% p.
# Golden Label: entailment

investment_rate_premise = 12
investment_rate_hypothesis = 72

# the hypothesis refers to the investment rate mentioned in the premise
if investment_rate_premise >= investment_rate_hypothesis:
    # check if the premise's investment rate contradicts the hypothesis's estimate of being less than 'investment_rate_hypothesis'
    label = "contradiction"
elif investment_rate_hypothesis > investment_rate_premise:
    # any investment rate that is less than 'investment_rate_hypothesis' but more than 'investment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
    
print(label)

