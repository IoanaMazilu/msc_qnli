father_gathered_wood_premise = 80
sacks_premise = 6
pieces_wood_per_sack = 20
filled_sacks_hypothesis = 6

# the hypothesis refers to the number of filled sacks, which is also mentioned in the premise
# compute the total number of pieces of wood gathered from the premise
total_wood_gathered_premise = father_gathered_wood_premise + filled_sacks_hypothesis * pieces_wood_per_sack

# check if the number of filled sacks in the hypothesis contradicts the number of pieces of wood gathered from the premise
if filled_sacks_hypothesis!= total_wood_gathered_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
