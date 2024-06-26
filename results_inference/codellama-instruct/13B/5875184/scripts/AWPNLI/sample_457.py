premise_algae_plants = 3263.0
hypothesis_algae_plants = 4074.0

# the hypothesis refers to the total number of algae plants in the lake, which is also mentioned in the premise
# compute the total number of algae plants in the premise
total_algae_plants_premise = premise_algae_plants + received_algae_plants_premise
if total_algae_plants_hypothesis!= total_algae_plants_premise:
    # check if the number of algae plants in the hypothesis contradicts the number of algae plants from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
