# Premise: Dan spent $11.76 on a snake toy, and a cage cost him $14.54 and Dan also found a dollar bill on the ground.
# Hypothesis: The total cost of Dan's purchases is 23.9.
# Golden Label: contradiction

snake_toy_cost = 11.76
cage_cost = 14.54
found_money = 1

# the hypothesis refers to the total cost of Dan's purchases, which are also mentioned in the premise
# compute the total cost of the purchases in the premise
total_cost_premise = snake_toy_cost + cage_cost

total_cost_hypothesis = 23.9

if total_cost_hypothesis != total_cost_premise:
    # check if the total cost in the hypothesis contradicts the total cost from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

