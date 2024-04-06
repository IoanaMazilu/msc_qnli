# Premise: Christian’s father and the senior ranger gathered firewood as they walked towards the lake in the park and brought with them sacks, and every sack can contain around 20.0 pieces of wood.
# Hypothesis: They were able to gather 1604.0 pieces of firewood if they gathered 80.0 sacks.
# Golden Label: contradiction

wood_per_sack_premise = 20.0
total_firewood_hypothesis = 1604.0
total_sacks_hypothesis = 80.0

# the hypothesis refers to the total amount of firewood gathered, which is also mentioned in the premise
# compute the total amount of firewood according to the premise
total_firewood_premise = wood_per_sack_premise * total_sacks_hypothesis
if total_firewood_hypothesis != total_firewood_premise:
    # check if the total firewood from the hypothesis contradicts the total firewood from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

