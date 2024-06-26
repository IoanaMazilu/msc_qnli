investment_rate_premise = 8
investment_rate_hypothesis = 6

# the hypothesis refers to the interest rate of Sandy's investment mentioned in the premise
if investment_rate_premise <= investment_rate_hypothesis:
    # check if the investment_rate_hypothesis contradicts the investment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
