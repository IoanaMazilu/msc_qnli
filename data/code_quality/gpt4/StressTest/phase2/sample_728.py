profit_premise = 15
profit_hypothesis = 45

# the hypothesis is asking for the sales prices needed to generate a different profit percentage than the one mentioned in the premise
if profit_hypothesis == profit_premise:
    # check if the profit percentages in the hypothesis and premise are the same, which would mean entailment
    label = "entailment"
else:
    # the hypothesis is asking for a different profit percentage than the one mentioned in the premise
    # so it does not contradict the premise, but it cannot be fully and explicitly entailed from the premise either
    label = "neutral"

print(label)
