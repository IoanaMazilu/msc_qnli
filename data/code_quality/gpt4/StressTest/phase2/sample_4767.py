mary_investment_premise = 700
harry_investment_premise = 300
mary_investment_hypothesis = 400
harry_investment_hypothesis = 300

# the hypothesis refers to the investments of Mary and Harry mentioned in the premise
if mary_investment_premise <= mary_investment_hypothesis:
    # check if the estimate of 'mary_investment_hypothesis' contradicts the investment amount of Mary in the premise
    label = "contradiction"
elif harry_investment_hypothesis != harry_investment_premise:
    # check if the investment of Harry in the hypothesis contradicts the investment amount of Harry reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
