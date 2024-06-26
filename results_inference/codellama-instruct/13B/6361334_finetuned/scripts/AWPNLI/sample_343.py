father_and_ranger_premise = 2
sacks_premise = 6
wood_per_sack_premise = 20.0
wood_gathered_premise = 80.0

# the hypothesis refers to the number of sacks and the amount of wood gathered, which are also mentioned in the premise
# compute the total number of sacks in the premise
total_sacks_premise = father_and_ranger_premise * sacks_premise
if total_sacks_premise!= sacks_premise:
    # check if the number of sacks in the hypothesis contradicts the number of sacks from the premise
    label = "contradiction"
elif wood_gathered_premise / wood_per_sack_premise!= sacks_premise:
    # check if the amount of wood gathered in the hypothesis contradicts the amount of wood from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
