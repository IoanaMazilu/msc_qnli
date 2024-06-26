pet_fish_premise = 26.0
pet_fish_eaten_premise = 6.0
total_pet_fish_premise = pet_fish_premise - pet_fish_eaten_premise
new_pet_fish_hypothesis = 20.0

# the hypothesis refers to the number of pet fish Sandy has now, which is also mentioned in the premise
# compute the total number of pet fish in the premise
total_pet_fish_hypothesis = total_pet_fish_premise
if new_pet_fish_hypothesis!= total_pet_fish_hypothesis:
    # check if the number of pet fish in the hypothesis contradicts the number of pet fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
