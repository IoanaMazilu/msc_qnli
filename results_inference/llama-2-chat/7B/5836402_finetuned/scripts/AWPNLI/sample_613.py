fish_total_premise = 261.0
fish_per_bowl_premise = 23.0
total_fishbowls_hypothesis = 12.5

# the hypothesis refers to the total number of fishbowls, which is also mentioned in the premise
# compute the total number of fishbowls from the premise
total_fishbowls_premise = fish_total_premise / fish_per_bowl_premise
if total_fishbowls_hypothesis!= total_fishbowls_premise:
    # check if the number of fishbowls in the hypothesis contradicts the number of fishbowls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
