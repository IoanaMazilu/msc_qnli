# Premise: Dan spent $11.76 on a snake toy, and a cage cost him $14.54 and Dan also found a dollar bill on the ground.
# Hypothesis: The total cost of Dan's purchases is 26.3.
# Golden Label: entailment

snake_toy_cost_premise = 11.76
cage_cost_premise = 14.54
found_money_premise = 1
total_cost_hypothesis = 26.3

# the hypothesis refers to the total cost of the purchases, which are also mentioned in the premise
# compute the total cost in the premise
total_cost_premise = snake_toy_cost_premise + cage_cost_premise - found_money_premise

if total_cost_hypothesis != total_cost_premise:
    # check if the total cost in the hypothesis contradicts the total cost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

