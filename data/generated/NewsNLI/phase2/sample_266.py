# Premise: '' The letters were escalating in demands until they reached the $50,000 figure.
# Hypothesis: Spokesman:Letters escalated '' in demands until they reached the $50,000 figure''
# Golden Label: entailment

demands_premise = 50000
demands_hypothesis = 50000

# the hypothesis mentions the amount of demands, which is mentioned in the premise
if demands_hypothesis != demands_premise:
    # check if the amount of demands in the hypothesis contradicts the amount of demands reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

