fish_premise = 212.0
bought_fish_premise = 280.0
total_fish_hypothesis = 492.0

# the hypothesis refers to the total number of fish, which is also mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_premise + bought_fish_premise
if total_fish_hypothesis!= total_fish_premise:
    # check if the total number of fish in the hypothesis contradicts the total number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
