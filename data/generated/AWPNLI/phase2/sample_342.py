# Premise: Christian’s father and the senior ranger gathered firewood as they walked towards the lake in the park and brought with them sacks, and every sack can contain around 20.0 pieces of wood.
# Hypothesis: They were able to fill 4.0 sacks if they gathered 80.0 pieces of wood.
# Golden Label: entailment

sacks_capacity_premise = 20.0
gathered_wood_hypothesis = 80.0
filled_sacks_hypothesis = 4.0

# the hypothesis refers to the number of filled sacks and gathered pieces of wood, which are also mentioned in the premise
# compute the total number of filled sacks from the premise using the gathered wood and the capacity of a sack
filled_sacks_premise = gathered_wood_hypothesis / sacks_capacity_premise
if filled_sacks_hypothesis != filled_sacks_premise:
    # check if the number of filled sacks in the hypothesis contradicts the number of filled sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

