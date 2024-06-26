father_sacks_premise = 20.0
ranger_sacks_premise = 20.0
wood_premise = 80.0
sacks_hypothesis = 6.0

# the hypothesis refers to the number of sacks filled, which are also mentioned in the premise
# compute the total number of pieces of wood gathered from the premise
total_wood_premise = father_sacks_premise * sacks_premise + ranger_sacks_premise * sacks_premise
if total_wood_hypothesis!= total_wood_premise:
    # check if the number of pieces of wood gathered in the hypothesis contradicts the number of pieces of wood from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
