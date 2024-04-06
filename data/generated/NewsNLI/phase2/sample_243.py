# Premise: Chevron CEO David O'Reilly says his company's profit is about 7 percent.
# Hypothesis: O'Reilly:Chevron profits about 7 percent.
# Golden Label: entailment

profit_premise = 0.07
profit_hypothesis = 0.07

# the hypothesis mentions the profit percentage of Chevron, which is also mentioned in the premise
if profit_hypothesis != profit_premise:
    # check if the profit percentage in the hypothesis contradicts the profit percentage reported in the premise
    label = "contradiction"
else:
    # if the profit percentage in the hypothesis does not contradict the profit percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

