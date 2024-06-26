pet_fish_premise = 26.0
eaten_by_cat_premise = 6.0
total_fish_hypothesis = 20.0

# the hypothesis refers to the number of fish, which are also mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = pet_fish_premise - eaten_by_cat_premise
if total_fish_hypothesis!= total_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
