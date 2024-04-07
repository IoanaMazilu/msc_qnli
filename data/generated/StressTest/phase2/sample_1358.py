# Premise: What will be Rakesh’s share in the profit of 150000 earned at the end of three years from the start of the business in 1996?
# Hypothesis: What will be Rakesh’s share in the profit of more than 150000 earned at the end of three years from the start of the business in 1996?
# Golden Label: contradiction

profit_premise = 150000
profit_hypothesis = 150000

# the hypothesis refers to Rakesh's share in the profit mentioned in the premise
if profit_premise < profit_hypothesis:
    # check if the hypothesis value contradicts the profit amount in the premise
    label = "contradiction"
elif profit_hypothesis != profit_premise:
    # check if the hypothesis value contradicts the profit amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

