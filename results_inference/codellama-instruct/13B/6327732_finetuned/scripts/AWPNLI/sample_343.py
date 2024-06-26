father_gathered_wood_premise = 80.0
senior_ranger_gathered_wood_premise = 80.0
sacks_premise = 6.0
pieces_per_sack_premise = 20.0

# the hypothesis refers to the number of sacks and pieces of wood, which are also mentioned in the premise
# compute the total number of pieces of wood gathered by both fathers
total_wood_gathered_premise = father_gathered_wood_premise + senior_ranger_gathered_wood_premise
if total_wood_gathered_premise!= sacks_premise * pieces_per_sack_premise:
    # check if the number of pieces of wood in the hypothesis contradicts the number of pieces of wood from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
