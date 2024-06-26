profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit at the end of the year mentioned in the premise
if profit_hypothesis > profit_premise:
    # check if the profit value in the hypothesis contradicts the exact profit value in the premise
    label = "contradiction"
elif profit_hypothesis < profit_premise:
    # check if the profit value in the hypothesis contradicts the exact profit value in the premise
    label = "contradiction"
else:
    # if the profit value in the hypothesis does not contradict the exact profit value in the premise, we can infer entailment
    label = "entailment"

print(label)
