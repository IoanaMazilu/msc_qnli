original_algae_premise = 3263.0
additional_algae_premise = 809.0
total_algae_hypothesis = 4072.0

# the hypothesis refers to the total number of algae in the lake, which is also mentioned in the premise
# compute the total number of algae plants in the premise
total_algae_premise = original_algae_premise + additional_algae_premise
if total_algae_hypothesis != total_algae_premise:
    # check if the total number of algae in the hypothesis contradicts the total number of algae from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
