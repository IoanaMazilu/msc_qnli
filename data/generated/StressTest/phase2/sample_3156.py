# Premise: Sandy invested a certain sum of money at 8% p.
# Hypothesis: Sandy invested a certain sum of money at more than 2% p.
# Golden Label: entailment

investment_rate_premise = 8
investment_rate_hypothesis = 2

# the hypothesis refers to the investment rate mentioned in the premise
if investment_rate_premise <= investment_rate_hypothesis:
    # check if the estimate of 'investment_rate_hypothesis' contradicts the investment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

