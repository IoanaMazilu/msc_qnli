father_wood = 80.0
ranger_wood = 80.0
sacks_hypothesis = 6.0
sacks_per_sack = 20.0

# the hypothesis refers to the number of sacks, which are also mentioned in the premise
# compute the total number of sacks in the premise
total_sacks_premise = father_wood / sacks_per_sack + ranger_wood / sacks_per_sack
if sacks_hypothesis > total_sacks_premise:
    # check if the number of sacks in the hypothesis contradicts the number of sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
