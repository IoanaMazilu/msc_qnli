pet_fish_premise = 26.0
fish_bought_premise = 6.0
pet_fish_hypothesis = 27.0

# the hypothesis refers to the number of pet fish, which are also mentioned in the premise
# compute the total number of pet fish in the premise
total_pet_fish_premise = pet_fish_premise + fish_bought_premise
if total_pet_fish_hypothesis!= total_pet_fish_premise:
    # check if the number of pet fish in the hypothesis contradicts the number of pet fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
