# Premise: What will Sally have to sell each item for to generate a 15% profit?
# Hypothesis: What will Sally have to sell each item for to generate a less than 85% profit?
# Golden Label: entailment

profit_percentage_premise = 15
profit_percentage_hypothesis = 85

# the hypothesis refers to the profit percentage mentioned in the premise
if profit_percentage_hypothesis < profit_percentage_premise:
    # check if the hypothesis value contradicts the profit percentage in the premise
    label = "contradiction"
elif profit_percentage_hypothesis > profit_percentage_premise:
    # check if the hypothesis value is greater than the profit percentage in the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

