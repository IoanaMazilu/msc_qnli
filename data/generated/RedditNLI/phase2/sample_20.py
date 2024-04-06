# Premise: Oil markets facing shortfall in the second half (ie. demand will surpass supply unless we fond another 1.5 million barrels of oil a day).
# Hypothesis: World oil demand will exceed supply in the second half of the year unless we can increase production by 1.5 million barrels a day.
# Golden Label: entailment

oil_shortfall_premise = 1.5
oil_shortfall_hypothesis = 1.5

# the hypothesis and premise mention the shortfall in oil production that needs to be addressed
if oil_shortfall_hypothesis != oil_shortfall_premise:
    # check if the shortfall estimate in the hypothesis contradicts the shortfall estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

