total_fish_premise = 261.0
fish_per_bowl_premise = 23.0
total_bowls_hypothesis = 12.5

# the hypothesis refers to the number of fishbowls, which can be computed from the premise
# compute the total number of fishbowls in the premise
total_bowls_premise = total_fish_premise / fish_per_bowl_premise
if total_bowls_hypothesis!= total_bowls_premise:
    # check if the number of fishbowls in the hypothesis contradicts the number of fishbowls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)