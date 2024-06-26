sacks_per_section_premise = 45.0
sections_premise = 8.0
total_sacks_hypothesis = 361.0

# the hypothesis refers to the total number of sacks harvested daily, which can be computed from the premise
# compute the total number of sacks from the premise
total_sacks_premise = sacks_per_section_premise * sections_premise
if total_sacks_hypothesis != total_sacks_premise:
    # check if the total number of sacks in the hypothesis contradicts the total number of sacks from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
